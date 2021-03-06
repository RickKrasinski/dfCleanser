"""
# cfg 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import json 
import os



"""
#--------------------------------------------------------------------------
#   local helper functions
#--------------------------------------------------------------------------
"""
def display_javascript_HTML(html) :
    from IPython.core.display import display 
    display(html)#, metadata=dict(isolated=True))


def run_javascript(jscript, errmsg) :

    try :            
        from IPython.core.magics.display import Javascript
        display_javascript_HTML(Javascript(jscript))
    except :
        print(errmsg,jscript)
        
def does_dir_exist(path) :
    if(os.path.exists(path)) :
        if(os.path.isdir(path)) :   
            return(True)
        else :
            return(False)
    
def make_dir(path) :
    try :
        os.mkdir(path)
        return()
    
    except FileExistsError:
        return()

def does_file_exist(path) :
    if(os.path.exists(path)) :
        if(os.path.isfile(path)) :   
            return(True)
        else :
            return(False)
"""
#--------------------------------------------------------------------------
#   dfcleanser common notebook file and path functions
#--------------------------------------------------------------------------
"""
    
def get_common_files_path() :
    common_files_path = os.path.join(get_dfcleanser_location(),"files")
    return(common_files_path + "\\")   

def get_notebook_files_path() :
    notebook_files_path = os.path.join(get_dfcleanser_location(),"files","notebooks")
    return(notebook_files_path + "\\")   

def get_dfcleanser_location()  :

    import os
    import dfcleanser
    ppath = os.path.abspath(dfcleanser.__file__)
    #print("dfc path",dcfpath)   

    initpyloc = ppath.find("__init__.py")
    if(initpyloc > 0) :
        ppath = ppath[:initpyloc]

    return(ppath)

"""    
#--------------------------------------------------------------------------
#   dfcleanser sync jupyter with js 
#--------------------------------------------------------------------------
"""
def sync_with_js(parms) :
    DataframeCleansercfg.sync_js(parms)    

def get_notebookname() :
    try :
        run_javascript("window.getNotebookName();","Unable to get notebook name")
    except :
        print("getNotebookName error")
        
def get_notebookpath() :
    try :
        run_javascript("window.getNotebookPath();","Unable to get notebook path")
    except :
        print("getNotebookPath error")
    


        
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser dataframe objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   dfcleanser chapter ids
#--------------------------------------------------------------------------
"""
DataCleansing_ID        =   "DataCleansing"
DataExport_ID           =   "DataExport"
DataImport_ID           =   "DataImport"
DataInspection_ID       =   "DataInspection"
DataScripting_ID        =   "DataScripting"
DataTransform_ID        =   "DataTransform"
SWUtilities_ID          =   "SWUtilities"
SWDFSubsetUtility_ID    =   "SWDFSubsetUtility"
SWGeocodeUtility_ID     =   "SWGeocodeUtility"
SWZipcodeUtility_ID     =   "SWZipcodeUtility"
SWCensusUtility_ID      =   "SWCensusUtility"
System_ID               =   "System"


DBUtils_ID              =   "DBUtils"
DumpUtils_ID            =   "DumpUtils"
Help_ID                 =   "Help"
GenFunction_ID          =   "GenFunction"


"""
#--------------------------------------------------------------------------
#    chapter current dataframe objects   
#--------------------------------------------------------------------------
"""
chapter_select_df_input_title             =   "Dataframe To Inspect"
chapter_select_df_input_id                =   "datainspectdf"
chapter_select_df_input_idList            =   ["didfdataframe"]

chapter_select_df_input_labelList         =   ["dataframe_to_inspect"]

chapter_select_df_input_typeList          =   ["select"]

chapter_select_df_input_placeholderList   =   ["dataframe to inspect"]

chapter_select_df_input_jsList            =   [None]

chapter_select_df_input_reqList           =   [0]

chapter_select_df_input_form              =   [chapter_select_df_input_id,
                                               chapter_select_df_input_idList,
                                               chapter_select_df_input_labelList,
                                               chapter_select_df_input_typeList,
                                               chapter_select_df_input_placeholderList,
                                               chapter_select_df_input_jsList,
                                               chapter_select_df_input_reqList]  



data_cleansing_df_input_id                =   "datacleansedf"
data_transform_df_input_id                =   "datatransformdf"
data_export_df_input_id                   =   "dataexportdf"
data_subset_df_input_id                   =   "datasubsetdf"



def update_chapter_df_select(chapterselect) :
    """
    * ---------------------------------------------------------
    * function : change the df list in select forms
    * 
    * Parms :
    *  chapterform - chapter fomr to update
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    if(chapterselect == "didfdataframe") :
        select_df_form  =   get_select_df_form(DataInspection_ID) 
        cfg_key         =   CURRENT_INSPECTION_DF
    elif(chapterselect == "dcdfdataframe") :
        select_df_form  =   get_select_df_form(DataCleansing_ID) 
        cfg_key         =   CURRENT_CLEANSE_DF
    elif(chapterselect == "dtdfdataframe") :
        select_df_form  =   get_select_df_form(DataTransform_ID) 
        cfg_key         =   CURRENT_TRANSFORM_DF
    elif(chapterselect == "dedfdataframe") :
        select_df_form  =   get_select_df_form(DataExport_ID) 
        cfg_key         =   CURRENT_EXPORT_DF
    elif(chapterselect == "dgdfdataframe") :
        select_df_form  =   get_select_df_form(SWGeocodeUtility_ID) 
        cfg_key         =   CURRENT_GEOCODE_DF
    elif(chapterselect == "dsdfdataframe") :
        select_df_form  =   get_select_df_form(SWDFSubsetUtility_ID) 
        cfg_key         =   CURRENT_SUBSET_DF
    else :
        return()
    
    if(is_a_dfc_dataframe_loaded()) :
        df_titles       =   get_dfc_dataframes_titles_list()
        selected_df     =   df_titles[0]
    
        if(get_config_value(cfg_key) is None)     :   
            set_config_value(cfg_key,selected_df)
        else :
            selected_df    =   get_config_value(cfg_key)
    
    else :
        selected_df     =   ""
        drop_config_value(cfg_key)            
    
    from dfcleanser.common.common_utils import patch_html, run_jscript
        
    new_df_html         =   select_df_form.get_html()
    new_df_html         =   patch_html(new_df_html)

    change_select_js = "$("
    change_select_js = change_select_js + "'#" + chapterselect + "').html('"
    change_select_js = change_select_js + new_df_html + "');"
    run_jscript(change_select_js,"fail update select : ")
    
    set_select_js = "$("
    set_select_js = set_select_js + "'#" + chapterselect + " :selected').text('" + selected_df + "');"
    run_jscript(set_select_js,"fail update select : ")

    
    set_select_js = "$("
    set_select_js = set_select_js + "'#" + chapterselect + "').trigger('change');"
    run_jscript(set_select_js,"fail update select : ")
    

def get_select_df_form(chapterid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get select dataframe form
    * 
    * parms :
    *  chapterid    -   chapter id
    *
    * returns : form
    * --------------------------------------------------------
    """

    if(chapterid == DataCleansing_ID) :
        idlist      =   ["dcdfdataframe"]
        labellist   =   ["dataframe_to_cleanse"]
        formid      =   "datacleansedf"

    elif(chapterid == DataTransform_ID) :
        idlist      =   ["dtdfdataframe"]
        labellist   =   ["dataframe_to_transform"]
        formid      =   "datatransformdf"

    elif(chapterid == DataExport_ID) :
        idlist      =   ["dedfdataframe"]
        labellist   =   ["dataframe_to_export"]
        formid      =   "dataexportdf"
    
    elif(chapterid == SWGeocodeUtility_ID) :
        idlist      =   ["dgdfdataframe"]
        labellist   =   ["dataframe_to_geocode"]
        formid      =   "datageocodedf"
    
    elif(chapterid == SWDFSubsetUtility_ID) :
        idlist      =   ["dsdfdataframe"]
        labellist   =   ["dataframe_to_subset"]
        formid      =   "datasubsetdf"

    else :
        idlist      =   chapter_select_df_input_idList
        labellist   =   chapter_select_df_input_labelList
        formid      =   chapter_select_df_input_id
    
    from dfcleanser.common.html_widgets import InputForm
    select_df_form  =   InputForm(formid,
                                  idlist,
                                  labellist,
                                  chapter_select_df_input_typeList,
                                  chapter_select_df_input_placeholderList,
                                  chapter_select_df_input_jsList,
                                  chapter_select_df_input_reqList)
    
    df_list     =   get_dfc_dataframes_select_list(chapterid)

    if(not (df_list is None)) :
        dataframes      =   df_list
    else :
        dataframes      =   {'default': "no dfs defined", 'list': ["no dfs defined"], "callback" : "select_chapter_df"}

    selectDicts     =   []
    selectDicts.append(dataframes)

    from dfcleanser.common.common_utils import get_select_defaults
    get_select_defaults(select_df_form,
                        formid,
                        idlist,
                        chapter_select_df_input_typeList,
                        selectDicts)
    
    select_df_form.set_shortForm(True)
    
    if(get_dfc_mode() == INLINE_MODE) :
        select_df_form.set_gridwidth(780)
    else :
        select_df_form.set_gridwidth(480)
        
    return(select_df_form)


