import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "BOM": [
            {
                "fieldname": "weight_calculation",
                "label": "Weight Calculation",
                "fieldtype": "Table",
                "options": "Material Weight Calculator",
                "insert_after": "items"
                
            }
        ]
    }

    create_custom_fields(custom_fields)
    frappe.db.commit()
