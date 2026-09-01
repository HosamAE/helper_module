# -*- coding: utf-8 -*-
import random
from datetime import datetime
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Example 1: Compact Size (sm)
    helper_simple_demo = fields.Char(
        string="Simple Live Helper (Size: SM)",
        helper="_get_simple_helper_demo",
        helper_size="sm",
        help="Compact mini popover."
    )

    # Example 2: Standard Size (md) Auto Dict Card
    helper_dict_demo = fields.Char(
        string="Dictionary Card (Size: MD)",
        helper="_get_dict_helper_demo",
        helper_size="md",
    )

    # Example 3: Large Size (lg) with KPI Grid & Progress Bar
    helper_qweb_demo = fields.Char(
        string="KPI Grid & Progress (Size: LG)",
        helper="_get_qweb_helper_demo",
        helper_template="dynamic_field_helper_demo.partner_qweb_kpi_popover",
        helper_size="lg",
    )

    # Example 4: Extra Large Size (xl) Full Customer 360 Dashboard
    helper_dashboard_demo = fields.Char(
        string="Executive 360 Dashboard (Size: XL)",
        helper="_get_dashboard_helper_demo",
        helper_template="dynamic_field_helper_demo.partner_qweb_dashboard_popover",
        helper_size="xl",
    )

    def _get_simple_helper_demo(self):
        now_str = datetime.now().strftime('%H:%M:%S')
        return f"""
            <div class='text-center py-1'>
                <div class='small text-muted mb-1'>Live System Time</div>
                <div class='fw-bold text-success font-monospace fs-6'>{now_str}</div>
            </div>
        """

    def _get_dict_helper_demo(self):
        return {
            'partner_name': self.name or 'New Customer',
            'live_clock': datetime.now().strftime('%H:%M:%S'),
            'random_score': f"{random.randint(85, 99)}% (Live)",
            'credit_available': f"{random.randint(10, 50) * 1000:,} kr",
            'status': 'Active (Real-Time)',
        }

    def _get_qweb_helper_demo(self):
        used_credit = random.randint(20, 80)
        return {
            'partner_name': self.name or 'Draft Partner',
            'is_company_partner': bool(self.is_company),
            'status_label': 'Enterprise VIP' if self.is_company else 'Individual Account',
            'credit_score': random.randint(700, 850),
            'live_clock': datetime.now().strftime('%H:%M:%S'),
            'used_credit_pct': used_credit,
            'credit_limit_str': '100,000 kr',
            'spent_str': f"{used_credit * 1000:,} kr",
        }

    def _get_dashboard_helper_demo(self):
        return {
            'partner_name': self.name or 'Account Summary',
            'total_sales': f"{random.randint(45, 120) * 1000:,.2f} kr",
            'open_invoices': random.randint(1, 5),
            'paid_invoices': random.randint(10, 25),
            'on_time_delivery': f"{random.randint(92, 99)}%",
            'satisfaction_rating': f"{random.uniform(4.5, 5.0):.1f} / 5.0",
            'refreshed_at': datetime.now().strftime('%H:%M:%S'),
        }