def display_data_select_df(chapterid) :
    """
    * -------------------------------------------------------------------------- 
    * function : display select dataframe form
    * 
    * parms :
    *  chapterid    -   chapter id
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    select_df_form              =   get_select_df_form(chapterid)
    select_df_form_html         =   select_df_form.get_html()
    
    gridclasses     =   ["dfc-footer"]
    gridhtmls       =   [select_df_form_html]
    
    from dfcleanser.common.common_utils import display_generic_grid   
    if(get_dfc_mode() == INLINE_MODE) :
        display_generic_grid("df-select-df-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-select-df-pop-up-wrapper",gridclasses,gridhtmls)


def display_no_dfs(chapterid) :
    """
    * -------------------------------------------------------------------------- 
    * function : display status fro no dfs
    * 
    * parms :
    *  chapterid    -   chapter id
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(chapterid == DataCleansing_ID) :         msg    =   "No dataframe imported to select for data cleansing"
    elif(chapterid == DataInspection_ID) :      msg    =   "No dataframe imported to select for data inspection"
    elif(chapterid == DataExport_ID) :          msg    =   "No dataframe imported to select for data export"
    elif(chapterid == DataTransform_ID) :       msg    =   "No dataframe imported to select for data transform"
    elif(chapterid == SWDFSubsetUtility_ID) :   msg    =   "No dataframe imported to select for subsets"
    elif(chapterid == DataImport_ID)        :   msg    =   "No dataframe imported to select for data import"
    elif(chapterid == SWGeocodeUtility_ID)  :   msg    =   "No dataframe imported to select for geocoding"
    
    from dfcleanser.common.common_utils import display_grid_status
    display_grid_status(msg)
    

def delete_df(df) :
    """
    * -------------------------------------------------------------------------- 
    * function : delete df and memory
    * 
    * parms :
    *  df    -   df to delete
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    del df
    import gc
    gc.collect()


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  dfc dataframe objects and methods
#
#   a dfc dataframe is an object that contains a descriptive, 
#   a pandas dataframe and descriptive notes
#
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   dfcleanser Dataframe helper methods
#--------------------------------------------------------------------------
"""

def is_a_dfc_dataframe_loaded() :
    """
    * ---------------------------------------------------------------------
    * function : chek if a dfc dataframe is loaed in memory for usage
    *
    * returns : 
    *  True if a dfc dataframe loaded else False
    * --------------------------------------------------------------------
    """
    return(dfc_dfs.is_a_dfc_dataframe_loaded()) 

def get_dataframe(title) :
    """
    * ---------------------------------------------------------------------
    * function : get a datframe object
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    return(dfc_dfs.get_dataframe(title))
 
def get_dfc_dataframe(title) :
    """
    * ---------------------------------------------------------------------
    * function : get a dfc datframe object
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    return(dfc_dfs.get_dfc_dataframe(title))
    
def get_dfc_dataframe_df(title) :
    """
    * ---------------------------------------------------------------------
    * function : get a dfc datframe object dataframe attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_df  =  dfc_dfs.get_dfc_dataframe(title)
    if(dfc_df is None) :
        return(None)
    else :
        return(dfc_df.get_df())
    
def set_dfc_dataframe_df(title,df) :
    """
    * ---------------------------------------------------------------------
    * function : set a dfc datframe pandas dataframe attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    
    dfc_df  =  dfc_dfs.get_dfc_dataframe(title)
    if(not(dfc_df) is None) :
        dfc_df.set_df(df)
    

def get_dfc_dataframe_notes(title) :
    """
    * ---------------------------------------------------------------------
    * function : get a dfc datframe note attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    return(dfc_dfs.get_dataframe_notes(title))
    
def set_dfc_dataframe_notes(title,notes) :
    """
    * ---------------------------------------------------------------------
    * function : set a dfc datframe note attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_dfs.set_dataframe_notes(title,notes)

def append_dfc_dataframe_notes(title,notes) :
    """
    * ---------------------------------------------------------------------
    * function : append a note to the dfc dataframe notes
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_notes   =   get_dfc_dataframe_notes(title)
    dfc_notes   =   dfc_notes + "\n--------\n" + notes
    dfc_dfs.set_dataframe_notes(title,notes)

"""
* --------------------------------------
* dfcleanser dataframe object methods
* --------------------------------------
"""  

def get_total_dfc_dataframes() :
    return(dfc_dfs.get_df_count())

     
def rename_dfc_dataframe(oldtitle,newtitle) :
    """
    * ---------------------------------------------------------------------
    * function : rename a dfc datframe title attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_dfs.rename_dataframe(oldtitle,newtitle)

     
