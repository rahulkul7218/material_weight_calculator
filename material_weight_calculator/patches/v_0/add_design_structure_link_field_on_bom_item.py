import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def execute():
    custom_field = {
        "BOM Item": [
            dict(
                fieldname="design_structure",
                label="Design Instruction",
                fieldtype="Button",
                insert_after="item_code",
                in_list_views=1
                
            )
        ]
    }

    for doctype, fields in custom_field.items():
        for field in fields:
            create_custom_field(doctype, field)
