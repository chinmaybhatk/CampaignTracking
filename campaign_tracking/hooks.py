from . import __version__ as app_version

app_name = "campaign_tracking"
app_title = "Campaign Tracking"
app_publisher = "Chinmay Bhatk"
app_description = "Campaign and UTM Link Tracking"
app_email = "chinmay@example.com"
app_license = "MIT"
app_version = app_version

# Includes in <head>
app_include_css = "/assets/campaign_tracking/css/campaign_tracking.css"
app_include_js = "/assets/campaign_tracking/js/campaign_tracking.js"

# DocTypes for fixtures
fixtures = [
    {
        "dt": "DocType", 
        "filters": [
            ["name", "in", ["UTM Link", "Click Tracking"]]
        ]
    }
]

# Web Routes
website_route_rules = [
    {"name": "utm_redirect", "page_name": "utm_redirect", "generator": "UTM Link"}
]

# Permissions
permission_query_conditions = {
    "UTM Link": "campaign_tracking.utils.permissions.get_permission_query_conditions",
    "Click Tracking": "campaign_tracking.utils.permissions.get_permission_query_conditions"
}

# Dashboard configurations
dashboards = {
    "UTM Link": "campaign_tracking/doctype/utm_link/utm_link_dashboard.py"
}

# Scheduler Tasks
scheduler_events = {
    "daily": [
        "campaign_tracking.utils.analytics.cleanup_old_tracking_data"
    ]
}

# Customizations and Extensions
override_doctype_class = {
    "UTM Link": "campaign_tracking.controllers.utm_link.CustomUTMLink"
}

# Notification configurations
notification_config = "campaign_tracking.utils.notifications.get_notification_config"