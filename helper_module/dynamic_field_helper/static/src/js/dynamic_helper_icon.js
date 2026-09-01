/** @odoo-module **/

import { Component, useState, markup } from '@odoo/owl';
import { useService } from '@web/core/utils/hooks';
import { Popover } from '@web/core/popover/popover';

export class DynamicHelperIcon extends Component {
  setup() {
    this.orm = useService('orm');
    this.popover = useService('popover');
    this.state = useState({
      content: null,
      loading: false,
    });

    this.closePopover = null;
  }

  async onMouseEnter(ev) {
    if (this.closePopover) return; // Already open

    const target = ev.currentTarget;

    if (!this.state.content) {
      this.state.loading = true;
      try {
        const resId = this.props.record.resId;
        const model = this.props.record.resModel;
        const fieldName = this.props.fieldName;

        if (!resId) {
          this.state.content = markup('<i>Please save the record to view help.</i>');
        } else {
          const result = await this.orm.call(model, 'get_field_helper', [resId, fieldName]);
          // Mark as trusted HTML so OWL renders it instead of escaping
          this.state.content = result ? markup(result) : markup('<i>No content returned.</i>');
        }
      } catch (error) {
        this.state.content = markup(`<span class='text-danger'>Error: ${error.message || error}</span>`);
      } finally {
        this.state.loading = false;
      }
    }

    // Show Popover
    this.closePopover = this.popover.add(
      target,
      this.constructor.components.PopoverContent,
      { content: this.state.content, loading: this.state.loading },
      {
        position: 'right',
        onClose: () => {
          this.closePopover = null;
        },
      }
    );
  }

  onMouseLeave() {
    // Close immediately on leave to behave like a tooltip
    if (this.closePopover) {
      this.closePopover();
      this.closePopover = null;
    }
  }
}

class PopoverContent extends Component {
  static template = 'dynamic_field_helper.PopoverContent';
}

DynamicHelperIcon.components = { PopoverContent };
DynamicHelperIcon.template = 'dynamic_field_helper.Icon';