def drop_dfc_dataframe(title) :
    """
    * ---------------------------------------------------------------------
    * function : drop a dfc datframe 
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_dfs.drop_dataframe(title)
    
    df_selects_list     =   ["didfdataframe","dcdfdataframe","dtdfdataframe","dedfdataframe","dgdfdataframe","dsdfdataframe"]
    df_selects_cfgs_id  =   [CURRENT_INSPECTION_DF,CURRENT_CLEANSE_DF,CURRENT_TRANSFORM_DF,CURRENT_EXPORT_DF,CURRENT_GEOCODE_DF,CURRENT_SUBSET_DF]  
    
    for i in range(len(df_selects_list)) : 
        
        drop_js     =   '$("#' + df_selects_list[i] + ' option[value=' + "'" + title + "'" + ']").remove();'
        run_javascript(drop_js,"fail update select : ") 
        
        current_df  =   get_config_value(df_selects_cfgs_id[i])
        
        if(current_df == title) :
            
            drop_config_value(df_selects_cfgs_id[i])    

            if(get_total_dfc_dataframes() > 0) :
        
                df_titles   =   get_dfc_dataframes_titles_list()
                change_selected_js = "$('#" + df_titles[0] + "').prop('selectedIndex', 1);" 
                run_javascript(change_selected_js,"fail update select : ")
                
                set_config_value(df_selects_cfgs_id[i],df_titles[0])
                
    

def add_dfc_dataframe(dfcdf,update=True) :
    """
    * ---------------------------------------------------------------------
    * function : add a dfc dataframe object to available list
    * 
    * parms :
    *  dfcdf     - dfc_dataframe object
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------------------
    """
    
    dfc_dfs.add_dataframe(dfcdf)
    
    df_selects_list     =   ["didfdataframe","dcdfdataframe","dtdfdataframe","dedfdataframe","dgdfdataframe","dsdfdataframe"]
    df_selects_cfgs_id  =   [CURRENT_INSPECTION_DF,CURRENT_CLEANSE_DF,CURRENT_TRANSFORM_DF,CURRENT_EXPORT_DF,CURRENT_GEOCODE_DF,CURRENT_SUBSET_DF]  
    
    for i in range(len(df_selects_list)) :
        
        if(get_total_dfc_dataframes() == 1) :
        
            drop_js     =   '$("#' + df_selects_list[i] + ' option[value=' + "'" + 'no dfs defined' + "'" + ']").remove();'
            run_javascript(drop_js,"fail update select : ") 
            set_config_value(df_selects_cfgs_id[i],dfcdf.get_title()) 

        if(get_total_dfc_dataframes() == 1) :
            change_select_js = "$('#" + df_selects_list[i] + "').append('<option style=" + '"' + "text-align:left; font-size:12px;" + '"' + " value=" + '"' + dfcdf.get_title() + '"' + " selected>" + dfcdf.get_title() + "</option>');" 
        
        else :
            change_select_js = "$('#" + df_selects_list[i] + "').append('<option style=" + '"' + "text-align:left; font-size:12px;" + '"' + " value=" + '"' + dfcdf.get_title() + '"' + ">" + dfcdf.get_title() + "</option>');" 
            
        run_javascript(change_select_js,"fail update select : ")


def get_dfc_dataframes_titles_list() :
    """
    * ---------------------------------------------------------
    * class : get a python list of dfc dataframes titles 
    * 
    * returns : 
    *  list of dfc dataframe titles 
    * --------------------------------------------------------
    """
    return(dfc_dfs.get_dataframe_titles())


def get_dfc_dataframes_select_list(chapterid) :
    """
    * ---------------------------------------------------------
    * class : get the list of dfc dataframes for a select 
    * 
    * returns : 
    *  select list of dfc dataframe objects 
    * --------------------------------------------------------
    """
    
    df_select           =   {}
    df_select_titles    =   get_dfc_dataframes_titles_list()

    if(chapterid == DataInspection_ID)      :   default_df  =   get_config_value(CURRENT_INSPECTION_DF)
    elif(chapterid == DataCleansing_ID)     :   default_df  =   get_config_value(CURRENT_CLEANSE_DF)
    elif(chapterid == DataTransform_ID)     :   default_df  =   get_config_value(CURRENT_TRANSFORM_DF)
    elif(chapterid == DataExport_ID)        :   default_df  =   get_config_value(CURRENT_EXPORT_DF)
    elif(chapterid == DataImport_ID)        :   default_df  =   get_config_value(CURRENT_IMPORT_DF)
    elif(chapterid == SWGeocodeUtility_ID)  :   default_df  =   get_config_value(CURRENT_GEOCODE_DF)
    elif(chapterid == SWDFSubsetUtility_ID) :   default_df  =   get_config_value(CURRENT_SUBSET_DF)
    else                                    :   default_df  =   None
   
    if(not (df_select_titles is None) ) :
        if(default_df is None) :
            df_select.update({"default": df_select_titles[0]})
        else :
            df_select.update({"default": default_df})
            
        df_select.update({"list":df_select_titles})
        df_select.update({"callback":"select_chapter_df"})
        return(df_select)
    else :
        return(None)



"""
#--------------------------------------------------------------------------
#   individual dfc dataframe object
#--------------------------------------------------------------------------
"""
class dfc_dataframe :
    """
    * ---------------------------------------------------------
    * class : dfc dataframe object
    * 
    * attributes :
    *  title     - dataframe title 
    *  df        - pandas dataframe object 
    *  notes     - dataframe descriptive notes 
    *
    * returns : 
    *  dataframe cleanser dataframe object 
    * --------------------------------------------------------
    """
    
    dfc_df    =   [None,None,None]
    
    def __init__(self,titleparm,dfparm,notesparm=""):
        self.dfc_df     =   [titleparm,dfparm,notesparm]
        
    def get_title(self)     : return(self.dfc_df[0])       
    def get_df(self)        : return(self.dfc_df[1])       
    def get_notes(self)     : return(self.dfc_df[2])       

    def set_title(self,title)   : self.dfc_df[0] = title       
    def set_df(self,df)         : self.dfc_df[1] = df     
    def set_notes(self,notes)   : self.dfc_df[2] = notes  


CURRENT_INSPECTION_DF                   =   "currentinspectiondf"
CURRENT_CLEANSE_DF                      =   "currentcleansedf"
CURRENT_TRANSFORM_DF                    =   "currenttransformdf"
CURRENT_EXPORT_DF                       =   "currentexportdf"
CURRENT_IMPORT_DF                       =   "currentimportdf"
CURRENT_GEOCODE_DF                      =   "currentgeocodedf"
CURRENT_SUBSET_DF                       =   "currentsubsetdf"
CURRENT_CENSUS_DF                       =   "currentcensusdf"
    

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser config objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   dfc dataframe Chapters current dataframe config value
#--------------------------------------------------------------------------
"""

def get_current_chapter_dfc_df_title(chapterId) :
    
    if(is_a_dfc_dataframe_loaded()) : 
        
        if(chapterId == DataCleansing_ID)           :   dftitle     =   CURRENT_CLEANSE_DF
        elif(chapterId == DataExport_ID)            :   dftitle     =   CURRENT_EXPORT_DF
        elif(chapterId == DataImport_ID)            :   dftitle     =   CURRENT_IMPORT_DF
        elif(chapterId == DataInspection_ID)        :   dftitle     =   CURRENT_INSPECTION_DF
        elif(chapterId == DataTransform_ID)         :   dftitle     =   CURRENT_TRANSFORM_DF
        elif(chapterId == SWDFSubsetUtility_ID)     :   dftitle     =   CURRENT_SUBSET_DF
        elif(chapterId == SWGeocodeUtility_ID)      :   dftitle     =   CURRENT_GEOCODE_DF
        elif(chapterId == SWCensusUtility_ID)       :   dftitle     =   CURRENT_CENSUS_DF
        else                                        :   dftitle     =   None
        
        if(dftitle is None) :
            return(None)
        else :
            
            current_df  =   get_config_value(dftitle)
            return(current_df)
    
    else :
        return(None)


