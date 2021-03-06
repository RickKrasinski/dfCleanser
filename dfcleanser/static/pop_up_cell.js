define([
    'require',
    'jquery',
    'base/js/namespace',
    'base/js/events',
    'base/js/utils',
    'notebook/js/codecell',
    'notebook/js/outputarea',
], function(
    requirejs,
    $,
    Jupyter,
    events,
    utils,
    codecell,
    outputarea
) {
    "use strict";

    var CodeCell = codecell.CodeCell;

    var PopUp = null;

    var PopUpCodeCell = function(nb) {
        var popupcodecell = this;
        this.notebook = nb;
        this.kernel = nb.kernel;
        this.km = nb.keyboard_manager;
        this.collapsed = true;

        // setup the reset and minimize cell buttons
        this.element = $("<div id='dfcleanser-PopUpCodeCell'>");

        this.close_button = $("<i>").addClass("fa fa-caret-square-o-down PopUpCodeCell-btn PopUpCodeCell-close");
        this.reset_button = $("<i>").addClass("fa fa-refresh PopUpCodeCellReset-btn PopUpCodeCell-reset");
        this.run_button = $("<i>").addClass("fa fa-arrow-circle-right PopUpCodeCellRun-btn PopUpCodeCell-run");
        this.clear_button = $("<i>").addClass("fa fa-minus-circle PopUpCodeCellClear-btn PopUpCodeCell-clear");

        this.element.append(this.close_button);
        this.element.append(this.reset_button);
        this.element.append(this.run_button);
        this.element.append(this.clear_button);

        this.close_button.click(function() {
            popupcodecell.collapse();
        });
        this.reset_button.click(function() {
            reset_pop_up();
        });
        this.run_button.click(function() {
            popupcodecell.run_popup();
        });
        this.clear_button.click(function() {
            popupcodecell.clear_popup();
        });

        // create the pop up working cell
        var cell = this.cell = new CodeCell(nb.kernel, {
            events: nb.events,
            config: nb.config,
            keyboard_manager: nb.keyboard_manager,
            notebook: nb,
            tooltip: nb.tooltip,
        });

        // add the dfcleanser cellid metadata
        var dfcellDict = { "dfc_cellid": "dfcPopUpCell" };
        var dfcleanserDict = { "dfcleanser_metadata": dfcellDict };
        var newcellDict = { "trusted": true, "scrolled": false, "dfcleanser_metadata": dfcellDict };
        cell.metadata = newcellDict;

        // do cell housekeeping
        cell.set_input_prompt();
        this.element.append($("<div/>").addClass('cell-wrapper').append(this.cell.element));
        cell.render();
        cell.refresh();
        this.collapse();

        /*
        // override ctrl/shift-enter to execute me if I'm focused instead of the notebook's cell
        var execute_and_select_action = this.km.actions.register({
            handler: $.proxy(this.execute_and_select_event, this),
        }, 'popupcodecell-execute-and-select');
        var execute_action = this.km.actions.register({
            handler: $.proxy(this.execute_event, this),
        }, 'popupcodecell-execute');
        var toggle_action = this.km.actions.register({
            handler: $.proxy(this.toggle, this),
        }, 'popupcodecell-toggle');

        var shortcuts = {
            'shift-enter': execute_and_select_action,
            'ctrl-enter': execute_action,
            'ctrl-b': toggle_action,
        }
        this.km.edit_shortcuts.add_shortcuts(shortcuts);
        this.km.command_shortcuts.add_shortcuts(shortcuts);
        */

        // add me to the notebook
        $("body").append(this.element);
    };

    PopUpCodeCell.prototype.run_code_in_popup = function(code) {
        this.cell.set_text(code);
        this.cell.execute();
    }

    PopUpCodeCell.prototype.clear_popup = function() {
        this.cell.set_text("");
        this.cell.execute();
    }

    PopUpCodeCell.prototype.run_popup = function() {
        this.cell.execute();
    }


    PopUpCodeCell.prototype.toggle = function() {
        if (this.collapsed) {
            this.expand();
        } else {
            this.collapse();
        }
        return false;
    };

    PopUpCodeCell.prototype.expand = function() {
        this.collapsed = false;
        var site_height = $("#site").height();
        this.element.animate({
            height: site_height,
        }, 200);
        this.reset_button.show();
        this.close_button.show();
        this.clear_button.show();
        this.run_button.show();
        this.cell.element.show();
        this.cell.focus_editor();
        $("#notebook-container").css('margin-left', 0);
    };

    PopUpCodeCell.prototype.collapse = function() {
        this.collapsed = true;
        $("#notebook-container").css('margin-left', 'auto');
        this.element.animate({
            height: 0,
            width: 640,
            top: 20,
        }, 100);
        this.close_button.hide();
        this.reset_button.hide();
        this.clear_button.hide();
        this.run_button.hide();

        this.cell.element.hide();
    };

    /*
    PopUpCodeCell.prototype.execute_and_select_event = function(evt) {
        if (utils.is_focused(this.element)) {
            this.cell.execute();
        } else {
            this.notebook.execute_cell_and_select_below();
        }
    };

    PopUpCodeCell.prototype.execute_event = function(evt) {
        if (utils.is_focused(this.element)) {
            this.cell.execute();
        } else {
            this.notebook.execute_selected_cells();
        }
    };
    */

    //
    // ---------------------------------------------------
    // PopUpCodeCell helper functions
    // ---------------------------------------------------
    //

    window.setup_popupcodecell = function() {
        if (debug_flag)
            console.log(log_prefix + "[Load]\n" + "     dfcleanser popupcodecell created");
        PopUp = new PopUpCodeCell(Jupyter.notebook);
    }

    window.get_popupcodecell = function() {
        return (PopUp.cell);
    }

    window.delete_popupcodecell = function() {
        if (debug_flag)
            console.log(log_prefix + "\n" + "     delete_popupcodecell");
        PopUp = null;
    }

    window.is_pop_up_visible = function() {
        if (PopUp.collapsed)
            return (false);
        else
            return (true);
    }

    window.toggle_popupcodecell = function() {
        if (debug_flag)
            console.log(log_prefix + "\n" + "     toggle_popupcodecell");
        PopUp.toggle();
    }

    window.run_code_in_popupcodecell = function(code) {
        if (debug_flag)
            console.log(log_prefix + "\n" + "     run_code_in_popupcodecell", code);

        if (PopUp.collapsed == false)
            PopUp.run_code_in_popup(code);
        else {
            PopUp.expand();
            PopUp.run_code_in_popup(code);
        }
    }

    window.reset_pop_up = function() {
        process_pop_up_cmd(6);
    }

    window.cleart_pop_up = function() {
        process_pop_up_cmd(6);
    }

    window.shut_off_autoscroll = function() {
        if (debug_flag)
            console.log(log_prefix + "\n" + "     shut_off_autoscroll");

        outputarea.OutputArea.auto_scroll_threshold = -1;
    }


});