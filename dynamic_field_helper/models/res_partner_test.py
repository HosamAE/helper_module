import random
from datetime import datetime

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Test Field 1: Static return
    dynamic_helper_test = fields.Char(
        string="Dynamic Helper Test",
        helper="_get_dynamic_helper_content",
        help="This is the standard static help."
    )

    def _get_dynamic_helper_content(self):
        """
        Return dynamic content including timestamp and random value.
        """
        return f"""
            <div style='color: #017e84; font-weight: bold;'>
                Dynamic Helper Active!
            </div>
            <ul>
                <li>Record: {self.name}</li>
                <li>ID: {self.id}</li>
                <li>Time: {datetime.now().strftime('%H:%M:%S')}</li>
                <li>Random: {random.randint(1, 100)}</li>
            </ul>
            <small>This content is generated on the fly!</small>
        """
