/** @odoo-module **/

import { Field } from '@web/views/fields/field';
import { patch } from '@web/core/utils/patch';
import { DynamicHelperIcon } from './dynamic_helper_icon';

patch(Field.prototype, {
  setup() {
    super.setup();
  },

  get hasDynamicHelper() {
    // Check if the parameter exists in the field definition
    // this.props.record.fields contains the model definition
    if (this.props.record && this.props.record.fields) {
      const fieldDef = this.props.record.fields[this.props.name];
      return fieldDef && fieldDef.helper;
    }
    return false;
  },
});

// We need to register the component to be available in the template
// Since Field is a component, we can add to its components list?
// No, standard way in Odoo 17 to expose components to templates patched via inheritance
// is to ensure they are available in the scope or added to the component.
// Patching the components static property:
Field.components = {
  ...Field.components,
  DynamicHelperIcon,
};