def get_current_chapter_df(chapterId) :
    
    if(is_a_dfc_dataframe_loaded()) : 
        
        if(chapterId == DataCleansing_ID)           :   dftitle     =   CURRENT_CLEANSE_DF
        elif(chapterId == DataExport_ID)            :   dftitle     =   CURRENT_EXPORT_DF
        elif(chapterId == DataImport_ID)            :   dftitle     =   CURRENT_IMPORT_DF
        elif(chapterId == DataInspection_ID)        :   dftitle     =   CURRENT_INSPECTION_DF
        elif(chapterId == DataTransform_ID)         :   dftitle     =   CURRENT_TRANSFORM_DF
        elif(chapterId == SWDFSubsetUtility_ID)     :   dftitle     =   CURRENT_SUBSET_DF
        elif(chapterId == SWGeocodeUtility_ID)      :   dftitle     =   CURRENT_GEOCODE_DF
        elif(chapterId == SWCensusUtility_ID)       :   dftitle     =   CURRENT_CENSUS_DF
        else                                        :   dftitle     =   None
        
        if(dftitle is None) :
            return(None)
        else :
        
            saved_df    =   get_config_value(dftitle)
            df          =   get_dfc_dataframe_df(saved_df)
            
            if(df is None) :
                drop_config_value(saved_df)
                return(None)
            else :
                return(df)
    
    else :
        return(None)

def set_current_chapter_df(chapterId,df,opstat) :
    
    if(is_a_dfc_dataframe_loaded()) : 
        
        if(chapterId == DataCleansing_ID)           :   dftitle     =   CURRENT_CLEANSE_DF
        elif(chapterId == DataExport_ID)            :   dftitle     =   CURRENT_EXPORT_DF
        elif(chapterId == DataImport_ID)            :   dftitle     =   CURRENT_IMPORT_DF
        elif(chapterId == DataInspection_ID)        :   dftitle     =   CURRENT_INSPECTION_DF
        elif(chapterId == DataTransform_ID)         :   dftitle     =   CURRENT_TRANSFORM_DF
        elif(chapterId == SWDFSubsetUtility_ID)     :   dftitle     =   CURRENT_SUBSET_DF
        elif(chapterId == SWGeocodeUtility_ID)      :   dftitle     =   CURRENT_GEOCODE_DF
        elif(chapterId == SWCensusUtility_ID)       :   dftitle     =   CURRENT_CENSUS_DF
        else                                        :   dftitle     =   None
        
        saved_df    =   get_config_value(dftitle)
        
        if(dftitle is None) :
            opstat.set_status(False)
            opstat.set_errorMsg("invalid chapter id")
        
        else :
            
            if(df is None) :
                opstat.set_status(False)
                opstat.set_errorMsg("invalid df")
            
            else :
                saved_df    =   get_config_value(dftitle)
                set_dfc_dataframe_df(saved_df,df)
            


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser config data objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""  

def get_cfg_parm_from_input_list(formid,label,labellist) :
    """
    * ---------------------------------------------------------
    * function : get a parm from cfg parms list
    * 
    * parms :
    *  formid     - form id
    *  label      - label of parm to get
    *  labellist  - input form label list
    *
    * returns : 
    *  geocoder engine 
    * --------------------------------------------------------
    """

    parmslist   =   get_config_value(formid+"Parms")
    
    if(not (parmslist == None)) :
        
        for i in range(len(labellist)) :
            if(label == labellist[i]) :
                return(parmslist[i])
                
    return(None)

     
"""
#--------------------------------------------------------------------------
#   Generic System config value keys
#--------------------------------------------------------------------------
"""
NOTEBOOK_TITLE          =   "NoteBookName"
NOTEBOOK_PATH           =   "NoteBookPath"
DFC_CELLS_LOADED        =   "dfCcellsLoaded"
DFC_CELLS_CBS           =   "dfCcellcbs"

"""
#--------------------------------------------------------------------------
#   DBUtils config value keys
#--------------------------------------------------------------------------
"""
CURRENT_DB_ID_KEY           =   "currentDBID"
CURRENT_DBLIB_ID_KEY        =   "currentDBLIBID"

"""
#--------------------------------------------------------------------------
#   Data Inspection config value keys
#--------------------------------------------------------------------------
"""
CURRENT_SCROLL_ROW_KEY      =   "currentdfScrollRow"

"""
#--------------------------------------------------------------------------
#   Cleansing config value keys
#--------------------------------------------------------------------------
"""
UNIQUES_FLAG_KEY                        =   "columnUniquesDisplay"
UNIQUES_RANGE_KEY                       =   "columnUniquesRange"

DATA_TYPES_FLAG_KEY                     =   "columnDataTypeChange"

CLEANSING_COL_KEY                       =   "datacleansingcolumn"
CLEANSING_ROW_KEY                       =   "datacleansingrow"
CHKNUM_COL_KEY                          =   "ChknumColumn"

"""
#--------------------------------------------------------------------------
#   Export config value keys
#--------------------------------------------------------------------------
"""
CURRENT_EXPORTED_FILE_NAME_KEY          =   "currentExportedFileName"
CURRENT_EXPORT_START_TIME               =   "exportStartTime"

"""
#--------------------------------------------------------------------------
#   Import config value keys
#--------------------------------------------------------------------------
"""
CURRENT_IMPORTED_DATA_SOURCE_KEY        =   "currentImportedDataSource"
CURRENT_SQL_IMPORT_ID_KEY               =   "currentSQLImportID"
CURRENT_IMPORT_START_TIME               =   "importStartTime"

"""
#--------------------------------------------------------------------------
#   Transform config value keys
#--------------------------------------------------------------------------
"""
DATA_TRANSFORM_COL_SELECTED_KEY         =   "DT_ColumnsSelected"
MAP_TRANSFORM_COL_NAME_KEY              =   "DT_MapColumnName"
MOVE_COL_ID_KEY                         =   "MoveColumnId"
MOVE_AFTER_COL_ID_KEY                   =   "MoveAfterColumnId"
ADD_COL_COL_NAME_KEY                    =   "AddColumnColName"
ADD_COL_DATATYPE_ID_KEY                 =   "AddColumnDataType"
ADD_COL_CODE_KEY                        =   "AddColumnCode"
COPY_COL_TO_KEY                         =   "CopyColumnTo"
COPY_COL_FROM_KEY                       =   "CopyColumnFrom"
COMPAT_COL_KEY                          =   "CompatColumn"

"""
#--------------------------------------------------------------------------
#   Scripting config value keys
#--------------------------------------------------------------------------
"""
SCRIPT_LOG_KEY                          =   "ScriptLog"
BACKUP_SCRIPT_LOG_KEY                   =   "BackupScriptLog"
SCRIPTING_FLAG_KEY                      =   "ScriptingFlag"

"""
#--------------------------------------------------------------------------
#   SW Utilities config value keys
#--------------------------------------------------------------------------
"""
CURRENT_GEOCODER_KEY                    =   "currentGeocoder"
ARCGIS_BATCH_MAX_BATCH_SIZE_KEY         =   "arcgisMaxBatchSize"
ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY   =   "arcgisSuggestedBatchSize"

BULK_GEOCODE_MODE_KEY                   =   "bulkGeocodeMode"

BULK_GEOCODE_APPENDED_CSV_ID            =   "bulkgeocodeappendcsvid"
BULK_GEOCODE_EXPORTED_CSV_ID            =   "bulkgeocodeexportcsvid"
BULK_ERRORS_EXPORTED_CSV_ID             =   "bulkerrorsexportcsvid"

