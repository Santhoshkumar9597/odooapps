{
    'name': 'Appointment Email From Override',
    'version': '18.0.1.0.0',
    'author': 'Santhosh',
    'category': 'Productivity',
    'website': 'https://github.com/Santhoshkumar9597',
    'summary': 'Force static From email in appointment emails',
    'description': """
This module allows you to override the default sender email address 
for appointment-related emails in Odoo.

Features:
- Set a static "From" email address
- Applies to appointment booking emails
- Ensures consistent sender identity
- Easy configuration

Use Case:
Useful when companies want all appointment emails to be sent 
from a centralized email address instead of user-specific emails.
""",
    'depends': ['mail', 'calendar', 'appointment'],
    'images': ['static/description/banner.png'],
    'price': 0,
    'currency': 'USD',
    'installable': True,
    'application': False,
    "license": "LGPL-3",
}
