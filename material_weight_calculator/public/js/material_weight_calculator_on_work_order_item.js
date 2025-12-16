frappe.ui.form.on('Work Order Item', {
    design_structure: function(frm, cdt, cdn) {
        let row = frm.doc.required_items.find(r => r.name === cdn);

        if (!row || !row.item_code) {
            frappe.msgprint(__('Please select an Item first.'));
            return;
        }

        if (!row.shape) {
            frappe.msgprint(__('Please select a Shape first.'));
            return;
        }

        (async () => {
            try {
                let shape_doc = await frappe.db.get_doc('Shape', row.shape);

                if (!shape_doc || !shape_doc.critical_parameter?.length) {
                    return;
                }

                let critical_fields = shape_doc.critical_parameter.map(cp => {
                    let label = cp.parameter_name || cp.name1 || 'Parameter';
                    return {
                        label: label,
                        fieldname: label.toLowerCase().replace(/\s+/g, '_'),
                        fieldtype: 'Float',
                        default: 0
                    };
                });

                let item_doc = await frappe.db.get_doc('Item', row.item_code);
                let density_row = item_doc.density?.find(d => d.shape?.toLowerCase() === row.shape?.toLowerCase());
                let default_density = density_row?.density_kgmm3 || 0;

                let previous_params = {};
                if (row.item_parameters) {
                    try {
                        previous_params = JSON.parse(row.item_parameters);
                    } catch (e) {
                        previous_params = {};
                    }
                }

                let dialog_fields = [
                    ...critical_fields.map(f => ({
                        ...f,
                        default: previous_params[f.fieldname] || f.default
                    })),
                    { label: 'Density (kg/mm³)', fieldname: 'density', fieldtype: 'Float', precision: 9, default: previous_params.density || default_density },
                    { label: 'Gross Weight / Required Qty (Kg)', fieldname: 'weight_approx', fieldtype: 'Float', read_only: 1, default: previous_params.weight_approx || 0 }
                ];

                let d = new frappe.ui.Dialog({
                    title: `Enter Parameters for ${row.item_code} (${row.shape})`,
                    fields: dialog_fields,
                    primary_action_label: 'Save',
                    primary_action(values) {
                        let weight = parseFloat(d.get_value('weight_approx')) || 0;

                        // SAVE into required_qty
                        frappe.model.set_value(cdt, cdn, 'required_qty', weight);

                        let params = {};
                        critical_fields.forEach(f => params[f.fieldname] = values[f.fieldname]);
                        params.density = values.density;
                        params.required_qty = weight;
                        params.weight_approx = weight;

                        frappe.model.set_value(cdt, cdn, 'item_parameters', JSON.stringify(params));

                        d.hide();
                        frm.refresh_field('required_items');
                    }
                });

                const update_weight = () => {
                    let density = parseFloat(d.get_value('density')) || 0;
                    let weight = 0;

                    const find_field = (keywords) => {
                        keywords = Array.isArray(keywords) ? keywords : [keywords];
                        return critical_fields.find(f =>
                            keywords.some(k => f.label.toLowerCase().includes(k.toLowerCase()))
                        )?.fieldname;
                    };

                    if (row.shape.toLowerCase() === 'round') {
                        let diameter_field = find_field(['diameter', 'dia']);
                        let length_field = find_field(['length', 'len']);
                        if (diameter_field && length_field) {
                            let diameter = parseFloat(d.get_value(diameter_field)) || 0;
                            let length = parseFloat(d.get_value(length_field)) || 0;
                            weight = 3.1416 * Math.pow(diameter / 2, 2) * length * density;
                        }
                    } else if (row.shape.toLowerCase() === 'square') {
                        let length_field = find_field(['length', 'len']);
                        let width_field = find_field(['width', 'wid']);
                        let thickness_field = find_field(['thickness', 'thick', 'thk']);
                        if (length_field && width_field && thickness_field) {
                            let length = parseFloat(d.get_value(length_field)) || 0;
                            let width = parseFloat(d.get_value(width_field)) || 0;
                            let thickness = parseFloat(d.get_value(thickness_field)) || 0;
                            weight = length * width * thickness * density;
                        }
                    } else {
                        weight = 1;
                        dialog_fields.forEach(f => {
                            if (f.fieldname !== 'weight_approx') {
                                let val = parseFloat(d.get_value(f.fieldname));
                                if (!isNaN(val)) weight *= val;
                            }
                        });
                    }

                    d.set_value('weight_approx', weight);
                };

                dialog_fields.forEach(f => {
                    if (f.fieldname !== 'weight_approx' && d.fields_dict[f.fieldname]) {
                        let input = d.fields_dict[f.fieldname].input;
                        if (input) input.oninput = update_weight;
                    }
                });

                d.show();
                update_weight();

            } catch (err) {
                console.error("Error fetching Shape or Item data:", err);
                frappe.msgprint(__('Error fetching Shape or Item data. Check console for details.'));
            }
        })();
    }
});
