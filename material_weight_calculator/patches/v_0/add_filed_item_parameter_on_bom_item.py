import frappe

def execute():
    doctype = "BOM Item"
    fieldname = "item_parameters"

    # Check if field already exists
    if not frappe.db.exists("Custom Field", {"dt": doctype, "fieldname": fieldname}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": doctype,
            "fieldname": 'item_parameters',
            "label": "Item Parameters",
            "fieldtype": "Small Text",
            "insert_after": "item_code",
            "no_copy": 1
        }).insert(ignore_permissions=True)
        frappe.db.commit()
        print(f"Custom field '{fieldname}' added to {doctype}")
    else:
        print(f"Custom field '{fieldname}' already exists in {doctype}")