CURRENT_GENERIC_FUNCTION                =   "currentGenFunction"

CENSUS_DOWNLOAD_LISTS                   =   "censusdownloadlists"
CENSUS_CURRENT_MODE                     =   "censuscurrentmode"
CENSUS_DROP_DATASET_LISTS               =   "censusdropdataset"
CENSUS_DROP_SUBDATASET_LIST             =   "censusdropsubdataset"
CENSUS_CURRENT_DATASET                  =   "censuscurrentdataset"
CENSUS_CURRENT_GET_COLS_SUBDATA_ID      =   "censuscurrentgetcolssubdataid"
CENSUS_CURRENT_GET_COLS_SUBDATA_LISTS_ID      =   "censuscurrentgetcolssubdataidlists"

CENSUS_DATASET_TO_INSERT_FROM           =   "censusdatasettoinsertfrom"
CENSUS_DATASET_TYPES_TO_INSERT_FROM     =   "censusdatasettypestoinsertfrom"

CENSUS_ADD_DATASETS_LIST                =   "censusadddatasets"
CENSUS_DROP_DATASETS_LIST               =   "censusdropdatasets"

CENSUS_SELECTED_DATASET_ID              =   "censusdatasetid"
CENSUS_SELECTED_SUBSET_ID               =   "censussubsetid"


"""
#--------------------------------------------------------------------------
#   System config value keys
#--------------------------------------------------------------------------
"""
EULA_FLAG_KEY                           =   "EULARead"
SAVED_FILE_NAME_KEY                     =   "DCS_savedfilenname"
DFC_CURRENTLY_LOADED_KEY                =   "dfcleanserCurrentlyLoaded"
DFC_CHAPTERS_LOADED_KEY                 =   "dfcCurrentlyLoadedChapters"
CURRENT_DF_DISPLAYED_KEY                =   "dfcCurrentSelecteddf"

"""
#--------------------------------------------------------------------------
#   working column name
#--------------------------------------------------------------------------
"""
CURRENT_COL_NAME    =   "currentColumnName"

def get_current_col_name() :
    return(get_config_value(CURRENT_COL_NAME))


DEBUG_CFG   =   False


"""
#--------------------------------------------------------------------------
#   global keys that should be stored at the dfcleanser level
#--------------------------------------------------------------------------
"""
GlobalKeys     =   ["EULARead","geocoder","GoogleV3_querykwargs",
                    "arcgisgeocoderParms","binggeocoderParms","mapquestgeocoderParms",
                    "nomingeocoderParms","googlegeocoderParms","baidu_geocoderParms",
                    "googlebulkgeocoderParms","arcgisbatchgeocoderParms",
                    "bingbulkgeocoderParms","baidubulkgeocoderParms",
                    "PostgresqldbconnectorParms","MySQLdbconnectorParms","SQLitedbconnectorParms",
                    "OracledbconnectorParms","MSSQLServerdbconnectorParms","customdbconnectorParms",
                    "currentDBID","currentDBLIBID"]

def is_global_parm(key) :
    if(key in GlobalKeys) :
        return(True)
    else :
        return(False)


"""
#--------------------------------------------------------------------------
#   helper functions
#--------------------------------------------------------------------------
"""
def get_config_value(key) :
    return(DataframeCleansercfg.get_config_value(key))

def set_config_value(key, value, write_through=False) :
    DataframeCleansercfg.set_config_value(key,value,write_through)
    
def drop_config_value(key, write_through=False) :
    DataframeCleansercfg.drop_config_value(key, write_through)

def set_notebookName(nbname) :
    DataframeCleansercfg.set_notebookname(nbname)
    
def get_notebookName() :
    return(DataframeCleansercfg.get_notebookname())
    
def set_notebookPath(nbpath) :
    DataframeCleansercfg.set_notebookpath(nbpath)

    if(not (get_config_value(DFC_CURRENTLY_LOADED_KEY) is None)) :
        get_loaded_cells() 
        
        from dfcleanser.common.common_utils import log_debug_dfc
        log_debug_dfc(-1,"set_notebookPath - get_loaded_cells")

    
def get_notebookPath() :
    return(DataframeCleansercfg.get_notebookpath())  



"""
#--------------------------------------------------------------------------
#   Dataframe Cleanser config class
#--------------------------------------------------------------------------
"""

