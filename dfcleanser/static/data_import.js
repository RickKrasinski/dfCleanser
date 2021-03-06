//
// 
// ------------------------------------------------------
// Data Import javascript functions
// ------------------------------------------------------
//
// 

function import_taskbar_callback(fid) {
    /**
     * Data Import main taskbar callback.
     *
     * Parameters:
     *  fid - function id
     */
    switch (fid) {
        case 0:
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", 1));
            break;
        case 1:
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", 3));
            break;
        case 2:
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", 0));
            break;

    }
    window.scroll_to('DCDataImport');
}

function pandas_import_tb_select_callback(id) {
    /**
     * Pandas Import taskbar callbacks.
     *
     * Parameters:
     *  id - import type
     */
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", 2 + "," + id));
    window.scroll_to('DCDataImport');
}

function pandas_import_tb_return_callback() {
    /**
     * Pandas Import taskbar return.
     */
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", 0));
    window.scroll_to('DCDataImport');
}

function pandas_details_import_callback(id) {
    /**
     * Pandas Details Import taskbar callback.
     *
     * Parameters:
     *  id - import type
     */

    if (window.debug_detail_flag)
        console.log(log_prefix + "\n" + "     pandas_details_import_callback : " + id.toString());

    var formid = "";
    switch (id) {
        case 0:
            formid = "importPandasCSV";
            break;
        case 1:
            formid = "importPandasFWF";
            break;
        case 2:
            formid = "importPandasExcel";
            break;
        case 3:
            formid = "importPandasJSON";
            break;
        case 4:
            formid = "importPandasHTML";
            break;
        case 31:
            formid = "importPandasHTMLdf";
            break;
    }

    // get the input values
    var importVals = get_input_form_parms(formid);
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "process_import_form", id + ", " + importVals));

    if (get_dfc_mode() == 1)
        reset_dependents([false, true, true, true, true, true]);

    window.scroll_to('DCDataImport');
}

function pandas_details_clear_callback(id) {
    /**
     * Pandas Details Import clear inputs callback.
     *
     * Parameters:
     *  id - import type
     */
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", "2" + ", " + id));
    window.scroll_to('DCDataImport');
}

function pandas_details_return_callback(ownerid) {
    /**
     * Pandas Details Import return callback.
     */
    if (ownerid == 0) {
        window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", "1"));
        window.scroll_to('DCDataImport');
    } else {
        window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", "1"));
        window.scroll_to('DCDataExport');
    }
}

function pandas_sql_import_callback(itype, dbid) {
    /**
     * Pandas sql Import callbacks.
     *
     * Parameters:
     *  itype - import type
     *  dbid  - database id
     */

    if (window.debug_detail_flag)
        console.log(log_prefix + "\n" + "     pandas_sql_import_callback : " + itype.toString() + " : " + dbid.toString());

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
    var importVals = get_input_form_parms(formid);
    if (itype == 0) { window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_pandas_import_sql_inputs", "5,0" + "," + dbid + "," + importVals)); } else { window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_pandas_import_sql_inputs", "6,0" + "," + dbid + "," + importVals)); }
    window.scroll_to('DCDataImport');
}

function custom_import_callback(fid) {
    /**
     * Custom Import callbacks.
     *
     * Parameters:
     *  fid  - function id
     */

    switch (fid) {
        case 8:
        case 9:
            var inputs = new Array();
            inputs.push(fid)

            var parms = get_input_form_parms("customImport");
            inputs.push(JSON.stringify(parms));

            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "process_import_form", "7," + JSON.stringify(inputs)));
            break;
        case 10:
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", 0));
            break;
    }
    window.scroll_to('DCDataImport');
}

function pandas_details_test_con_callback(sqlid, dbid, driverid) {
    /**
     * test db connection callbacks.
     *
     * Parameters:
     *  sqlid    - table or query
     *  dbid     - database id
     *  driverid - database driver id
     */

    if (window.debug_detail_flag)
        console.log(log_prefix + "\n" + "     pandas_details_test_con_callback : " + sqlid.toString() + " : " + dbid.toString() + driverid.toString());

    var sqlinputparms = null;
    var sqlform = 0

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
        case 5:
            sqlinputparms = window.get_input_form_parms("customdbconnector");
            break;
    }

    if (sqlid == 0) {
        sqlform = 5;
    } else {
        sqlform = 6;
    }

    if (sqlinputparms != null) {
        window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "test_import_sql_db_connector", sqlform + ", " + driverid + ", " + sqlinputparms));
    }
}

function pandas_details_get_index_columns_callback(sqltype) {
    /**
     * get db columns callback.
     */

    if (window.debug_detail_flag)
        console.log(log_prefix + "\n" + "     pandas_details_get_index_columns_callback : " + sqltype);

    var sqlinputparms = [];

    if (sqltype == "table")
        sqlinputparms = window.get_input_form_parms("importPandasSQLCommonTable");
    else
        sqlinputparms = window.get_input_form_parms("importPandasSQLQuery");

    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "get_index_columns", sqlinputparms));

    window.scroll_to('DCDataImport');
}

