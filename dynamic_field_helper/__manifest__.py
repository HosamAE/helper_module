# -*- coding: utf-8 -*-
{
    'name': 'Dynamic Field Helper',
    'version': '19.0.1.0.0',
    'category': 'Productivity/Tools',
    'summary': 'Display dynamic, live-calculated help content for fields on-the-fly.',
    'description': """
Dynamic Field Helper for Odoo 19.0
===================================
Transform static field help into interactive, real-time calculated popovers.

Key Capabilities:
-----------------
* Live Real-Time Fetching: Fetches calculations dynamically on every hover (Zero stale cache).
* Draft/Dirty Data Support: Evaluates in-memory draft values for unsaved records.
* Tri-Mode Architecture:
  1. Simple String / HTML return from Python methods.
  2. Auto-generated sleek Key-Value cards from Python dictionaries.
  3. Full QWeb Template support with responsive Bootstrap design.
* Native Dark Mode: Dedicated dark token styling in web.assets_web_dark.
* Pure & Lightweight: Zero external dependencies, pure OWL 2.0 component.
""",
    'author': 'HosamAE',
    'maintainer': 'HosamAE',
    'website': 'https://www.linkedin.com/in/hossameldeen-eissa/',
    'support': 'hossamA.Eissa@gmail.com',
    'license': 'LGPL-3',
    'depends': ['web', 'base'],
    'images': [
        'static/description/banner.png',
    ],
    'assets': {
        'web.assets_backend': [
            'dynamic_field_helper/static/src/scss/field_helper.scss',
            'dynamic_field_helper/static/src/xml/field_helper.xml',
            'dynamic_field_helper/static/src/js/dynamic_helper_icon.js',
            'dynamic_field_helper/static/src/js/field_patch.js',
        ],
        'web.assets_web_dark': [
            'dynamic_field_helper/static/src/scss/field_helper.dark.scss',
        ],
    },
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
