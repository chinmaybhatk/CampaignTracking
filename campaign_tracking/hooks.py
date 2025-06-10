from . import __version__ as app_version

app_name = "campaign_tracking"
app_title = "Campaign Tracking"
app_publisher = "Chinmay Bhat"
app_description = "Campaign and UTM Link Tracking"
app_version = app_version
app_email = "chinmaybhatk@gmail.com"
app_license = "MIT"

before_install = "campaign_tracking.utils.install.before_install"
after_install = "campaign_tracking.utils.install.after_install"

fixtures = [
    {
        "dt": "DocType", 
        "filters": [
            ["name", "in", ["UTM Link"]]
        ]
    }
]