class DataframeCleansercfg :
    
    # instance variables
    
    # notebook specific cfg file data
    cfg_data                =   {}
    dfc_cfg_data            =   {}
    
    default_cfg_data        =   {}
    default_dfc_cfg_data    =   {"EULARead":"False"}
    
    notebookName            =   ""
    notebookPath            =   ""
    
    # Jupyter synced flag
    cfg_file_loaded         =   False
    dfc_cfg_file_loaded     =   False
    
    cfg_trace_log           =   []

    
    @staticmethod
    def add_to_cfg_error_log(msg,msg_type=0) :
        add_error_to_log(msg)
    
    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser config initialization methods
    #--------------------------------------------------------------------------
    """
    
    # full constructor
    def __init__(self) :
        
        DataframeCleansercfg.init_cfg_file(0) 
        DataframeCleansercfg.init_cfg_file(1)

    @staticmethod
    def init_cfg_file(cfgType) :
        
        if(cfgType == 0) :
            DataframeCleansercfg.init_cfg_file_data(DataframeCleansercfg.get_cfg_dir_name(),
                                                    DataframeCleansercfg.get_cfg_file_name(),
                                                    0,
                                                    DataframeCleansercfg.cfg_file_loaded)
        else :
            DataframeCleansercfg.init_cfg_file_data(DataframeCleansercfg.get_dfc_cfg_dir_name(),
                                                    DataframeCleansercfg.get_dfc_cfg_file_name(),
                                                    1,
                                                    DataframeCleansercfg.dfc_cfg_file_loaded)
    
    @staticmethod
    def init_cfg_file_data(cfg_dirname,cfg_filename,cfgType,storeFlag) :
        
        import time
        
        retry_limit     =   5
        delay_seconds   =   1
        current_retry   =   0
        
        if(not (cfg_dirname is None)) :
            
            if(not (does_dir_exist(cfg_dirname))) :
                make_dir(cfg_dirname)
        
            if(not (does_file_exist(cfg_filename))) :
                
                # The very first cfg file load
                while(current_retry < retry_limit) :

                    try :
                    
                        with open(cfg_filename, 'w') as  cfg_file :
                            if(cfgType == 0) :
                                json.dump(DataframeCleansercfg.default_cfg_data,cfg_file)
                            else :
                                json.dump(DataframeCleansercfg.default_dfc_cfg_data,cfg_file)
                        
                            cfg_file.close()
                            
                        current_retry     =   retry_limit
                        
                        if(cfgType == 0) :
                            
                            DataframeCleansercfg.cfg_data   =   DataframeCleansercfg.default_cfg_data
                            DataframeCleansercfg.cfg_file_loaded = True
                            
                        else :
                            
                            DataframeCleansercfg.dfc_cfg_data   =   DataframeCleansercfg.default_dfc_cfg_data
                            DataframeCleansercfg.dfc_cfg_file_loaded = True
                            
                        break
                    
                    except :
                        current_retry   =   current_retry + 1
                        time.sleep(delay_seconds)
            
            # cfg file does exist
            else :
                
                while(current_retry < retry_limit) :
                    
                    try :

                        with open( cfg_filename, 'r') as  cfg_file :
                            
                            if(cfgType == 0) :
                                DataframeCleansercfg.cfg_data = json.load(cfg_file)
                            else :
                                DataframeCleansercfg.dfc_cfg_data = json.load(cfg_file)
                                
                            cfg_file.close()
                    
                        if(cfgType == 0) :
                            DataframeCleansercfg.cfg_file_loaded = True
                        else :
                            DataframeCleansercfg.dfc_cfg_file_loaded = True
                        
                        current_retry     =   retry_limit
                        
                        break
                    
                    except json.JSONDecodeError :
                        
                        try :
                                
                            with open( cfg_filename, 'w') as  cfg_file :
                                if(cfgType == 0) :
                                    json.dump(DataframeCleansercfg.default_cfg_data,cfg_file)
                                    DataframeCleansercfg.cfg_data = DataframeCleansercfg.default_cfg_data
                                else :
                                    json.dump(DataframeCleansercfg.default_dfc_cfg_data,cfg_file)
                                    DataframeCleansercfg.dfc_cfg_data = DataframeCleansercfg.default_dfc_cfg_data
                                
                            cfg_file.close()
                                
                        except :
                            DataframeCleansercfg.add_to_cfg_error_log("[Load default cfg file Error - for json decode error] "  + str(sys.exc_info()[0].__name__),1)


    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser config files dirs and names
    #--------------------------------------------------------------------------
    """
    
    @staticmethod 
    def get_cfg_dir_name() :
        
        nbdir   =   DataframeCleansercfg.get_notebookpath()
        nbname  =   DataframeCleansercfg.get_notebookname()
        
        if((nbdir is None)or(nbname is None)) :
            return(None)
        else :
            return(os.path.join(nbdir,nbname + "_files"))
    
    @staticmethod
    def get_cfg_file_name() :
        
        cfgdir  =   DataframeCleansercfg.get_cfg_dir_name()
        nbname  =   DataframeCleansercfg.get_notebookname()
        
        if((cfgdir is None)or(nbname is None)) :
            return(None)
        else :
            return(os.path.join(cfgdir,nbname + "_config.json"))    
    
    @staticmethod
    def get_dfc_cfg_dir_name() :
        
        dfcdir  =   get_dfcleanser_location() 
        return(os.path.join(dfcdir,"files"))
    
    @staticmethod
    def get_dfc_cfg_file_name() :

        dfcdir  =   DataframeCleansercfg.get_dfc_cfg_dir_name()   
        
        if(dfcdir is None) :
            return(None)
        else :
            return(os.path.join(dfcdir,"dfcleanserCommon_config.json")) 
    
    @staticmethod
    def save_cfg_file(cfgType) :
        
        if(cfgType == 0) :
        
            if(DataframeCleansercfg.cfg_file_loaded) :
    
                try :
                    
                    with open(DataframeCleansercfg.get_cfg_file_name(), 'w') as cfg_file :
                        json.dump(DataframeCleansercfg.cfg_data,cfg_file)
                        cfg_file.close()
                    
                except :
                    
                    DataframeCleansercfg.add_to_cfg_error_log("[Save cfg file Error] "  + str(sys.exc_info()[0].__name__),1)
                     
            else :
                
                DataframeCleansercfg.add_to_cfg_error_log("[Unable to Save cfg file Error : because cfg not loaded] ",1)
       
        else :
            
            if(DataframeCleansercfg.dfc_cfg_file_loaded) :

                try :
                    with open(DataframeCleansercfg.get_dfc_cfg_file_name(), 'w') as cfg_file :
                        json.dump(DataframeCleansercfg.dfc_cfg_data,cfg_file)
                        cfg_file.close()
            
                except :

                    DataframeCleansercfg.add_to_cfg_error_log("[Save dfc cfg file Error] "  + str(sys.exc_info()[0].__name__),1)
        
    @staticmethod
    def is_loaded(cfgtype) :

        if(cfgtype == 0) :
        
            if(not (DataframeCleansercfg.cfg_file_loaded)) :
                DataframeCleansercfg.wait_for_cfg_file_load(0)
        
            if(not (DataframeCleansercfg.cfg_file_loaded)) :
                return(False)
            else :
                return(True)
                
        else :
            
            if(not (DataframeCleansercfg.dfc_cfg_file_loaded)) :
                DataframeCleansercfg.wait_for_cfg_file_load(1)
        
            if(not (DataframeCleansercfg.dfc_cfg_file_loaded)) :
                return(False)
            else :
                return(True)

    @staticmethod
    def wait_for_cfg_file_load(cfgtype) :
        
        import time
        
        if(cfgtype == 0) :
            load_flag   =   DataframeCleansercfg.cfg_file_loaded
        else :
            load_flag   =   DataframeCleansercfg.dfc_cfg_file_loaded
        
        if(not (load_flag)) :
            
            wait_for_load   =   True
            retry_limit     =   10
            retry_count     =   0
            retry_delay     =   0.1
            
            while(wait_for_load)  :
                
                time.sleep(retry_delay)  
                retry_count     =   retry_count + 1
                
                if(retry_count == retry_limit) :
                    wait_for_load = False
                else :
                    if(cfgtype == 0) :
                        if(DataframeCleansercfg.cfg_file_loaded) :
                            wait_for_load = False  
                    else :
                        if(DataframeCleansercfg.dfc_cfg_file_loaded) :
                            wait_for_load = False  
        
        if(cfgtype == 0) :
            
            if(not (DataframeCleansercfg.cfg_file_loaded)) :
                return(False)
            else :
                return(True)
                
        else :
            
            if(not (DataframeCleansercfg.dfc_cfg_file_loaded)) :
                return(False)
            else :
                return(True)

    @staticmethod        
    def get_config_value(key) :
        
        if(not(is_global_parm(key))) :
            
            if(DataframeCleansercfg.is_loaded(0)) :
                return(DataframeCleansercfg.cfg_data.get(key,None))
            else :
                DataframeCleansercfg.add_to_cfg_log("[get_config_value _ unable to load cfg_data] : "  + str(key) + " " + str(len(DataframeCleansercfg.cfg_data)),1)
                return(None)
                
        else :
            
            if(DataframeCleansercfg.is_loaded(1)) :
                return(DataframeCleansercfg.dfc_cfg_data.get(key,None))
            else :
                DataframeCleansercfg.add_to_cfg_error_log("[get_config_value _ unable to load dfc_cfg_data] : "  + str(key) + " " + str(len(DataframeCleansercfg.cfg_data)),1)
                return(None)
        
    @staticmethod        
    def set_config_value(key, value, write_through) :
        
        if(not(is_global_parm(key))) :
            
            if(DataframeCleansercfg.is_loaded(0)) :
                DataframeCleansercfg.cfg_data.update({key : value})
                if(write_through) :
                    DataframeCleansercfg.save_cfg_file(0)
            else :
                DataframeCleansercfg.add_to_cfg_error_log("[set_config_value - unable to load cfg_data] : "  + str(key) + " " + str(len(DataframeCleansercfg.cfg_data)),1)
                
        else :
            
            if(DataframeCleansercfg.is_loaded(1)) :
                DataframeCleansercfg.dfc_cfg_data.update({key : value})
                DataframeCleansercfg.save_cfg_file(1)
            else :
                DataframeCleansercfg.add_to_cfg_error_log("[set_config_value - unable to load dfc_cfg_data] : "  + str(key) + " " + str(len(DataframeCleansercfg.dfc_cfg_data)),1)
        
    @staticmethod       
    def drop_config_value(key, write_through) :
        
        if(not(is_global_parm(key))) :
            
            if(DataframeCleansercfg.is_loaded(0)) :
                popped  =   DataframeCleansercfg.cfg_data.pop(key,None)
                if(not (popped is None)) :
                    if(write_through) :
                        DataframeCleansercfg.save_cfg_file(0)
            else :
                DataframeCleansercfg.add_to_cfg_error_log("[drop_config_value - unable to load cfg_data] : "  + str(key) + " " + str(len(DataframeCleansercfg.cfg_data)),1)
                
        else :
            
            if(DataframeCleansercfg.is_loaded(1)) :
                popped  =   DataframeCleansercfg.dfc_cfg_data.pop(key,None)
                if(not (popped is None)) :
                    DataframeCleansercfg.save_cfg_file(1)
            else :
                DataframeCleansercfg.add_to_cfg_error_log("[drop_config_value - unable to load dfc_cfg_data] : "  + str(key) + " " + str(len(DataframeCleansercfg.dfc_cfg_data)),1)


    #---------------------------------------------------
    #   dfcleanser common values
    #--------------------------------------------------- 
    @staticmethod
    def set_notebookname(nbname) :
        DataframeCleansercfg.notebookName = nbname

    @staticmethod
    def set_notebookpath(nbpath) :
        DataframeCleansercfg.notebookPath = nbpath
        DataframeCleansercfg.init_cfg_file(0)
        DataframeCleansercfg.init_cfg_file(1)
        
    @staticmethod    
    def get_notebookname() :
        return(DataframeCleansercfg.notebookName) 
    @staticmethod    
    def get_notebookpath() :
        return(DataframeCleansercfg.notebookPath) 

    @staticmethod
    def sync_js(parms) :

        nbname  =   parms[0]
        DataframeCleansercfg.set_notebookname(nbname)
        get_notebookpath()
        
