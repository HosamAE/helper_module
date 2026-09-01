# 💡 Dynamic Field Helper Suite for Odoo (Multi-Version)

> **Official Repository:** [HosamAE/helper_module](https://github.com/HosamAE/helper_module)  
> **Supported Versions:** Odoo 19.0 | Odoo 18.0 | Odoo 17.0 (Community & Enterprise)  
> **Author:** [HosamAE](https://www.linkedin.com/in/hossameldeen-eissa/)  
> **Email:** [hossamA.Eissa@gmail.com](mailto:hossamA.Eissa@gmail.com)  
> **License:** LGPL-3  

---

## 🌟 Overview

**Dynamic Field Helper** transforms static, unhelpful Odoo field help strings into interactive, live-calculated popovers on hover and click — without incurring any form-loading performance overhead.

---

## 🌿 Version Branches

| Branch | Odoo Version | Framework Engine | Status |
| :--- | :--- | :--- | :--- |
| [`19.0`](https://github.com/HosamAE/helper_module/tree/19.0) | **Odoo 19.0** | Pure OWL 2.0 + Draft In-Memory RPC | Production Ready |
| [`18.0`](https://github.com/HosamAE/helper_module/tree/18.0) | **Odoo 18.0** | Pure OWL 2.0 + Draft In-Memory RPC | Production Ready |
| [`17.0`](https://github.com/HosamAE/helper_module/tree/17.0) | **Odoo 17.0** | Pure OWL 2.0 + Draft In-Memory RPC | Production Ready |

---

## 📦 Modules in This Repository

1. **`dynamic_field_helper`**: Core framework module defining the OWL component, `_valid_field_parameter` ORM extensions, and real-time calculation RPC engine.
2. **`dynamic_field_helper_demo`**: Ready-to-test interactive demonstration module adding 4 size recipes on `res.partner` (Contacts).

---

## 🚀 Key Features

* **⚡ Zero Stale Cache:** Calculations run on-demand per hover/click.
* **📝 In-Memory Draft Support:** Evaluates unsaved form numbers before saving.
* **📐 4 Size Presets:** `helper_size="sm"` (Compact), `"md"` (Default), `"lg"` (KPI Grid), `"xl"` (360 Dashboard), or custom `helper_width="450px"`.
* **📌 Click-to-Pin:** Hover to glance, click to pin open. Dismisses seamlessly on outside click.
* **🔄 Smart Flipping Arrow:** Automatically detects viewport edges and flips orientation.
* **🌙 Native Dark Mode:** Full dark token styling in `web.assets_web_dark`.

---

## 👨‍💻 Developer & Author

* **Author:** [HosamAE](https://www.linkedin.com/in/hossameldeen-eissa/)
* **Email:** [hossamA.Eissa@gmail.com](mailto:hossamA.Eissa@gmail.com)
* **LinkedIn:** [https://www.linkedin.com/in/hossameldeen-eissa/](https://www.linkedin.com/in/hossameldeen-eissa/)
* **Available for:** Odoo Enterprise Implementation, Custom Module Development, Performance Optimization & Consulting.
