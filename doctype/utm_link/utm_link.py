import frappe
from frappe.model.document import Document
import shortuuid
from datetime import datetime, timedelta

class UTMLink(Document):
    def before_insert(self):
        """
        Generate unique short code and set default expiry
        """
        self.short_code = self._generate_unique_short_code()
        
        # Set default expiry if not specified
        if not self.expiry_date:
            self.expiry_date = datetime.now() + timedelta(days=90)
    
    def _generate_unique_short_code(self, length=8):
        """
        Generate a unique short code ensuring no duplicates
        """
        while True:
            code = shortuuid.uuid()[:length]
            if not frappe.db.exists('UTM Link', {'short_code': code}):
                return code
    
    def validate(self):
        """
        Validate UTM link before saving
        """
        # Validate URL
        if not self.original_url:
            frappe.throw("Original URL is required")
        
        # Validate max clicks
        if self.max_clicks_allowed and self.max_clicks_allowed < 0:
            frappe.throw("Max clicks must be a positive number")
    
    def is_expired(self):
        """
        Check if link is expired
        """
        if self.expiry_date:
            return datetime.now().date() > self.expiry_date
        return False
    
    def track_click(self):
        """
        Track individual link click
        """
        # Increment total clicks
        self.total_clicks = (self.total_clicks or 0) + 1
        self.last_clicked = frappe.utils.now()
        
        # Check click limit
        if self.max_clicks_allowed and self.total_clicks > self.max_clicks_allowed:
            frappe.throw("Maximum click limit reached")
        
        # Create click tracking entry
        frappe.get_doc({
            'doctype': 'Click Tracking',
            'utm_link': self.name,
            'clicked_at': frappe.utils.now(),
            'ip_address': frappe.local.request_ip,
            'user_agent': frappe.request.headers.get('User-Agent', '')
        }).insert()
        
        self.save()
        return self.original_url

    @staticmethod
    def get_utm_link(short_code):
        """
        Retrieve UTM link by short code
        """
        return frappe.get_doc('UTM Link', {'short_code': short_code})