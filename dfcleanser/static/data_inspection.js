//
// 
// ------------------------------------------------------
// Data Inspection Chapter javascript functions
// ------------------------------------------------------
//
//  

function inspection_task_bar_callback(fid) {
    /**
     * Data inspection taskbar callback.
     *
     * Parameters:
     *  fid - function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "inspection_task_bar_callback", fid);

    var inputs = new Array();

    switch (fid) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            var inputParms = window.get_input_form_parms("datainspectdf");
            inputs.push(inputParms);
            window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", fid + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataInspection');
            break;
        case 9:
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "open_as_excel", "0"));
            break;
        case 12:
        case 13:
            var inputs = new Array();
            var selected_value = $("#inspectcolname :selected").text();
            inputs.push(selected_value);
            window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", fid + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataInspection');
            break;
        case 14:
            var inputs = new Array();
            var selected_value = $("#inspectcolname :selected").text();
            inputs.push(selected_value);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "12" + ", " + JSON.stringify(inputs)));
            window.scroll_to('DCDataCleansing');
            break;
        case 15:
            var inputs = new Array();
            inputs.push("DataInspection");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", "21" + ", " + JSON.stringify(inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 16:
            window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", fid));
            window.scroll_to('DCDataInspection');
            break;
        case 17:
            var inputParms = window.get_input_form_parms("scrolldfrowsinput");
            inputs.push(inputParms);
            window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", fid + "," + inputs));
            window.scroll_to('DCDataInspection');
            break;
        case 18:
        case 19:
            window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", fid));
            window.scroll_to('DCDataInspection');
            break;
    }
}

function display_remote_df_rows(chapterid) {
    /**
     * Data inspection taskbar callback.
     *
     * Parameters:
     *  fid - function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "display_remote_df_rows", chapterid);

    var inputs = new Array();
    inputs.push(chapterid)

    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", 21 + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataInspection');

}


function get_df_row(rowid) {
    /**
     * Data Inspection dsiplay specific row.
     *
     * Parameters:
     *  rowid
     */

    var inputs = new Array();
    inputs.push(rowid);
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.window.CLEANSING_LIB, "display_data_cleansing", 56 + "," + rowid.toString()));
    window.scroll_to('DCDataCleansing');
}


function get_columns_name_list() {
    /**
     * Data Inspection get a dsiplay of all column names.
     *
     * Parameters:
     *  NA
     */

    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "10"));
    window.scroll_to('DCDataInspection');
}

function change_inspect_cols_col(id) {

    if (window.debug_detail_flag)
        console.log("change_inspect_cols_col", id);

    var inputs = new Array();
    var inputParms = window.get_input_form_parms("datainspectdf");
    inputs.push(inputParms);
    var selected_value = $("#inspectcolname :selected").text();
    inputs.push(selected_value);
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", 4 + "," + JSON.stringify(inputs)));
}

function srow(rowid) {
    /**
     * Data Inspection select a row to display.
     *
     * Parameters:
     *  rowid - row id
     */

    var goodrowid = true;
    try {
        if (rowid.length > 0) {
            goodrowid = false;
            var nrow = parseInt(rowid);
            if (nrow === parseInt(nrow, 10))
                goodrowid = true;
        }
    } catch (e) {}
    if (goodrowid) {
        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "8" + "," + JSON.stringify(rowid)));
        window.scroll_to('DCDataCleansing');
    }
}

function display_objects_callback(id) {
    /* Data Inspection deprecated.
     * @param:
     *  rowid - row id
     */

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "16," + id));
    window.scroll_to('DCDataCleansing');
}

function ucol(colid) {
    /**
     * Data Inspection display unique columns values.
     *
     * Parameters:
     *  colid - column id
     */

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "1" + "," + JSON.stringify(colid)));
    window.scroll_to('DCDataCleansing');
}

function ncol(colid) {
    /**
     * Data Inspection display numeric columns.
     *
     * Parameters:
     *  colid - column id
     */

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "12" + "," + JSON.stringify(colid)));
    window.scroll_to('DCDataCleansing');
}

function scatcol(colid) {
    /**
     * Data Inspection display cat columns.
     *
     * Parameters:
     *  colid - column id
     */

    var ids = new Array("catcolumnname", "catcolumnnameordered", "catcolumncompleteuniques");
    ids = ids.toString();
    var vals = new Array(colid, "False", "True");

    var parms = "[[" + '"catcolumnname",' + '"catcolumnnameordered",' + '"catcolumncompleteuniques"],';
    parms = parms + '["' + colid + '",' + '"False",' + '"True"]]';

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "265" + "," + parms));
    window.scroll_to('DCDataTransform');
}


