frappe.ui.form.on('BOM Item', {
    item_code: async function(frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);
        if (!row.item_code) return;

        try {
            // Fetch the selected Item document
            let item_doc = await frappe.db.get_doc('Item', row.item_code);

            if (!item_doc.density || item_doc.density.length === 0) {
                // frappe.msgprint(__('No Density data found for this Item.'));
                return;
            }

            // If multiple rows exist in density table, you can choose the first or implement logic to select
            let density_row = item_doc.density[0];

            // Set fields in BOM Item
            frappe.model.set_value(cdt, cdn, 'material_type', density_row.material_type || '');
            frappe.model.set_value(cdt, cdn, 'shape', density_row.shape || '');
            frappe.model.set_value(cdt, cdn, 'density', density_row.density_kgmm3 || '');

        } catch (err) {
            console.error('Error fetching Item data:', err);
            frappe.msgprint(__('Error fetching Item density data. Check console for details.'));
        }
    }
});
