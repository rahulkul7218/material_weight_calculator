import frappe

def execute():
    doctype = "BOM Item"

    fields_to_add = [
        {
            "fieldname": "material_type",
            "label": "Material Type",
            "fieldtype": "Data",
              # Assuming you have a doctype named 'Material Type'
            "insert_after": "item_code"
        },
        {
            "fieldname": "shape",
            "label": "Shape",
            "fieldtype": "Data",
            # Assuming you have a doctype named 'Shape'
            "insert_after": "material_type"
        },
        {
            "fieldname": "density",
            "label": "Density",
            "fieldtype": "Data",
            # Assuming you have a doctype named 'Shape'
            "insert_after": "shape"
        }
    ]

    for field in fields_to_add:
        if not frappe.db.exists("Custom Field", {"dt": doctype, "fieldname": field["fieldname"]}):
            frappe.get_doc({
                "doctype": "Custom Field",
                "dt": doctype,
                "label": field["label"],
                "fieldname": field["fieldname"],
                "fieldtype": field["fieldtype"],
                "options": field.get("options"),
                "insert_after": field.get("insert_after"),
            }).insert()
            print(f"Added field {field['label']} to {doctype}")
        else:
            print(f"Field {field['label']} already exists in {doctype}")
