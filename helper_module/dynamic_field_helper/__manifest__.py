{
    "name": "Dynamic Field Helper",
    "version": "18.0.1.0.0",
    "category": "Tools",
    "summary": "Display dynamic, calculated help content for fields.",
    "author": "HosamAE",
    "maintainer": "HosamAE",
    "website": "https://github.com/HosamAE",
    "depends": ["web", "base"],
    "assets": {
        "web.assets_backend": [
            "dynamic_field_helper/static/src/xml/field_helper.xml",
            "dynamic_field_helper/static/src/js/dynamic_helper_icon.js",
            "dynamic_field_helper/static/src/js/field_patch.js",
            "dynamic_field_helper/static/src/scss/field_helper.scss"
        ],
        "web.assets_web_dark": [
            "dynamic_field_helper/static/src/scss/field_helper.dark.scss"
        ]
    },
    "data": [
        "views/res_partner_test_views.xml",
    ],
    "installable": True,
    "application": False,
}
