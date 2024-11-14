app_name = "github_apps"
app_title = "Github Apps"
app_publisher = "Dipangkar H"
app_description = "Gihub Test & Inport and Export the Data and the Entire Apps"
app_email = "idipangkar0@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "github_apps",
# 		"logo": "/assets/github_apps/logo.png",
# 		"title": "Github Apps",
# 		"route": "/github_apps",
# 		"has_permission": "github_apps.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/github_apps/css/github_apps.css"
# app_include_js = "/assets/github_apps/js/github_apps.js"

# include js, css files in header of web template
# web_include_css = "/assets/github_apps/css/github_apps.css"
# web_include_js = "/assets/github_apps/js/github_apps.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "github_apps/public/scss/website"

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
# app_include_icons = "github_apps/public/icons.svg"

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
# 	"methods": "github_apps.utils.jinja_methods",
# 	"filters": "github_apps.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "github_apps.install.before_install"
# after_install = "github_apps.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "github_apps.uninstall.before_uninstall"
# after_uninstall = "github_apps.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "github_apps.utils.before_app_install"
# after_app_install = "github_apps.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "github_apps.utils.before_app_uninstall"
# after_app_uninstall = "github_apps.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "github_apps.notifications.get_notification_config"

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
# 		"github_apps.tasks.all"
# 	],
# 	"daily": [
# 		"github_apps.tasks.daily"
# 	],
# 	"hourly": [
# 		"github_apps.tasks.hourly"
# 	],
# 	"weekly": [
# 		"github_apps.tasks.weekly"
# 	],
# 	"monthly": [
# 		"github_apps.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "github_apps.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "github_apps.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "github_apps.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["github_apps.utils.before_request"]
# after_request = ["github_apps.utils.after_request"]

# Job Events
# ----------
# before_job = ["github_apps.utils.before_job"]
# after_job = ["github_apps.utils.after_job"]

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
# 	"github_apps.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

