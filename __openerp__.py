# -*- encoding: utf-8 -*-

{
    'name': 'Magento Integration',
    'author': 'Openlabs Technologies & Consulting Pvt Ltd.',
    'version': '0.1',
    'depends': [
        'base', 'sale'
    ],
    'category': 'Specific Industry Applications',
    'summary': 'Magento Integration',
    'description': """
This module integrates OpenERP with magento.
============================================

This will import the following:

* Product categories
* Products
* Customers
* Addresses
* Orders
    """,
    'data': ['magento.xml'],
    'css': [],
    'images': [],
    'demo': [],
    'installable': True,
    'application': True,
}