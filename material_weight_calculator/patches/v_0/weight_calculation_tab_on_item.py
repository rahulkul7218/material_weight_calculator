import frappe

def execute():
    # Step 1: Create Tab Break for "Mould Details"
    if not frappe.db.exists("Custom Field", {"dt": "Item", "fieldname": "weight_calculation_tab"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Item",
            "fieldname": "weight_calculation_tab",
            "label": "Weight Calculation Details",
            "fieldtype": "Tab Break",
            "insert_after": "weight_approx"
        }).insert(ignore_permissions=True)

    # Step 2: Create Section Break inside Mould Details tab
    if not frappe.db.exists("Custom Field", {"dt": "Item", "fieldname": "weight_calculation_section"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Item",
            "fieldname": "weight_calculation_section",
            "label": "Weight Calculation Section",
            "fieldtype": "Section Break",
            "insert_after": "weight_calculation_tab"
        }).insert(ignore_permissions=True)

    # Step 3: Create custom fields under the section
    custom_fields = [
        
        {
            "fieldname": "Density",
            "label": "Density",
            "fieldtype": "Table",
            "options": "Density Table",
            "insert_after": "weight_calculation_section"
        }
    ]

    for field in custom_fields:
        if not frappe.db.exists("Custom Field", {"dt": "Item", "fieldname": field["fieldname"]}):
            frappe.get_doc({
                "doctype": "Custom Field",
                "dt": "Item",
                **field
            }).insert(ignore_permissions=True)

    frappe.db.commit()
