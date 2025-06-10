import frappe

def before_install():
    frappe.log("Campaign Tracking: Before Install")

def after_install():
    frappe.log("Campaign Tracking: After Install")