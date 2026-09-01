# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools.translate import _


class BaseModel(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super(BaseModel, self).fields_get(allfields, attributes)
        
        # We want to expose 'helper_method' if it exists on the field
        # Odoo fields store extra kwargs in _kwargs or we can check the attribute if usage is standard.
        # However, passing unknown args to Field() might raise TypeError in strict definitions,
        # but Odoo Field often eats kwargs.
        
        for field_name, schema in res.items():
            field_obj = self._fields.get(field_name)
            if field_obj:
                # Check for the custom attribute
                # In Odoo, extra arguments passed to field constructor are available in _args or as attributes if patched.
                # simpler approach: we expect the user to pass `helper_method` to the field.
                # Odoo's Field.__init__ does: self.args = args, self._kwargs = kwargs.
                # So we check field_obj._kwargs.get('helper_method') or getattr(field_obj, 'helper_method', None)
                
                # Note: To avoid 'Invalid Argument' errors on Field init, strictly speaking we might need to patch Field.__init__
                # But typically Odoo Field consumes **kwargs.
                
                helper = getattr(field_obj, "helper", None)
                if not helper:
                    _kwargs = getattr(field_obj, "_kwargs", {})
                    # Ensure _kwargs is a dict before calling .get()
                    if isinstance(_kwargs, dict):
                        helper = _kwargs.get("helper")
                
                if helper:
                    schema['helper'] = helper
                    
        return res

    @api.model
    def get_field_helper(self, record_id, field_name):
        """
        RPC Endpoint called by Frontend to evaluate the helper.
        :param record_id: ID of the record
        :param field_name: Name of the field having the helper
        :return: String or HTML content
        """
        if not record_id or not field_name:
            return False
            
        record = self.browse(record_id)
        if not record.exists():
            return False
            
        field_obj = self._fields.get(field_name)
        if not field_obj:
            return False
            
        # Get the method name
        # Get the method name
        helper_method_name = getattr(field_obj, "helper", None)
        if not helper_method_name:
            _kwargs = getattr(field_obj, "_kwargs", {})
            if isinstance(_kwargs, dict):
                helper_method_name = _kwargs.get("helper")
        
        if not helper_method_name:
            return False
            
        # Security/Validity Check
        if not hasattr(record, helper_method_name):
            return f"Error: Method '{helper_method_name}' not found on model '{self._name}'."
            
        # Call the method
        method = getattr(record, helper_method_name)
        try:
            result = method()
            return result
        except Exception as e:
            return f"Error evaluating helper: {str(e)}"