function pandas_details_get_columns_callback(sqltype) {
    /**
     * get db columns callback.
     */

    if (window.debug_detail_flag)
        console.log(log_prefix + "\n" + "     pandas_details_get_columns_callback : " + sqltype);

    var sqlinputparms = [];

    if (sqltype == "table")
        sqlinputparms = window.get_input_form_parms("importPandasSQLCommonTable");
    else
        sqlinputparms = window.get_input_form_parms("importPandasSQLQuery");

    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "get_columns", sqlinputparms));

    window.scroll_to('DCDataImport');
}

function pandas_details_get_strftime_callback(sqltype) {
    /**
     * get format time list callback.
     */

    if (window.debug_detail_flag)
        console.log(log_prefix + "\n" + "     pandas_details_get_strftime_callback : " + sqltype);

    var sqlinputparms = [];

    if (sqltype == "table")
        sqlinputparms = window.get_input_form_parms("importPandasSQLCommonTable");
    else
        sqlinputparms = window.get_input_form_parms("importPandasSQLQuery");

    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "get_datetimeformats", sqlinputparms));


    window.scroll_to('DCDataImport');

}

function select_db(dblibid) {
    /**
     * select db callback.
     *
     * Parameters:
     *  dblibid - database library is
     */

    if (window.debug_flag)
        console.log("select_db", dblibid);

    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_sql_details_form", JSON.stringify(dblibid)));
    window.scroll_to('DCDataImport');
}

function select_custom() {
    /**
     * select custom callback.
     */
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_sql_details_form", "5," + JSON.stringify("custom")));
    window.scroll_to('DCDataImport');
}

function select_table(tablename) {
    /**
     * select table DHTML callback.
     *
     * Parameters:
     *  tablename - table name
     */
    var table_name = $("#sqltablecommontableName");

    var inputs = [
        ["sqltablecommontableName"],
        [table_name.val()]
    ]
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "get_columns", JSON.stringify(inputs)));
    window.scroll_to('DCDataImport');
}

function select_column(columnname) {
    /**
     * select column callback.
     *
     * Parameters:
     *  columnname - column name
     */

    if (window.debug_detail_flag)
        console.log(log_prefix + "\n" + "     select_column : " + columnname);

    var column = $("#sqltablecommoncolumns");
    if (column.val() == "") {
        column.val("[" + columnname + "]");
    } else {
        var slen = column.val().length;
        var newstring = column.val().substr(0, slen - 1) + ", " + columnname + "]";
        column.val(newstring);
    }
}

function select_index_column(columnname) {
    /**
     * select column callback.
     *
     * Parameters:
     *  columnname - column name
     */

    if (window.debug_detail_flag)
        console.log(log_prefix + "\n" + "     select_index_column : " + columnname);

    var column = $("#sqltableindexcol");
    if (column.val() == "") {
        column.val("[" + columnname + "]");
    } else {
        var slen = column.val().length;
        var newstring = column.val().substr(0, slen - 1) + ", " + columnname + "]";
        column.val(newstring);
    }
}

function select_date_column(columnname) {

    if (window.debug_detail_flag)
        console.log(log_prefix + "\n" + "     select_index_column : " + columnname);

    var column = $("#sqltableparsedates");
    if (column.val() == "") {
        column.val("[" + columnname + "]");
    } else {
        var slen = column.val().length;
        var newstring = column.val().substr(0, slen - 1) + ", " + columnname + "]";
        column.val(newstring);
    }

    var selected_format = $("#sqltablecommondateformats :selected").text();

    var formats = $("#sqltablecommonparsedateformats");
    if (formats.val() == "") {
        formats.val("[" + selected_format + "]");
    } else {
        var slen = formats.val().length;
        var newstring = formats.val().substr(0, slen - 1) + ", " + selected_format + "]";
        formats.val(newstring);
    }


}

function select_dtformat(dtformat) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_dtformat", dtformat);
}

function pandas_import_sql_callback(fid) {
    /**
     * select column callback.
     *
     * Parameters:
     *  fid - function id
     */
    switch (fid) {
        case 0:
            var inputParms = window.get_input_form_parms("importPandasSQLCommonTable");
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "import_sql_table", inputParms));
            break;
        case 5:
            var inputParms = window.get_input_form_parms("importPandasSQLCustomTable");
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "import_sql_table", inputParms));
            break;
        default:
            var inputParms = window.get_input_form_parms("importPandasSQLQuery");
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "import_sql_query", inputParms));
            break;
    }
    window.reset_dependents([false, true, true, true, true, false]);
    window.scroll_to('DCDataImport');
}

function display_selected_html_df(dfid) {
    /**
     * select a df to display callback.
     *
     * Parameters:
     *  dfid - dataframe id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "display_selected_html_df", dfid);

    var inputs = new Array();
    inputs.push(dfid)

    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "process_import_form", "30," + JSON.stringify(inputs)));
    window.scroll_to('DCDataImport');

    return;
}