//
// 
// ------------------------------------------------------
// Data Export Chapter javascript functions
// ------------------------------------------------------
//
// 

function export_taskbar_callback(fid) {
    /**
     * Data Export main taskbar.
     *
     * Parameters:
     *  fid - function id
     */
    switch (fid) {
        case 0:
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", 1));
            break;
        case 1:
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", 3));
            break;
        case 2:
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", "0"));
            break;
    }
    window.scroll_to('DCDataExport');
}

function pandas_export_tb_select_callback(id) {
    /**
     * Pandas Export main taskbar.
     *
     * Parameters:
     *  id - import type
     */
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", (2 + "," + id)));
    window.scroll_to('DCDataExport');
}

function pandas_export_tb_return_callback() {
    /**
     * Pandas Export return callback.
     */
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", "0"));
    window.scroll_to('DCDataExport');
}

function pandas_details_export_callback(id) {
    /**
     * Pandas Export display details.
     *
     * Parameters:
     *  id - import type
     */
    var formid = "";
    switch (id) {
        case 0:
            formid = "exportPandasCSV";
            break;
        case 1:
            formid = "exportPandasExcel";
            break;
        case 2:
            formid = "exportPandasJSON";
            break;
        case 3:
            formid = "exportPandasHTML";
            break;
        case 4:
            formid = "exportPandasSQLTable";
            break;
    }
    var importVals = get_input_form_parms(formid);
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "process_export_form", (id + ", " + importVals)));
    window.scroll_to('DCDataExport');
}

function pandas_details_export_clear_callback(id) {
    /**
     * Pandas Export details clear.
     *
     * Parameters:
     *  id - import type
     */
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", "2" + ", " + id));
    window.scroll_to('DCDataExport');
}

function pandas_details_export_return_callback() {
    /**
     * Pandas Export details return.
     */
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", "1"));
    window.scroll_to('DCDataExport');
}

function pandas_details_export_help_callback(id) {
    /**
     * Pandas Export details help.
     *
     * Parameters:
     *  id - import type
     */
    var command = window.getJSPCode(window.EXPORT_LIB, "handle_pandas_details_export_click_help", id);
    var kernel = IPython.notebook.kernel;
    kernel.execute(command);
}

function select_export_db(dblibid) {
    /**
     * select db callbacks.
     *
     * Parameters:
     *  dblibid - database library is
     */

    console.log("select_export_db", dblibid);
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_sql_details_form", "5," + JSON.stringify(dblibid)));
    window.scroll_to('DCDataExport');
}


//
// -------------------------------------
// Custom Export callbacks
// -------------------------------------
//
function custom_export_callback(fid) {
    /**
     * Custom Export callback.
     *
     * Parameters:
     *  fid - function id
     */
    switch (fid) {
        case 0:
            var inputs = new Array();
            var parms = get_input_form_parms("customExport");
            inputs.push(JSON.stringify(parms));
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "process_export_form", "5," + JSON.stringify(inputs)));
            break;
        case 1:
            var customexportcode = $('#customexportcode');
            var custom_code = "# add USER CODE to export the df" + NEW_LINE + NEW_LINE;
            custom_code = (custom_code + "from dfcleanser.common.cfg import get_dfc_dataframe_df" + NEW_LINE);
            custom_code = (custom_code + "df = get_dfc_dataframe_df(dataframe_title)" + NEW_LINE + NEW_LINE);
            custom_code = (custom_code + "# USER CODE" + NEW_LINE);

            customexportcode.val(custom_code);
            break;
        case 2:
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", 0));
            break;
    }
    window.scroll_to('DCDataExport');
}


function pandas_details_export_test_con_callback(dbid, driverid) {
    /**
     * Export db connector test.
     *
     * Parameters:
     *  dbid     - database id
     *  driverid - database driver id
     */

    var sqlinputparms = null;
    switch (dbid) {
        case 0:
            sqlinputparms = window.get_input_form_parms("MySQLdbconnector");
            break;
        case 1:
            sqlinputparms = window.get_input_form_parms("MSSQLServerdbconnector");
            break;
        case 2:
            sqlinputparms = window.get_input_form_parms("SQLitedbconnector");
            break;
        case 3:
            sqlinputparms = window.get_input_form_parms("Postgresqldbconnector");
            break;
        case 4:
            sqlinputparms = window.get_input_form_parms("Oracledbconnector");
            break;
    }
    if (sqlinputparms != null) {
        window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "test_export_sql_db_connector", driverid + ", " + sqlinputparms));
    }
    window.scroll_to('DCDataExport');
}


function pandas_sql_export_callback(dbid) {
    /**
     * Export sql export display callback.
     *
     * Parameters:
     *  dbid     - database id
     */
    var formid = "";
    switch (dbid) {
        case 0:
            formid = "MySQLdbconnector";
            break;
        case 1:
            formid = "MSSQLServerdbconnector";
            break;
        case 2:
            formid = "SQLitedbconnector";
            break;
        case 3:
            formid = "Postgresqldbconnector";
            break;
        case 4:
            formid = "Oracledbconnector";
            break;
        case 5:
            formid = "Customdbconnector";
            break;
    }
    // get the input values
    var connectVals = get_input_form_parms(formid);
    var inputs = new Array();
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_pandas_export_sql_inputs", ("2," + dbid + "," + connectVals + "," + JSON.stringify(inputs))));
    window.scroll_to('DCDataExport');
}

function pandas_export_sql_callback(fid) {
    /**
     * Export sql export process callback.
     *
     * Parameters:
     *  dbid     - database id
     */
    var inputParms = window.get_input_form_parms("exportPandasSQLTable");
    switch (fid) {
        case 0:
        case 1:
            var connectVals = new Array();
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_pandas_export_sql_inputs", (fid + ", -1, " + JSON.stringify(connectVals) + ", " + inputParms)));
            break;
        case 2:
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "export_sql_table", inputParms));
            break;
    }
    window.reset_dependents([false, true, true, true, false, false]);
    window.scroll_to('DCDataExport');
}

//
// -------------------------------------
// Custom Export DHTML callbacks
// -------------------------------------
//
function select_export_table(tablename) {
    var table_name = $("#exportsqltableName");
    table_name.val(tablename);
}

function select_export_column(columnname) {
    var column = $("#exportsqltableindexlabel");
    if (column.val() == "") {
        console.log("empty")
        column.val("[" + columnname + "]");
    } else {
        var slen = column.val().length;
        var newstring = column.val().substr(0, slen - 1) + ", " + columnname + "]";
        column.val(newstring);
    }
}