"""
* ----------------------------------------------------
# static instantiation of the config data object
* ----------------------------------------------------
"""    
DataframeCleanserCfgData    =   DataframeCleansercfg()



"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   generic dfcleanser error logger
#------------------------------------------------------------------
#------------------------------------------------------------------
"""  

def add_error_to_log(msg) :
    dfc_erorr_log.add_error_to_dfc_log(msg)

def dump_error_log() :
    elog    =   dfc_erorr_log.get_error_log() 
    
    if(len(elog) > 0) :
        for i in range(len(elog)) :
            print("[",str(i),"] : ",str(elog[i]))
   
def clear_error_log() :
    dfc_erorr_log.clear_log() 


class DataframeCleanserErrorLogger :
    
    # instance variables
    
    # error log
    error_log               =   []
    error_log_loaded        =   False
    
    # full constructor
    def __init__(self) :
        
        self.error_log               =   []
        self.error_log_loaded        =   False
 
        self.init_errorlog_file() 
        
    def get_errorlog_dir_name(self) :
        
        from dfcleanser.common.cfg import get_notebookPath, get_notebookName
        nbdir   =   get_notebookPath()
        nbname  =   get_notebookName()
        
        if((nbdir is None)or(nbname is None)) :
            return(None)
        else :
            return(os.path.join(nbdir,nbname + "_files"))
   
    def get_errorlog_file_name(self) :
        
        from dfcleanser.common.cfg import get_notebookName
        eldir   =   self.get_errorlog_dir_name()
        nbname  =   get_notebookName()
        
        if((eldir is None)or(nbname is None)) :
            return(None)
        else :
            return(os.path.join(eldir,nbname + "_errorlog.json"))    
    
    def init_errorlog_file(self) :
        
        errorlog_dirname   =   self.get_errorlog_dir_name()
        if(not (errorlog_dirname is None)) :
            
            if(not (does_dir_exist(errorlog_dirname))) :
                make_dir(errorlog_dirname)
        
            errorlog_filename   =   self.get_errorlog_file_name()
        
            if(not (does_file_exist(errorlog_filename))) :

                with open(errorlog_filename, 'w') as error_file :
                    json.dump(self.error_log,error_file)
                    error_file.close()
            else :
                
                try :

                    with open(errorlog_filename, 'r') as errorlog_file :
                        self.errorlog = json.load(errorlog_file)
                        errorlog_file.close()
                        
                    self.error_log_loaded = True
                    
                except json.JSONDecodeError :
                    self.errorlog.append("Error Log File Corrupted")
                except :
                    self.errorlog.append("[Load Error Log Error] "  + str(sys.exc_info()[0].__name__))
        
    def save_errorlog_file(self) :
        
        if(1) :#self.error_log_loaded) :
    
            try :
                with open(self.get_errorlog_file_name(), 'w') as errorlog_file :
                    json.dump(self.error_log,errorlog_file)
                    errorlog_file.close()
            
            except :
                self.add_error_to_dfc_log("[Save Error Log Error] "  + str(sys.exc_info()[0].__name__))    
   
    def add_error_to_dfc_log(self,msg) :
        
        import datetime
        date = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        
        self.error_log.append("[" + date + "]" + msg) 
        self.save_errorlog_file()   
  
    def get_error_log(self) :
        
        return(self.error_log) 

    def clear_log(self) :
        self.error_log               =   []
        

    
dfc_erorr_log   =   DataframeCleanserErrorLogger()  










"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  dfc dataframe storage class
#
#   a dfc dataframe is an object that contains a description, 
#   a pandas dataframe and descriptive notes
#
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   dfc dataframes store
#--------------------------------------------------------------------------
"""
class dfc_dataframes :
    
    dcdataframes    =   []

    def __init__(self):
        self.dcdataframes   =   []
        
        drop_config_value(CURRENT_INSPECTION_DF)
        drop_config_value(CURRENT_CLEANSE_DF)
        drop_config_value(CURRENT_TRANSFORM_DF)
        drop_config_value(CURRENT_EXPORT_DF)
        drop_config_value(CURRENT_IMPORT_DF)
        drop_config_value(CURRENT_GEOCODE_DF)
        drop_config_value(CURRENT_SUBSET_DF)

    def is_a_dfc_dataframe_loaded(self) :
        if(len(self.dcdataframes) > 0) :
            return(True)
        else :
            return(False)
        
    """
    * ------------------------------------
    * add or drop dfc dataframes 
    * ------------------------------------
    """        
    def add_dataframe(self,dfcdf) :
        for i in range(len(self.dcdataframes)) :
            if(self.dcdataframes[i].get_title() == dfcdf.get_title()) :
                self.drop_dataframe(dfcdf.get_title())    
        
        self.dcdataframes.append(dfcdf)
        
    def drop_dataframe(self,title) :
            
        dfindex     =   self.get_df_index(title)
        if(dfindex > -1) :
            del self.dcdataframes[dfindex]

    """
    * ------------------------------------
    * get dfc dataframe components
    * ------------------------------------
    """        
    def get_dataframe(self,title=None) :
        if(title == None) :
            dfindex     =   self.get_df_index(self.current_df)
        else :
            dfindex     =   self.get_df_index(title)
            
        if(dfindex > -1) :            
            return(self.dcdataframes[dfindex].get_df())
        else :
            return(None)
    
    def update_dataframe(self,title,df) :
        if(title == None) :
            dfindex     =   self.get_df_index(self.current_df)
        else :
            dfindex     =   self.get_df_index(title)
            
        if(dfindex > -1) :            
            return(self.dcdataframes[dfindex].set_df(df))
        else :
            print("no dataframe found for " + title)
                
    def get_dfc_dataframe(self,title) : 
        dfc_index   =  self.get_df_index(title)
        if(dfc_index == -1) :
            return(None)
        else :
            return(self.dcdataframes[dfc_index])
    
    def get_dataframe_notes(self,title) :
        if(title == None) :
            dfindex     =   self.get_df_index(self.current_df)
            if(dfindex > -1) :            
                return(self.dcdataframes[dfindex].get_notes())
            else :
                return(None)
        else :
            dfindex     =   self.get_df_index(title)
            if(dfindex > -1) :            
                return(self.dcdataframes[dfindex].get_notes())
            else :
                return(None)
    
    def set_dataframe_notes(self,title,notes) :
        if(title == None) :
            dfindex     =   self.get_df_index(self.current_df)
            if(dfindex > -1) :            
                self.dcdataframes[dfindex].set_notes(notes)
        else :
            dfindex     =   self.get_df_index(title)
            if(dfindex > -1) :            
                self.dcdataframes[dfindex].set_notes(notes)

    def rename_dataframe(self,oldName,newName) :
        dfindex     =   self.get_df_index(oldName)
        if(dfindex > -1) :            
            self.dcdataframes[dfindex].set_title(newName)
            
            if(oldName == self.current_df) :
                self.current_df     =   newName
                
    def get_dataframe_titles(self) :
        
        if(len(self.dcdataframes) > 0) :
            titles  =   []
            for i in range(len(self.dcdataframes)) :
                titles.append(self.dcdataframes[i].get_title())
                
            return(titles)
        else :
            return(None)
            
    def get_df_index(self,title) :
        
        for i in range(len(self.dcdataframes)) :
            if(self.dcdataframes[i].get_title() == title) :
                return(i)
                
        return(-1)
        
    def get_df_count(self) :
        return(len(self.dcdataframes))
        
