# -*- coding: utf-8 -*-
import json
from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval

# Register dynamic helper parameters in valid field parameters
if hasattr(models.BaseModel, '_valid_field_parameter'):
    models.BaseModel._valid_field_parameter.update(['helper', 'helper_template', 'helper_size', 'helper_width'])


class Base(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def _valid_field_parameter(self, field, name):
        if name in ('helper', 'helper_template', 'helper_size', 'helper_width'):
            return True
        return super()._valid_field_parameter(field, name)

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super().fields_get(allfields=allfields, attributes=attributes)
        for fname, field in self._fields.items():
            if fname in res:
                if getattr(field, 'helper', None):
                    res[fname]['has_dynamic_helper'] = True
                if getattr(field, 'helper_size', None):
                    res[fname]['helper_size'] = getattr(field, 'helper_size')
                if getattr(field, 'helper_width', None):
                    res[fname]['helper_width'] = getattr(field, 'helper_width')
        return res

    @api.model
    def get_field_helper(self, record_id=False, field_name=False, draft_values=None):
        if not field_name or field_name not in self._fields:
            return ""

        field = self._fields[field_name]
        helper_attr = getattr(field, 'helper', None)
        helper_template = getattr(field, 'helper_template', None)

        if not helper_attr:
            return ""

        # Use existing record or create draft record with in-memory dirty values
        record = self.browse(record_id) if record_id else self
        if draft_values and isinstance(draft_values, dict):
            try:
                record = record.new(draft_values)
            except Exception:
                pass

        # Evaluate helper attribute
        helper_content = ""
        if isinstance(helper_attr, str) and hasattr(record, helper_attr):
            helper_method = getattr(record, helper_attr)
            if callable(helper_method):
                try:
                    helper_content = helper_method()
                except Exception as e:
                    return f"<div class='text-danger'>Error calculating helper: {str(e)}</div>"
        elif callable(helper_attr):
            try:
                helper_content = helper_attr(record)
            except Exception as e:
                return f"<div class='text-danger'>Error calculating helper: {str(e)}</div>"
        else:
            helper_content = str(helper_attr)

        # Mode 3: Render QWeb template if specified
        if helper_template:
            try:
                qcontext = {
                    'record': record,
                    'env': self.env,
                    'helper_data': helper_content,
                }
                if isinstance(helper_content, dict):
                    qcontext.update(helper_content)
                return self.env['ir.qweb']._render(helper_template, qcontext)
            except Exception as e:
                return f"<div class='text-danger'>Error rendering QWeb template: {str(e)}</div>"

        # Mode 2: Auto-generate sleek Key-Value card if dict
        if isinstance(helper_content, dict):
            rows = ""
            for k, v in helper_content.items():
                label = k.replace('_', ' ').title()
                rows += f"""
                <div class="d-flex justify-content-between align-items-center py-1 border-bottom border-light">
                    <span class="text-muted small">{label}:</span>
                    <span class="fw-semibold text-dark ms-3">{v}</span>
                </div>
                """
            return f"""
            <div class="o_dynamic_helper_dict_card">
                {rows}
            </div>
            """

        return str(helper_content)
