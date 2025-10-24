import frappe

def create_custom_field(doc, method=None):
    target_doctype = "Material Weight Calculator"
    field_label = doc.name.strip()
    fieldname = frappe.scrub(field_label)

    if not frappe.db.exists("Custom Field", {"dt": target_doctype, "fieldname": fieldname}):
        custom_field = frappe.get_doc({
            "doctype": "Custom Field",
            "dt": target_doctype,
            "label": field_label,
            "fieldname": fieldname,
            "fieldtype": "Int",
            "insert_after": "last_field",
            "in_list_view": 1
        })
        custom_field.insert(ignore_permissions=True)
        frappe.db.commit()
        # frappe.msgprint(f"✅ Field '{field_label}' added to {target_doctype}.")
    # else:
    #     frappe.msgprint(f"⚠️ Field '{field_label}' already exists in {target_doctype}.")


