# 💡 Dynamic Field Helper Suite for Odoo 17.0

> **Target Framework:** Odoo 17.0 Community & Enterprise  
> **Author:** [Hossam Eldeen Eissa](https://www.linkedin.com/in/hossameldeen-eissa/)  
> **Email:** [hossamA.Eissa@gmail.com](mailto:hossamA.Eissa@gmail.com)  
> **License:** LGPL-3  
> Transform static field help strings into interactive, live-calculated, on-the-fly popovers.

---

## 🌟 Why Dynamic Field Helper?

In standard Odoo, `help="..."` is a dead static string. It cannot explain real-time calculations, display account credit balances, formula breakdowns, or live record state.

**Dynamic Field Helper** solves this by evaluating field helper methods on-demand with zero caching bottlenecks and zero impact on form load times.

---

## 🚀 Key Features

* **⚡ Live Real-Time Refresh:** Fetches fresh calculations dynamically on every hover (Zero stale cache).
* **📝 In-Memory Draft Support:** Accurately evaluates unsaved/dirty form data on-the-fly (`record.new(draft_values)`).
* **📐 4 Size Presets:** `helper_size="sm"` (Compact), `"md"` (Default), `"lg"` (KPI Grid), `"xl"` (360 Dashboard).
* **📌 Click-to-Pin:** Hover to glance, click to pin open. Dismisses seamlessly on outside click.
* **🔄 Smart Flipping Arrow:** Automatically detects viewport edges and flips orientation.
* **🌙 Native Dark Mode Support:** Tailored dark theme tokens declared in `web.assets_web_dark`.
* **🧩 Modular Architecture:** Core framework module (`dynamic_field_helper`) separated cleanly from interactive examples (`dynamic_field_helper_demo`).

---

## 💻 Developer Quick Start

### 1. Simple String Return (Mode 1)
```python
my_field = fields.Char(
    string="Account Quota",
    helper="_get_quota_helper",
    helper_size="sm",
)

def _get_quota_helper(self):
    return f"Live Available Quota: {self.quota - self.used_quota} hours"
```

### 2. Auto-Formatted Dictionary Card (Mode 2)
```python
price_field = fields.Float(
    string="Net Price",
    helper="_get_price_breakdown",
    helper_size="md",
)

def _get_price_breakdown(self):
    return {
        'base_rate': f"{self.base_price} kr/hr",
        'discount_applied': f"{self.discount_percent}%",
        'tax_estimate': f"{self.tax_amount} kr",
        'calculated_at': datetime.now().strftime('%H:%M:%S'),
    }
```

### 3. Full QWeb Template (Mode 3)
```python
vip_status = fields.Char(
    string="VIP Status",
    helper="_get_vip_data",
    helper_template="my_module.vip_popover_template",
    helper_size="lg",
)

def _get_vip_data(self):
    return {
        'customer_tier': 'Platinum Member',
        'points_balance': 15400,
    }
```

---

## 👨‍💻 Developer & Author

* **Author:** [Hossam Eldeen Eissa](https://www.linkedin.com/in/hossameldeen-eissa/)
* **Email:** [hossamA.Eissa@gmail.com](mailto:hossamA.Eissa@gmail.com)
* **LinkedIn:** [https://www.linkedin.com/in/hossameldeen-eissa/](https://www.linkedin.com/in/hossameldeen-eissa/)
* **Available for:** Odoo Enterprise Implementation, Custom Module Development, Performance Optimization & Consulting.
