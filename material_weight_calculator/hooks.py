app_name = "material_weight_calculator"
app_title = "material weight calculator"
app_publisher = "Assimilate Technologies Pvt Ltd"
app_description = "material weight calculator"
app_email = "info@assimilatetechnologies.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "material_weight_calculator",
# 		"logo": "/assets/material_weight_calculator/logo.png",
# 		"title": "material weight calculator",
# 		"route": "/material_weight_calculator",
# 		"has_permission": "material_weight_calculator.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/material_weight_calculator/css/material_weight_calculator.css"
# app_include_js = "/assets/material_weight_calculator/js/material_weight_calculator.js"

# include js, css files in header of web template
# web_include_css = "/assets/material_weight_calculator/css/material_weight_calculator.css"
# web_include_js = "/assets/material_weight_calculator/js/material_weight_calculator.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "material_weight_calculator/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "material_weight_calculator/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "material_weight_calculator.utils.jinja_methods",
# 	"filters": "material_weight_calculator.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "material_weight_calculator.install.before_install"
# after_install = "material_weight_calculator.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "material_weight_calculator.uninstall.before_uninstall"
# after_uninstall = "material_weight_calculator.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "material_weight_calculator.utils.before_app_install"
# after_app_install = "material_weight_calculator.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "material_weight_calculator.utils.before_app_uninstall"
# after_app_uninstall = "material_weight_calculator.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "material_weight_calculator.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"material_weight_calculator.tasks.all"
# 	],
# 	"daily": [
# 		"material_weight_calculator.tasks.daily"
# 	],
# 	"hourly": [
# 		"material_weight_calculator.tasks.hourly"
# 	],
# 	"weekly": [
# 		"material_weight_calculator.tasks.weekly"
# 	],
# 	"monthly": [
# 		"material_weight_calculator.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "material_weight_calculator.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "material_weight_calculator.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "material_weight_calculator.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["material_weight_calculator.utils.before_request"]
# after_request = ["material_weight_calculator.utils.after_request"]

# Job Events
# ----------
# before_job = ["material_weight_calculator.utils.before_job"]
# after_job = ["material_weight_calculator.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"material_weight_calculator.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

after_migrate = [
   "material_weight_calculator.patches.v_0.weight_calculation_tab_on_item.execute",
   "material_weight_calculator.patches.v_0.add_wt_calculation_table_on_bom.execute",
   "material_weight_calculator.patches.v_0.add_design_structure_link_field_on_bom_item.execute",
   "material_weight_calculator.patches.v_0.add_material_type_and_shape_on_bom_item.execute",
   "material_weight_calculator.patches.v_0.add_filed_item_parameter_on_bom_item.execute",
   "material_weight_calculator.patches.v_0.add_design_structure_link_field_on_work_order_item.execute"
   

    
]


doctype_js = {
	"Material Weight Calculator":"public/js/hide_add_row_button_on_item_density_table.js",
   "Item":"public/js/hide_add_row_button_on_item_density_table.js",
   "BOM":["public/js/dialog_box.js","public/js/fetched_material_type_and_shape_fromitem_on_bom_item_table.js"],
   "Work Order": ["public/js/fetched_density_of_material_on_work_order_item.js","public/js/material_weight_calculator_on_work_order_item.js"]
}

doc_events = {
   "Parameter Name": {
        "after_insert": "material_weight_calculator.api.create_field_dynamically.create_custom_field",
        
    }
}