function change_colsearch_cols(selectid) {
    /**
     * Data Inspection dynamic html for subset df rows
     *
     * Parameters:
     *  selectid - column select id
     */
    var selected_cols = getSelectValues(selectid);
    var labels = ["colsearchvalues0", "colsearchvalues1", "colsearchvalues2"];

    if ((selected_cols.length == 1) && (selected_cols[0] == "None")) {

        for (i = 0; i < 3; i++) {
            $("label[for='" + labels[i] + "']").text("column_values");
            $("#" + labels[i]).val("")
            $("#" + labels[i]).attr("readonly", true);

        }
    } else {

        var col_labels = new Array();
        var col_values = new Array();

        for (i = 0; i < 3; i++) {
            col_labels.push($("label[for='" + labels[i] + "']").text());
            col_values.push($("#" + labels[i]).val());
        }

        for (i = 0; i < 3; i++) {

            if (i < selected_cols.length) {

                var newlabel = "'";
                newlabel = newlabel + selected_cols[i];
                newlabel = newlabel + "' values_list";

                $("label[for='" + labels[i] + "']").text(newlabel);

                var found = -1;

                for (var j = 0; j < 3; j++) {
                    if (col_labels[j].indexOf(selected_cols[i]) > -1) {
                        found = j;
                    }
                }

                if (found > -1)
                    $("#" + labels[i]).val(col_values[found])
                else
                    $("#" + labels[i]).val("")

                $("#" + labels[i]).removeAttr("readonly");

            } else {

                $("label[for='" + labels[i] + "']").text("column_values");
                $("#" + labels[i]).val("")
                $("#" + labels[i]).attr("readonly", true);
            }
        }
    }
}


function getSelectValues(selectid) {
    var results = new Array();

    $('#' + selectid + ' option:selected').each(function() {
        results.push($(this).val());
    });

    return results;
}


function dc_drop_rows_callback(valtype) {
    /**
     * Data Inspection drop nan rows.
     *
     * Parameters:
     *  valtype - threshold type
     */

    var parms = new Array();
    parms.push(valtype);
    var inputs = window.get_input_form_parms("droprowsinput");
    parms.push(inputs);
    window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "6" + ", " + JSON.stringify(parms)));
    window.scroll_to('DCDataInspection');
}

function dc_drop_cols_callback(valtype) {
    /**
     * Data Inspection drop nan cols.
     *
     * Parameters:
     *  valtype - threshold type
     */

    var parms = new Array();
    parms.push(valtype);
    var inputs = window.get_input_form_parms("dropcolsinput");
    parms.push(inputs);
    window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "7" + ", " + JSON.stringify(parms)));
    window.scroll_to('DCDataInspection');
}

function change_dataframes_to_select() {
    /**
     * Update datframe select input forms.
     *
     * Parameters:
     *  optionsDict - select options dict
     *  selected    - option selected
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "change_dataframes_to_select");

    var df_forms = ["dfmgrtitle", "didfdataframe", "dcdfdataframe", "dtdfdataframe", "dedfdataframe", "dsdfdataframe"]
    var displayed_forms = new Array();

    var inspectdfs = window.get_input_form_parms("datainspectdfinput");
    var cleansingdfs = window.get_input_form_parms("datacleansedfinput");
    var transformdfs = window.get_input_form_parms("datatransformdfinput");
    var exportdfs = window.get_input_form_parms("dataexportdfinput");
    var geocodedfs = window.get_input_form_parms("datageocodedfinput");
    var subsetdfs = window.get_input_form_parms("datasubsetdfinput");

    if (inspectdfs.length > 0) displayed_forms.push("didfdataframe");
    if (cleansingdfs.length > 0) displayed_forms.push("dcdfdataframe");
    if (transformdfs.length > 0) displayed_forms.push("dtdfdataframe");
    if (exportdfs.length > 0) displayed_forms.push("dedfdataframe");
    if (geocodedfs.length > 0) displayed_forms.push("dgdfdataframe");
    if (subsetdfs.length > 0) displayed_forms.push("dsdfdataframe");

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "change_df_select", JSON.stringify(displayed_forms)));

}