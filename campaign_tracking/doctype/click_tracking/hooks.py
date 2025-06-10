# Click Tracking DocType Hooks
from __future__ import unicode_literals
from frappe import _

def get_dashboard_data(data):
    """
    Configure dashboard for Click Tracking DocType
    """
    return {
        'fieldname': 'utm_link',
        'transactions': [
            {
                'label': _('UTM Link'),
                'items': ['UTM Link']
            }
        ]
    }