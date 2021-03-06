"""
# system_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

Red     = "#FAA78F"
Green   = "#8FFAC0"
Yellow  = "#FAFB95"

READMEText =  """
README
"""

DISPLAY_MAIN                =   0
DISPLAY_CHAPTERS            =   1
RESET_CHAPTERS              =   2
DISPLAY_DATAFRAMES          =   3
DISPLAY_SYSTEM              =   4
DISPLAY_DFC_FILES           =   5
DISPLAY_ABOUT               =   6
DISPLAY_ADD_DATAFRAME       =   7
DISPLAY_OFFLINE             =   8

DISPLAY_EULA                =   12
PROCESS_EULA                =   13

DISPLAY_README              =   14

PROCESS_CHAPTERS            =   15
DISPLAY_ABBR_MAIN           =   16

EXIT_SETUP                  =   17

PROCESS_DATAFRAME           =   18
PROCESS_ADD_DATAFRAME       =   19

CORE                        =   0
UTILITIES                   =   1
SCRIPTING                   =   2

COPY_FILES                  =   0
RENAME_FILES                =   1
DELETE_FILES                =   2

DROP_DATAFRAME              =   0
SET_DATAFRAME               =   1
UPDATE_DATAFRAME            =   2
RENAME_DATAFRAME            =   3
ADD_DATAFRAME               =   4
RETURN_DATAFRAME            =   5

DEBUG_SYSTEM                =   True

"""
* ----------------------------------------------------
# dfcleanser system and document loaded
* ----------------------------------------------------
""" 

INLINE_MODE     =   0
POP_UP_MODE     =   1
     
def set_document_loaded() :
    dfc_document_loaded_status.set_document_loaded()

def is_document_loaded() :   
    return(dfc_document_loaded_status.is_document_loaded())

class dfc_document_status :
    
    # instance variables
    document_loaded             =   False
    
    # full constructor
    def __init__(self) :
        self.document_loaded    =   False
        
    def set_document_loaded(self) :
        self.document_loaded  =   True

    def is_document_loaded(self) :
        return(self.document_loaded)
   

dfc_document_loaded_status     =   dfc_document_status()   

def set_dfc_run_offline_status(status) :
    
    global Run_DFC_Offline
    
    if(not status) :
        Run_DFC_Offline     =   False
    else :
        Run_DFC_Offline     =   True
        from dfcleanser.common.common_utils import copy_dfc_images_to_local
        copy_dfc_images_to_local()
    
def get_dfc_run_offline_status() :
    
    global Run_DFC_Offline
    
    return(Run_DFC_Offline)
    
    
Run_DFC_Offline     =   False
 

