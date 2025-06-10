import frappe
from frappe.model.document import Document

class ClickTracking(Document):
    def before_insert(self):
        """
        Perform any pre-insertion logic
        """
        # Optional: Validate or modify data before insertion
        if not self.clicked_at:
            self.clicked_at = frappe.utils.now()
    
    def validate(self):
        """
        Validate click tracking entry
        """
        # Ensure UTM Link exists
        if not frappe.db.exists('UTM Link', self.utm_link):
            frappe.throw(f"UTM Link {self.utm_link} does not exist")
    
    @staticmethod
    def get_click_stats(utm_link):
        """
        Get click statistics for a specific UTM link
        """
        return frappe.get_all('Click Tracking', 
            filters={'utm_link': utm_link},
            fields=['name', 'clicked_at', 'ip_address', 'country', 'region']
        )
    
    def enrich_tracking_data(self):
        """
        Enrich click tracking data with additional information
        """
        try:
            # Optional: Add geolocation enrichment
            from geoip2.database import Reader
            
            if self.ip_address:
                try:
                    with Reader('/path/to/geolite2/GeoLite2-City.mmdb') as reader:
                        response = reader.city(self.ip_address)
                        self.country = response.country.name
                        self.region = response.subdivisions.most_specific.name
                        self.city = response.city.name
                except Exception as e:
                    frappe.log_error(f"Geolocation enrichment error: {str(e)}")
        except ImportError:
            frappe.log_error("geoip2 module not installed")