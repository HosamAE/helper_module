/** @odoo-module **/

import { Component, useState, markup, onWillUnmount, onMounted, useRef } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

function sanitizeDraftData(data) {
    if (!data || typeof data !== "object") {
        return {};
    }
    const safe = {};
    for (const [key, val] of Object.entries(data)) {
        if (val === null || val === undefined) {
            safe[key] = false;
        } else if (typeof val === "string" || typeof val === "number" || typeof val === "boolean") {
            safe[key] = val;
        } else if (Array.isArray(val) && val.length === 2 && typeof val[0] === "number") {
            safe[key] = val[0];
        }
    }
    return safe;
}

export class DynamicHelperIcon extends Component {
    setup() {
        this.orm = useService("orm");
        this.popover = useService("popover");
        this.state = useState({
            content: null,
            loading: false,
            isPinned: false,
        });
        this.closePopover = null;
        this.hideTimeout = null;

        this.onWindowClick = this.onWindowClick.bind(this);
        window.addEventListener("click", this.onWindowClick, true);

        onWillUnmount(() => {
            window.removeEventListener("click", this.onWindowClick, true);
            if (this.hideTimeout) {
                clearTimeout(this.hideTimeout);
            }
            if (this.closePopover) {
                this.closePopover();
            }
        });
    }

    get sizeClass() {
        const fieldDef = this.props.record?.fields?.[this.props.fieldName] || {};
        const size = fieldDef.helper_size || "md";
        return `o_helper_size_${size}`;
    }

    get customStyle() {
        const fieldDef = this.props.record?.fields?.[this.props.fieldName] || {};
        if (fieldDef.helper_width) {
            return `width: ${fieldDef.helper_width}; max-width: ${fieldDef.helper_width};`;
        }
        return "";
    }

    async openHelper(target, pinned = false) {
        if (this.hideTimeout) {
            clearTimeout(this.hideTimeout);
            this.hideTimeout = null;
        }

        if (this.closePopover && pinned) {
            this.state.isPinned = true;
            return;
        }

        if (this.closePopover) {
            return;
        }

        this.state.loading = true;
        this.state.content = null;
        this.state.isPinned = pinned;

        this.closePopover = this.popover.add(
            target,
            this.constructor.components.PopoverContent,
            {
                state: this.state,
                sizeClass: this.sizeClass,
                customStyle: this.customStyle,
                targetEl: target,
                onPopoverMouseEnter: () => this.onPopoverMouseEnter(),
                onPopoverMouseLeave: () => this.onPopoverMouseLeave(),
            },
            {
                position: "right",
                onClose: () => {
                    this.closePopover = null;
                    this.state.isPinned = false;
                },
            }
        );

        try {
            const resId = (typeof this.props.record?.resId === "number") ? this.props.record.resId : false;
            const model = this.props.record?.resModel;
            const fieldName = this.props.fieldName;
            const draftValues = sanitizeDraftData(this.props.record?.data);

            const result = await this.orm.call(model, "get_field_helper", [], {
                record_id: resId,
                field_name: fieldName,
                draft_values: draftValues,
            });

            this.state.content = result ? markup(result) : markup("<i>No content.</i>");
        } catch (error) {
            this.state.content = markup(`<span class="text-danger">Error: ${error.message || error}</span>`);
        } finally {
            this.state.loading = false;
        }
    }

    onMouseEnter(ev) {
        if (this.state.isPinned) {
            return;
        }
        this.openHelper(ev.currentTarget, false);
    }

    onMouseLeave() {
        if (this.state.isPinned) {
            return;
        }
        this.hideTimeout = setTimeout(() => {
            if (!this.state.isPinned && this.closePopover) {
                this.closePopover();
                this.closePopover = null;
            }
        }, 250);
    }

    onPopoverMouseEnter() {
        if (this.hideTimeout) {
            clearTimeout(this.hideTimeout);
            this.hideTimeout = null;
        }
    }

    onPopoverMouseLeave() {
        if (this.state.isPinned) {
            return;
        }
        this.hideTimeout = setTimeout(() => {
            if (!this.state.isPinned && this.closePopover) {
                this.closePopover();
                this.closePopover = null;
            }
        }, 200);
    }

    onClick(ev) {
        ev.stopPropagation();
        if (this.closePopover && this.state.isPinned) {
            this.closePopover();
            this.closePopover = null;
            this.state.isPinned = false;
        } else {
            this.openHelper(ev.currentTarget, true);
        }
    }

    onWindowClick(ev) {
        if (this.closePopover) {
            const popoverEl = document.querySelector(".o_dynamic_helper_popover");
            const isClickInside = popoverEl && popoverEl.contains(ev.target);
            if (!isClickInside) {
                this.closePopover();
                this.closePopover = null;
                this.state.isPinned = false;
            }
        }
    }
}

class PopoverContent extends Component {
    static template = "dynamic_field_helper.PopoverContent";
    static props = ["state", "sizeClass?", "customStyle?", "targetEl?", "onPopoverMouseEnter?", "onPopoverMouseLeave?", "close?"];

    setup() {
        this.rootRef = useRef("popoverRoot");
        onMounted(() => {
            this.adjustPlacement();
        });
    }

    adjustPlacement() {
        if (!this.rootRef.el || !this.props.targetEl) return;
        const popoverRect = this.rootRef.el.getBoundingClientRect();
        const targetRect = this.props.targetEl.getBoundingClientRect();
        if (popoverRect.right <= targetRect.left + 5) {
            this.rootRef.el.classList.add("o_placement_left");
        } else {
            this.rootRef.el.classList.remove("o_placement_left");
        }
    }
}

DynamicHelperIcon.components = { PopoverContent };
DynamicHelperIcon.template = "dynamic_field_helper.Icon";
