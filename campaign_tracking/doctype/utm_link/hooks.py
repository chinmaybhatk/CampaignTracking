# UTM Link DocType Hooks
from __future__ import unicode_literals
from frappe import _

def get_dashboard_data(data):
    """
    Configure dashboard for UTM Link DocType
    """
    return {
        'fieldname': 'utm_link',
        'transactions': [
            {
                'label': _('Click Tracking'),
                'items': ['Click Tracking']
            }
        ]
    }