"""
#--------------------------------------------------------------------------
#   dfc dataframe factory object
#--------------------------------------------------------------------------
"""
dfc_dfs     =   dfc_dataframes()




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser cells functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def get_util_chapters_loaded() :
    
    cellsList   =   get_config_value(DFC_CHAPTERS_LOADED_KEY)
    utilcbs     =   [0,0,0,0,0,0]

    if(not (cellsList == None)) :
        
        if(cellsList[21])    :   utilcbs[0] = 1
        if(cellsList[22])    :   utilcbs[1] = 1
        if(cellsList[23])    :   utilcbs[2] = 1
        if(cellsList[24])    :   utilcbs[3] = 1
        if(cellsList[25])    :   utilcbs[4] = 1
        if(cellsList[26])    :   utilcbs[5] = 1
        
    return(utilcbs)
   

def set_chapters_loaded(cellsList) :
    
    set_config_value(DFC_CHAPTERS_LOADED_KEY, cellsList,True)
   

def get_loaded_cells() :

    run_javascript("window.getdfcChaptersLoaded();",
                   "Unable to get cells loaded")
    
    from dfcleanser.common.common_utils import log_debug_dfc
    log_debug_dfc(-1,"get_loaded_cells")


def check_if_dc_init() :
    
    if( not(DataframeCleanserCfgData.get_notebookname() == None) ) :
        if( not(DataframeCleanserCfgData.get_notebookpath() == None) ) :  
            return(True)
    else :
        return(False)

        
def save_current_notebook() :

    run_javascript("window.saveCurrentNotebook();",
                   "Unable to save notebook")
    
    from dfcleanser.common.common_utils import log_debug_dfc
    log_debug_dfc(-1,"save current notebook")



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser common notebook and path functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def create_notebook_dir_and_cfg_files(notebookname,nbpath) :
    
    # create the proper dir
    os.chdir(os.path.join(nbpath))
    os.makedirs("./" + notebookname + "_files" + "/")
    os.chdir(nbpath + "/" + notebookname + "_files")
                
    # create the notebook specific files
    fname = notebookname + "_config.json"
    initcfg = {NOTEBOOK_TITLE : notebookname}
                
    with open(fname,'w') as dfc_cfg_file :
        json.dump(initcfg,dfc_cfg_file)
        dfc_cfg_file.close()
                
    fname = notebookname + "_scriptlog.json"
    initslog = {NOTEBOOK_TITLE : notebookname}
                
    with open(fname,'w') as dfc_script_file :
        json.dump(initslog,dfc_script_file)
        dfc_script_file.close()
    

def check_notebook_dir_and_cfg_files(notebookname) :
    
    nbpath  =  DataframeCleanserCfgData.get_notebookpath()
    
    if(not(nbpath == None)) :

        if(os.path.exists(nbpath + "/" + notebookname + "_files")) :
            if(os.path.isdir(nbpath + "/" + notebookname + "_files")) :
                
                # if no config file create one
                if(not(os.path.exists(nbpath + "/" + notebookname + "_files" + "/" + notebookname + "_config.json"))) : 
                    # create the initial config file 
                    fname = notebookname + "_config.json"
                    initcfg = {NOTEBOOK_TITLE : notebookname}
                    
                    with open(fname,'w') as dfc_cfg_file :
                        json.dump(initcfg,dfc_cfg_file)
                        dfc_cfg_file.close()
                
                # if no scriptlog file create one
                if(not(os.path.exists(nbpath + "/" + notebookname + "_files" + "/" + notebookname + "_scriptlog.json"))) : 
                    # create the initial config file 
                    fname = notebookname + "_scriptlog.json"
                    initslog = {NOTEBOOK_TITLE : notebookname}
                    
                    with open(fname,'w') as dfc_script_file :
                        json.dump(initslog,dfc_script_file)
                        dfc_script_file.close()
                
            else :
                # delete it if it is a file and not a dir
                try :
                    os.remove(nbpath + "/" + notebookname)
                    
                    import win32api
                    win32api.MessageBox(None,"remove cfg dir file","remove",1)

                    create_notebook_dir_and_cfg_files(notebookname,nbpath)
                except FileNotFoundError :
                    print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))
                except Exception :
                    print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))
                
        else :
            
            # notebook path and name not found so create them
            try :
                create_notebook_dir_and_cfg_files(notebookname,nbpath)
            except FileNotFoundError :
                print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))
            except Exception :
                print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))


"""
* ----------------------------------------------------
# dfcleanser mode - inline or popup
* ----------------------------------------------------
""" 

INLINE_MODE     =   0
POP_UP_MODE     =   1
     
def set_dfc_mode(mode) :
    dfcMode.set_mode(mode)

def get_dfc_mode() :   
    return(dfcMode.get_mode())

class dfc_mode :
    
    # instance variables
    mode                    =   INLINE_MODE
    
    # full constructor
    def __init__(self) :
        self.mode               =   INLINE_MODE
        
    def set_mode(self,inmode) :
        self.mode  =   inmode
        run_javascript("set_dfcmode(" + str(inmode) + ");","Unable to set mode")

    def get_mode(self) :
        return(self.mode)
   

dfcMode     =   dfc_mode()    
