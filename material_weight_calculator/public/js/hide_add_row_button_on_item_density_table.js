frappe.ui.form.on('Material Weight Calculator', {
    onload: function(frm) {
        toggle_add_row_button(frm, 'material_details');
    },
    material_details_add: function(frm) {
        toggle_add_row_button(frm, 'material_details');
    },
    material_details_remove: function(frm) {
        toggle_add_row_button(frm, 'material_details');
    }
});

frappe.ui.form.on('Density Table', {
    onload: function(frm) {
        toggle_add_row_button(frm, 'density');
    },
    density_add: function(frm) {
        toggle_add_row_button(frm, 'density');
    },
    density_remove: function(frm) {
        toggle_add_row_button(frm, 'density');
    }
});

// Common function to toggle add-row button for any table field
function toggle_add_row_button(frm, table_field) {
    console.log(`Checking table: ${table_field}`);
    let table_length = frm.doc[table_field]?.length || 0;
    console.log(`Row count in ${table_field}: ${table_length}`);

    frm.set_df_property(
        table_field,
        'cannot_add_rows',
        table_length > 0 ? true : false
    );
}
