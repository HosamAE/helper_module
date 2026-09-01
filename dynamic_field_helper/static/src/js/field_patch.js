/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Field } from "@web/views/fields/field";
import { DynamicHelperIcon } from "./dynamic_helper_icon";

patch(Field, {
    components: {
        ...Field.components,
        DynamicHelperIcon,
    },
});

patch(Field.prototype, {
    get hasDynamicHelper() {
        const fieldDef = this.props.record?.fields?.[this.props.name];
        return Boolean(fieldDef && fieldDef.has_dynamic_helper);
    },
});
