import frappe
from frappe.model.document import Document
import shortuuid

class UTMLink(Document):
    def before_insert(self):
        self.short_code = shortuuid.uuid()[:8]