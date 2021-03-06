"""
# sw_utility_bulk_geocode_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import dfcleanser.common.cfg as cfg

import dfcleanser.sw_utilities.sw_utility_geocode_model as sugm
import dfcleanser.sw_utilities.sw_utility_geocode_widgets as sugw

import dfcleanser.common.help_utils as dfchelp

from dfcleanser.common.html_widgets import (maketextarea) 
from dfcleanser.common.common_utils import (display_generic_grid, opStatus,  
                                            display_exception,
                                            get_parms_for_input, get_select_defaults)

from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, 
                                             SCROLL_DOWN, ROW_MAJOR)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    google bulk forms 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   google geocoder connect parms
#--------------------------------------------------------------------------
"""
google_bulk_geocoder_title               =   "Google V3 Bulk Geocoder Connector"
google_bulk_geocoder_id                  =   "googlebulkgeocoder"

google_bulk_geocoder_idList              =    ["ggbapikey",
                                               "ggbclient",
                                               "ggbclientsecret",
                                               "ggbtimeout",
                                               "ggbconnecttimeout",
                                               "ggbreadtimeout",
                                               "ggbretrytimeout",
                                               "ggbqueriespersecond",
                                               "ggbretryoverquerylimit",
                                               "ggbchannel",
                                               "ggbrequestskwargs",
                                               None,None,None,None,None,None,None]

google_bulk_geocoder_labelList           =   ["api_key",
                                              "client_id",
                                              "client_secret",
                                              "timeout",
                                              "connect_timeout",
                                              "read_timeout",
                                              "retry_timeout",
                                              "queries_per_second",
                                              "retry_over_query_limit",
                                              "channel",
                                              "requests_kwargs",
                                              "Test</br>Bulk</br>Geocoder</br>Connection",
                                              "Bulk</br>Geocoding",
                                              "Bulk</br>Reverse</br>Geocoding",
                                              "Bulk</br>Geocoding</br>Tuning",
                                              "Clear","Return","Help"]


google_bulk_geocoder_typeList            =   ["text","text","text","text","text","text","text","text","select","text","text",
                                              "button","button","button","button","button","button","button"]

google_bulk_geocoder_placeholderList     =   ["enter account api key.",
                                              "enter account client id. (default - None) required for premier",
                                              "enter account client secret. (default - None) required for premier",
                                              "Combined overall timeout for HTTP requests, in seconds. (default - None)",
                                              "Connection timeout in seconds. (default - None)",
                                              "Read(HTTP) timeout in seconds. (default - None)",
                                              "Retry(HTTP) timeout in seconds. (default - None)",
                                              "Number of queries per second permitted (default 25 - Max 50)",
                                              "retry over query limit flag (default - False)",
                                              "channel parameter (default - None)",
                                              "Keyword args -http://docs.python-requests.org/en/latest/api/#main-interface ",
                                              None,None,None,None,None,None,None]

google_bulk_geocoder_jsList              =   [None,None,None,None,None,None,None,None,None,None,None,
                                              "test_geocoder(" + str(sugm.GoogleId) + "," + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.GoogleId)  + "," + str(sugm.QUERY) + ","  + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.GoogleId)  + "," + str(sugm.REVERSE) + ","  + str(sugm.BULK) + ")",
                                              "display_geocoders(" + str(sugm.GoogleId) + "," + str(sugm.BULK_TUNING) + ")",
                                              "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                              "geocode_return()",
                                              "displayhelp('" + str(dfchelp.GoogleInitHelp) + "')"]

google_bulk_geocoder_reqList             =   [0,1,2]

google_bulk_geocoder_form                =   [google_bulk_geocoder_id,
                                              google_bulk_geocoder_idList,
                                              google_bulk_geocoder_labelList,
                                              google_bulk_geocoder_typeList,
                                              google_bulk_geocoder_placeholderList,
                                              google_bulk_geocoder_jsList,
                                              google_bulk_geocoder_reqList]

google_API_Key    =   "AIzaSyA8_3-UFBQTxukj6ePW0wp7eLW45GH3B7c"


"""
#--------------------------------------------------------------------------
#    google geocode bulk form 
#--------------------------------------------------------------------------
"""
bulk_google_query_input_title             =   "Google Bulk Geoocoding Parameters"
bulk_google_query_input_id                =   "googlebulkquery"
bulk_google_query_input_idList            =   ["bgqdataframe",
                                               "bgqaddress",
                                               "bgqcolumnname",
                                               "bgqsaveaddress",
                                               "bgqregion",
                                               "bgqlanguage",
                                               "bgqloctypes",
                                               "bgqsaveloctype",
                                               "bgqbulknumberlimit",
                                               "bgqbulkfailurelimit",
                                               "bgqbulkcheckpoint",
                                               None,None,None,None,None,None]

bulk_google_query_input_labelList         =   ["dataframe_to_geocode_from",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "save_geocoder_full_address_column_name",
                                               "region",
                                               "language",
                                               "valid_location_types",
                                               "save_location_type",
                                               "max_addresses_to_geocode",
                                               "failure_limit_percent",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Location </br>Types",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Clear","Return","Help"]

bulk_google_query_ltypes_input_labelList  =   ["dataframe_to_geocode_from",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "save_geocoder_full_address_column_name",
                                               "region",
                                               "language",
                                               "valid_location_types",
                                               "save_location_type_flag",
                                               "max_addresses_to_geocode",
                                               "failure_limit",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Coords",
                                               "Get</br> Column</br>Names",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Clear","Return","Help"]

bulk_google_query_input_typeList          =   ["select",maketextarea(4),"select","text",
                                               "select","select","text","select","text","text","text",
                                               "button","button","button","button","button","button"]

bulk_google_query_input_placeholderList   =  ["dataframe to geocode",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "Latitude,Longitude - stored as 2 columns  - [Latitude,Longitude] stored as one col",
                                              "full address column name (default = None - don't retrieve full address and save)",
                                              "region (default - None)",
                                              "language (default - english)",
                                              "valid location types default - ALL",
                                              "save location type default - False",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "failure limit (default - 2%)",
                                              "check point interval (default - every 10,000 rows)",
                                               None,None,None,None,None,None]

bulk_google_query_input_jsList            =   [None,None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.LOCATION_TYPES_TABLE) + "," + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "display_help_url('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_google_query_ltypes_input_jsList     =   [None,None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.COLNAMES_TABLE) + "," + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "displayhelpurl('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_google_query_input_reqList           =   [0,1,2,3]

bulk_google_query_input_form              =   [bulk_google_query_input_id,
                                               bulk_google_query_input_idList,
                                               bulk_google_query_input_labelList,
                                               bulk_google_query_input_typeList,
                                               bulk_google_query_input_placeholderList,
                                               bulk_google_query_input_jsList,
                                               bulk_google_query_input_reqList]  


"""
#--------------------------------------------------------------------------
#    google reverse bulk form 
#--------------------------------------------------------------------------
"""
bulk_google_reverse_input_title           =   "Google Bulk Reverse Parameters"
bulk_google_reverse_input_id              =   "googlebulkreverse"
bulk_google_reverse_input_idList          =   ["bgrdataframe",
                                               "bgrcolumnname",
                                               "bgraddresscomponents",
                                               "bgraddresslength",
                                               "bgrcolumnnames",
                                               "bgqloctypes",
                                               "bgrlanguage",
                                               "bgrbulknumberlimit",
                                               "bgrbulkfailurelimit",
                                               "bgrbulkcheckpoint",
                                               None,None,None,None,None,None,None]

bulk_google_reverse_input_labelList       =   ["dataframe_to_geocode_from",
                                               "dataframe_lat_long_column_name(s)",
                                               "address_components_list",
                                               "address_components_length_flag",
                                               "address_column_name(s)",
                                               "valid_location_type(s)",
                                               "language",
                                               "max_lat_longs",
                                               "failure_limit",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Addresses",
                                               "Get</br>Column</br>Names",
                                               "Get</br>Address</br>Comps",
                                               "Get</br>Location</br>Types",
                                               "Clear","Return","Help"]

bulk_google_reverse_input_typeList        =   ["select","text",maketextarea(6),"select","text","text",
                                               "select","text","text","text",
                                               "button","button","button","button","button","button","button"]

bulk_google_reverse_input_placeholderList =  ["datframe to geocode from",
                                              "lat long colname(s) - latitudfe, longitude - 2 cols [latcolname,longcolname] 1 col",
                                              "address components list (default = None - store full address in address_column_name(s))",
                                              "address components short length (default = True) False = Long)",
                                              "single address column name to store full address or [list] to store address components",
                                              "A filter of one or more location types to accept as valid (default - ALL)",
                                              "language (default - english)",
                                              "number of lat_lngs to get addresses for (default - len(dataframe))",
                                              "failure limit (default - 2%)",
                                              "checkpoint interval (default - every 10,000 rows)",
                                               None,None,None,None,None,None,None]

bulk_google_reverse_input_jsList          =   [None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.COLNAMES_TABLE) + "," + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.ADDRESS_COMPONENTS_TABLE) + "," + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "get_geocoding_table(" + str(sugm.LOCATION_TYPES_TABLE) + "," + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.GoogleId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "displayhelp('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_google_reverse_input_reqList         =   [0,1,2,3,4,5,6]

bulk_google_reverse_input_form            =   [bulk_google_reverse_input_id,
                                               bulk_google_reverse_input_idList,
                                               bulk_google_reverse_input_labelList,
                                               bulk_google_reverse_input_typeList,
                                               bulk_google_reverse_input_placeholderList,
                                               bulk_google_reverse_input_jsList,
                                               bulk_google_reverse_input_reqList]  


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   arcGIS get batch forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

create_user_url = "https://richardkrasinski.maps.arcgis.com"
user = "RichardKrasinski"
pw = "ArcGISPW2018"


"""
#--------------------------------------------------------------------------
#   arcgis batch geocoder connect parms
#--------------------------------------------------------------------------
"""
arcgis_connect_help                       =   "https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html#gis"


batch_arcgis_geocoder_title               =   "ArcGis Batch Geocoder Connector"
batch_arcgis_geocoder_id                  =   "arcgisbatchgeocoder"

batch_arcgis_geocoder_idList              =    ["agburl",
                                                "agbusername",
                                                "agbpassword",
                                                "agbkeyfile",
                                                "agbcertfile",
                                                "agbverifycert",
                                                "agbsetactive",
                                                "agbclientid",
                                                "agbprofile",
                                                "agbkwargs",
                                                None,None,None,None,None,None]

batch_arcgis_geocoder_labelList           =   ["url",
                                              "username",
                                              "password",
                                              "key_file",
                                              "cert_file",
                                              "verify_cert",
                                              "set_active",
                                              "client_id",
                                              "profile",
                                              "kwargs",
                                              "Test</br>Bulk</br>Geocoder</br>Connection",
                                              "Bulk</br>Geocoding",
                                              "Interactive</br>Geocoding",
                                              "Clear","Return","Help"]


batch_arcgis_geocoder_typeList            =   ["text","text","text","text","text","text","text","text","text",maketextarea(4),
                                              "button","button","button","button","button","button"]

batch_arcgis_geocoder_placeholderList     =   ["a web address to either a local Portal or to ArcGIS Online (default - None)",
                                              "login user name (case-sensitive)",
                                              "password (case-sensitive)",
                                              "The file path to a user’s key certificate for PKI authentication. (default - None)",
                                              "The file path to a user’s certificate file for PKI authentication. (default - None)",
                                              "ensure all SSL. (default - True)",
                                              "The GIS object will be used as the default GIS object throughout. (default - True)",
                                              "Optional string for the client ID value. (default None)",
                                              "profile that the user wishes to use to authenticate. (default - None)",
                                              "option keyword args (default - None)",
                                              None,None,None,None,None,None]

batch_arcgis_geocoder_jsList              =   [None,None,None,None,None,None,None,None,None,None,
                                              "test_geocoder(" + str(sugm.ArcGISId) + "," + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.ArcGISId) + "," + str(sugm.QUERY)  + "," + str(sugm.BULK) + ")",
                                              "display_geocoders(" + str(sugm.ArcGISId) + "," + str(sugm.INTERACTIVE) + ")",
                                              "clear_geocode_form(" + str(sugm.ArcGISId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                              "geocode_return()",
                                              "displayhelp('" + arcgis_connect_help + "')"]

batch_arcgis_geocoder_reqList             =   [0,1,2]

batch_arcgis_geocoder_form                =   [batch_arcgis_geocoder_id,
                                               batch_arcgis_geocoder_idList,
                                               batch_arcgis_geocoder_labelList,
                                               batch_arcgis_geocoder_typeList,
                                               batch_arcgis_geocoder_placeholderList,
                                               batch_arcgis_geocoder_jsList,
                                               batch_arcgis_geocoder_reqList]


"""
#--------------------------------------------------------------------------
#   arcGIS get batch coords forms
#--------------------------------------------------------------------------
"""
arcgis_geocode_help                 =   "https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.geocoding.html#batch-geocode"

batch_arcgis_query_title            =   "arcGIS Geocoder Get Batch Coordinates"
batch_arcgis_query_id               =   "arcgisbatchquery"

batch_arcgis_query_idList           =    ["bagdataframe",
                                          "bagaddrcomps",
                                          "baqcolumnname",
                                          "baqsaveaddress",
                                          "baqsourcecountry",
                                          "baqcategory",
                                          "baqoutsr",
                                          "baqbatchsize",
                                          "baqscore",
                                          "baqbulknumberlimit",
                                          "baqbulkfailurelimit",
                                          None,None,None,None]

batch_arcgis_query_labelList        =   ["dataframe_to_geocode",
                                         "dataframe_address_columns",
                                         "new_dataframe_lat_long_column_name(s)",
                                         "save_geocoder_full_address_column_name",
                                         "source_country",
                                         "category",
                                         "out_sr",
                                         "batch_size",
                                         "score",
                                         "max_addresses_to_geocode",
                                         "failure_limit_pct",
                                         "Get</br> Bulk Coords",
                                         "Clear","Return","Help"]


batch_arcgis_query_typeList         =   ["select",maketextarea(4),"text", "text","select",
                                         "select","text","text","text","text","text",
                                         "button","button","button","button"]

batch_arcgis_query_placeholderList  =   ["dataframe to geocode",
                                         "select from 'Column Names' for aggregate address : constant value use '+ Buffalo'",
                                         "Latitude,Longitude - stored as 2 columns  - [Latitude,Longitude] stored as one col",
                                         "retrieve aggregate address and store in column name (default = None - don't retrieve and save)",
                                         "source country (default - US)",
                                         "category (defailt - None)",
                                         "The (WKID) spatial reference of the x/y coordinates returned by a geocode request (default - None)",
                                         "batch size (default - geocoder recommended value)",
                                         "address match score threshold (0-100)  (default - 85%)",
                                         "max number of dataframe rows (default - all dataframe rows)",
                                         "failure limit (default - 5%)",
                                         None,None,None,None]

batch_arcgis_query_jsList           =   [None,None,None,None,None,None,None,None,None,None,None,
                                         "process_geocoding_callback(" + str(sugm.ArcGISId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                         "clear_geocode_form(" + str(sugm.ArcGISId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                         "geocode_return()",
                                         "displayhelp('" + arcgis_geocode_help + "')"]

batch_arcgis_query_reqList          =   [0,1,2,3,4,5,6]

batch_arcgis_query_form             =   [batch_arcgis_query_id,
                                         batch_arcgis_query_idList,
                                         batch_arcgis_query_labelList,
                                         batch_arcgis_query_typeList,
                                         batch_arcgis_query_placeholderList,
                                         batch_arcgis_query_jsList,
                                         batch_arcgis_query_reqList]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    bing bulk forms 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    bing bulk geocoder form
#--------------------------------------------------------------------------
"""
bing_bulk_geocoder_title                 =   "Bing Bulk Geocoder Connector"
bing_bulk_geocoder_id                    =   "bingbulkgeocoder"

bing_bulk_geocoder_idList                =    ["bingapikey",
                                               "bingagent",
                                               "bingtimeout",
                                               "bingfstring",
                                               "bingscheme",
                                               "bingproxies",
                                               None,None,None,None,None,None,None]

bing_bulk_geocoder_labelList             =   ["api_key",
                                               "user_agent",
                                               "timeout",
                                               "format_string",
                                               "scheme",
                                               "proxies",
                                               "Test</br>Geocoder</br>Connection",
                                               "Bulk</br>Geocoding",
                                               "Bulk</br>Reverse</br>Geocoding",
                                               "Bulk</br>Geocoding</br>Tuning",
                                               "Clear","Return","Help"]


bing_bulk_geocoder_typeList              =   ["text","text","text","text","text","text",
                                              "button","button","button","button","button","button","button"]

bing_bulk_geocoder_placeholderList       =   ["enter Bing api key",
                                              "user agent (default - my-application)",
                                              "enter timeout in seconds (default 20)",
                                              "enter format string (default %s)",
                                              "enter scheme (default https)",
                                              "proxies dict (default None)",
                                              None,None,None,None,None,None,None]

bing_bulk_geocoder_jsList                 =   [None,None,None,None,None,None,
                                              "test_geocoder(" + str(sugm.BingId) + "," + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.QUERY) + ","  + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.REVERSE) + ","  + str(sugm.BULK) + ")",
                                              "display_geocoders(" + str(sugm.BingId) + "," + str(sugm.BULK_TUNING) + ")",
                                              "clear_geocode_form(" + str(sugm.BingId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                              "geocode_return()",
                                               "displayhelp('" + str(dfchelp.BingInitHelp) + "')"]

bing_bulk_geocoder_reqList               =   [0]

bing_bulk_geocoder_form                  =   [bing_bulk_geocoder_id,
                                              bing_bulk_geocoder_idList,
                                              bing_bulk_geocoder_labelList,
                                              bing_bulk_geocoder_typeList,
                                              bing_bulk_geocoder_placeholderList,
                                              bing_bulk_geocoder_jsList,
                                              bing_bulk_geocoder_reqList]

"""
#--------------------------------------------------------------------------
#    bing bulk query form
#--------------------------------------------------------------------------
"""
bulk_bing_query_input_title               =   "Bing Bulk Geoocoding Parameters"
bulk_bing_query_input_id                  =   "bingbulkquery"
bulk_bing_query_input_idList              =   ["bbgdataframe",
                                               "bbqaddress",
                                               "bbqcolumnname",
                                               "bbqsaveaddress",
                                               "bbquserloc",
                                               "bbqculture",
                                               "bbqneighborhood",
                                               "bbqcountrycode",
                                               "bbqbulknumberlimit",
                                               "bbqbulkfailurelimit",
                                               "bbqbulkcheckpoint",
                                               None,None,None,None,None]

bulk_bing_query_input_labelList           =   ["dataframe_to_geocode",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "save_geocoder_full_address_column_name",
                                               "user_location",
                                               "culture",
                                               "include_neighborhood",
                                               "include_country_code",
                                               "max_addresses_to_geocode",
                                               "failure_limit",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Coords",
                                               "Bulk </br>Reverse</br>Geocoding",
                                               "Clear","Return","Help"]

bulk_bing_query_input_typeList            =   ["select",maketextarea(4),"select","text","text",
                                               "select","select","select","text","text","text",
                                               "button","button","button","button","button"]

bulk_bing_query_input_placeholderList     =  ["dataframe to geocode",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "Latitude,Longitude - stored as 2 columns  - [Latitude,Longitude] stored as one col",
                                              "full address column name (default = None - don't retrieve full address and save)",
                                              "prioritize result closest to user_location [lat,lng] (default - None)",
                                              "culture (default - US)",
                                              "include neighborhood in response (default - False)",
                                              "include country code in response (default - False)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "failure limit (default - 5%)",
                                              "checkpoint interval (default - every 10,000 rows)",
                                               None,None,None,None,None]

bulk_bing_query_input_jsList              =   [None,None,None,None,None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.BingId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "displayhelp('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_bing_query_input_reqList             =   [0,1,2]

bulk_bing_query_input_form                =   [bulk_bing_query_input_id,
                                               bulk_bing_query_input_idList,
                                               bulk_bing_query_input_labelList,
                                               bulk_bing_query_input_typeList,
                                               bulk_bing_query_input_placeholderList,
                                               bulk_bing_query_input_jsList,
                                               bulk_bing_query_input_reqList]  

"""
#--------------------------------------------------------------------------
#    bing bulk reverse form
#--------------------------------------------------------------------------
"""
bulk_bing_reverse_input_title             =   "Bing Bulk Geoocoding Parameters"
bulk_bing_reverse_input_id                =   "bingbulkreverse"
bulk_bing_reverse_input_idList            =   ["bbrdataframe",
                                               "bbrcolumnname",
                                               "bbrculture",
                                               "bbrcountrycode",
                                               "bbrbulknumberlimit",
                                               "bbrbulkfailurelimit",
                                               "bbrbulkcheckpoint",
                                               None,None,None,None,None]

bulk_bing_reverse_input_labelList         =   ["dataframe_to_geocode",
                                               "dataframe_lat_long_column_name(s)",
                                               "culture",
                                               "include_country_code",
                                               "max_lat_longs",
                                               "failure_limit",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Addresses",
                                               "Bulk </br>Geocoding",
                                               "Clear","Return","Help"]

bulk_bing_reverse_input_typeList          =   ["select",maketextarea(2),
                                               "select","select","text","text","text",
                                               "button","button","button","button","button"]

bulk_bing_reverse_input_placeholderList   =  ["dataframe to geocode",
                                              "lat long colname(s) - latitudfe, longitude - 2 cols [latcolname,longcolname] - 1 col",
                                              "culture (default - US)",
                                              "include country code in response (default - False)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "failure limit (default - 5%)",
                                              "checkpoint interval (default - every 10,000 rows)",
                                               None,None,None,None,None]

bulk_bing_reverse_input_jsList            =   [None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.BingId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.BingId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "displayhelp('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_bing_reverse_input_reqList           =   [0,1,2]

bulk_bing_reverse_input_form              =   [bulk_bing_reverse_input_id,
                                               bulk_bing_reverse_input_idList,
                                               bulk_bing_reverse_input_labelList,
                                               bulk_bing_reverse_input_typeList,
                                               bulk_bing_reverse_input_placeholderList,
                                               bulk_bing_reverse_input_jsList,
                                               bulk_bing_reverse_input_reqList]  


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Baidu bulk forms 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    bing bulk geocoder form
#--------------------------------------------------------------------------
"""
baidu_bulk_geocoder_title                =   "Baidu Bulk Geocoder Connector"
baidu_bulk_geocoder_id                   =   "baidubulkgeocoder"

baidu_bulk_geocoder_idList               =    ["baiduapikey",
                                               "baiduscheme",
                                               "baidutimeout",
                                               "baiduproxies",
                                               "baiduagent",
                                               "baidufstring",
                                               "baidssl",
                                               "baiduseckey",
                                               None,None,None,None,None,None,None]

baidu_bulk_geocoder_labelList            =   ["api_key",
                                              "scheme",
                                              "timeout",
                                              "proxies",
                                              "user_agent",
                                              "format_string",
                                              "ssl_context",
                                              "security_key", 
                                              "Test</br>Geocoder</br>Connection",
                                              "Bulk</br>Geocoding",
                                              "Bulk</br>Reverse</br>Geocoding",
                                              "Bulk</br>Geocoding</br>Tuning",
                                              "Clear","Return","Help"]


baidu_bulk_geocoder_typeList             =   ["text","text","text","text","text","text","text","text",
                                              "button","button","button","button","button","button","button"]

baidu_bulk_geocoder_placeholderList      =   ["enter Baidu api key",
                                              "enter scheme (default https)",
                                              "enter timeout in seconds (default 1)",
                                              "proxies dict (default None)",
                                              "user agent (default - 'geopy/x.xx.x')",
                                              "enter format string (default %s)",
                                              "enter ssl context (default None)",
                                              "enter authentication security key (default None)",
                                              None,None,None,None,None,None,None]

baidu_bulk_geocoder_jsList               =   [None,None,None,None,None,None,None,None,
                                              "test_geocoder(" + str(sugm.BaiduId) + "," + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.QUERY) + ","  + str(sugm.BULK) + ")",
                                              "display_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.REVERSE) + ","  + str(sugm.BULK) + ")",
                                              "display_geocoders(" + str(sugm.BaiduId) + "," + str(sugm.BULK_TUNING) + ")",
                                              "clear_geocode_form(" + str(sugm.BaiduId) + "," + str(sugm.GEOCODER) + "," + str(sugm.BULK) + ")",
                                              "geocode_return()",
                                               "displayhelp('" + str(dfchelp.BingInitHelp) + "')"]

baidu_bulk_geocoder_reqList              =   [0]

baidu_bulk_geocoder_form                 =   [baidu_bulk_geocoder_id,
                                              baidu_bulk_geocoder_idList,
                                              baidu_bulk_geocoder_labelList,
                                              baidu_bulk_geocoder_typeList,
                                              baidu_bulk_geocoder_placeholderList,
                                              baidu_bulk_geocoder_jsList,
                                              baidu_bulk_geocoder_reqList]


"""
#--------------------------------------------------------------------------
#    baidu bulk query form
#--------------------------------------------------------------------------
"""
bulk_baidu_query_input_title              =   "Baidu Bulk Geoocoding Parameters"
bulk_baidu_query_input_id                 =   "baidubulkquery"
bulk_baidu_query_input_idList             =   ["baiduqdataframe",
                                               "baiduqaddress",
                                               "baiduqcolumnname",
                                               "baiduqsaveaddress",
                                               "baiduqbulknumberlimit",
                                               "baiduqbulkfailurelimit",
                                               "baiduqbulkcheckpoint",
                                               None,None,None,None,None]

bulk_baidu_query_input_labelList          =   ["dataframe_to_geocode",
                                               "dataframe_address_columns",
                                               "new_dataframe_lat_long_column_name(s)",
                                               "save_geocoder_full_address_column_name",
                                               "max_addresses_to_geocode",
                                               "failure_limit",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Coords",
                                               "Bulk </br>Reverse</br>Geocoding",
                                               "Clear","Return","Help"]

bulk_baidu_query_input_typeList           =   ["select",maketextarea(4),"text","text","text","text","text",
                                               "button","button","button","button","button"]

bulk_baidu_query_input_placeholderList    =  ["dataframe to geocode",
                                              "select from 'Column Names' for aggregate address : constant value ie .. + Cleveland",
                                              "colname stored as [lat,long] - [latcolname,longcolname] stored as two cols",
                                              "full address column name (default = None - don't retrieve full address and save)",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "failure limit (default - 5%)",
                                              "checkpoint interval (default - every 10,000 rows)",
                                               None,None,None,None,None]

bulk_baidu_query_input_jsList             =   [None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.BaiduId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "displayhelp('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_baidu_query_input_reqList            =   [0,1,2]

bulk_baidu_query_input_form               =   [bulk_baidu_query_input_id,
                                               bulk_baidu_query_input_idList,
                                               bulk_baidu_query_input_labelList,
                                               bulk_baidu_query_input_typeList,
                                               bulk_baidu_query_input_placeholderList,
                                               bulk_baidu_query_input_jsList,
                                               bulk_baidu_query_input_reqList]  

"""
#--------------------------------------------------------------------------
#    bing bulk reverse form
#--------------------------------------------------------------------------
"""
bulk_baidu_reverse_input_title            =   "Baidu Bulk Geoocoding Parameters"
bulk_baidu_reverse_input_id               =   "baidubulkreverse"
bulk_baidu_reverse_input_idList           =   ["baidurdataframe",
                                               "baidurcolumnname",
                                               "baidurbulknumberlimit",
                                               "baidurbulkfailurelimit",
                                               "baidurbulkcheckpoint",
                                               None,None,None,None,None]

bulk_baidu_reverse_input_labelList        =   ["dataframe_to_geocode",
                                               "dataframe_lat_long_column_name(s)",
                                               "max_lat_longs",
                                               "failure_limit",
                                               "checkpoint_interval",
                                               "Get</br> Bulk </br>Addresses",
                                               "Bulk </br>Geocoding",
                                               "Clear","Return","Help"]

bulk_baidu_reverse_input_typeList         =   ["select",maketextarea(2),"text","text","text",
                                               "button","button","button","button","button"]

bulk_baidu_reverse_input_placeholderList  =  ["dataframe to geocode",
                                              "lat long colname(s) - [latcolname,longcolname] read from two cols",
                                              "number of addresses to get coords for (default - len(dataframe))",
                                              "failure limit (default - 5%)",
                                              "checkpoint interval (default - every 10,000 rows)",
                                               None,None,None,None,None]

bulk_baidu_reverse_input_jsList           =   [None,None,None,None,None,None,None,
                                               "process_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "display_geocoding_callback(" + str(sugm.BaiduId) + "," + str(sugm.QUERY) + "," + str(sugm.BULK) + ")",
                                               "clear_geocode_form(" + str(sugm.BaiduId) + "," + str(sugm.REVERSE) + "," + str(sugm.BULK) + ")",
                                               "geocode_return()",
                                               "displayhelp('" + str(dfchelp.GoogleQueryHelp) + "')"]

bulk_baidu_reverse_input_reqList          =   [0,1,2]

bulk_baidu_reverse_input_form             =   [bulk_bing_reverse_input_id,
                                               bulk_bing_reverse_input_idList,
                                               bulk_bing_reverse_input_labelList,
                                               bulk_bing_reverse_input_typeList,
                                               bulk_bing_reverse_input_placeholderList,
                                               bulk_bing_reverse_input_jsList,
                                               bulk_bing_reverse_input_reqList]  


SWUtility_bulk_geocode_inputs             =   [google_bulk_geocoder_id, bulk_google_query_input_id, bulk_google_reverse_input_id,
                                               batch_arcgis_geocoder_id, batch_arcgis_query_id, bing_bulk_geocoder_id, bulk_bing_query_input_id,
                                               bulk_bing_reverse_input_id, baidu_bulk_geocoder_id, bulk_baidu_query_input_id, bulk_baidu_reverse_input_id]
                                 

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   geocoding bulk display methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#  bulk geocode tables 
#--------------------------------------------------------------------------
"""
def get_languages_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of languages
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    languagesHeader      =   [""]
    languagesRows        =   []
    languagesWidths      =   [100]
    languagesAligns      =   ["left"]
    languagesHrefs       =   []


    from dfcleanser.sw_utilities.sw_utility_model import get_Dict
    langdict    =   get_Dict("Language_Codes")
    languages   =   list(langdict.keys())
    languages.sort()
    
    for i in range(len(languages)) :
        
        languagesrow = [languages[i]]
        languagesRows.append(languagesrow)
        languagesHrefs.append([callback])
        
    languages_table = None
                
    languages_table = dcTable("Languages",tableid,owner,
                              languagesHeader,languagesRows,
                              languagesWidths,languagesAligns)
            
    languages_table.set_refList(languagesHrefs)
    
    languages_table.set_small(True)
    languages_table.set_smallwidth(98)
    languages_table.set_smallmargin(10)

    languages_table.set_border(True)
        
    languages_table.set_checkLength(True)
            
    languages_table.set_textLength(26)
    languages_table.set_html_only(True) 
    
    languages_table.set_tabletype(ROW_MAJOR)
    languages_table.set_rowspertable(20)

    listHtml = get_row_major_table(languages_table,SCROLL_DOWN,False)

    return(listHtml)


def get_regions_table(tableid,owner,callback,countriesFlag=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of regions
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    regionsHeader      =   [""]
    regionsRows        =   []
    regionsWidths      =   [100]
    regionsAligns      =   ["left"]
    regionsHrefs       =   []


    from dfcleanser.sw_utilities.sw_utility_model import get_Dict
    regionsdict     =   get_Dict("Country_Codes")
    regions         =   list(regionsdict.keys())
    regions.sort()
    
    for i in range(len(regions)) :
        
        regionsrow = [regions[i]]
        regionsRows.append(regionsrow)
        regionsHrefs.append([callback])
        
    regions_table = None
    
    if(countriesFlag) :
        ttitle  =   "Countries" 
    else :
        ttitle  =   "Regions" 
          
    regions_table = dcTable(ttitle,tableid,owner,
                             regionsHeader,regionsRows,
                             regionsWidths,regionsAligns)
            
    regions_table.set_refList(regionsHrefs)
    
    regions_table.set_small(True)
    regions_table.set_smallwidth(98)
    regions_table.set_smallmargin(10)

    regions_table.set_border(True)
        
    regions_table.set_checkLength(True)
            
    regions_table.set_textLength(26)
    regions_table.set_html_only(True) 
    
    regions_table.set_tabletype(ROW_MAJOR)
    regions_table.set_rowspertable(20)

    listHtml = get_row_major_table(regions_table,SCROLL_DOWN,False)

    return(listHtml)


def get_categories_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of catefories
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    categoriesHeader      =   [""]
    categoriesRows        =   []
    categoriesWidths      =   [100]
    categoriesAligns      =   ["left"]
    categoriesHrefs       =   []


    from dfcleanser.sw_utilities.sw_utility_model import get_Dict
    regionsdict     =   get_Dict("Language_Codes")
    categories      =   list(regionsdict.keys())
    categories.sort()
    
    for i in range(len(categories)) :
        
        categoriesrow = [categories[i]]
        categoriesRows.append(categoriesrow)
        categoriesHrefs.append([callback])
        
    categories_table = None
                
    categories_table = dcTable("Categories",tableid,owner,
                               categoriesHeader,categoriesRows,
                               categoriesWidths,categoriesAligns)
            
    categories_table.set_refList(categoriesHrefs)
    
    categories_table.set_small(True)
    categories_table.set_smallwidth(98)
    categories_table.set_smallmargin(10)

    categories_table.set_border(True)
        
    categories_table.set_checkLength(True)
            
    categories_table.set_textLength(26)
    categories_table.set_html_only(True) 
    
    categories_table.set_tabletype(ROW_MAJOR)
    categories_table.set_rowspertable(20)

    listHtml = get_row_major_table(categories_table,SCROLL_DOWN,False)
        
    return(listHtml)


def get_address_components_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of catefories
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    addrcompsHeader       =   [""]
    addrcompsRows         =   []
    addrcompsWidths       =   [100]
    addrcompsAligns       =   ["left"]
    addrcompsHrefs        =   []

    from dfcleanser.sw_utilities.sw_utility_model import get_List
    acomplist       =   get_List("Address_Components")
    addrcomplist    =   ["full_address"]
    
    for i in range(len(acomplist)) :
        addrcomplist.append(acomplist[i])    

    for i in range(len(addrcomplist)) :
        
        addrcompsrow = [addrcomplist[i]]
        addrcompsRows.append(addrcompsrow)
        addrcompsHrefs.append([callback])
        
    addrcomps_table = None
                
    addrcomps_table = dcTable("Address Components",tableid,owner,
                               addrcompsHeader,addrcompsRows,
                               addrcompsWidths,addrcompsAligns)
            
    addrcomps_table.set_refList(addrcompsHrefs)
    
    addrcomps_table.set_small(True)
    addrcomps_table.set_smallwidth(98)
    addrcomps_table.set_smallmargin(10)

    addrcomps_table.set_border(True)
        
    addrcomps_table.set_checkLength(True)
            
    addrcomps_table.set_textLength(32)
    addrcomps_table.set_html_only(True) 
    
    addrcomps_table.set_tabletype(ROW_MAJOR)
    addrcomps_table.set_rowspertable(20)

    listHtml = get_row_major_table(addrcomps_table,SCROLL_DOWN,False)

    return(listHtml)


def get_result_types_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of catefories
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    restypesHeader        =   [""]
    restypesRows          =   []
    restypesWidths        =   [100]
    restypesAligns        =   ["left"]
    restypesHrefs         =   []


    for i in range(10) :
        
        restypesrow = [str(i)]
        restypesRows.append(restypesrow)
        restypesHrefs.append([callback])
        
    restypes_table = None
                
    restypes_table = dcTable("result types",tableid,owner,
                             restypesHeader,restypesRows,
                             restypesWidths,restypesAligns)
            
    restypes_table.set_refList(restypesHrefs)
    
    restypes_table.set_small(True)
    restypes_table.set_smallwidth(98)
    restypes_table.set_smallmargin(10)

    restypes_table.set_border(True)
        
    restypes_table.set_checkLength(True)
            
    restypes_table.set_textLength(22)
    restypes_table.set_html_only(True) 
    
    restypes_table.set_tabletype(ROW_MAJOR)
    restypes_table.set_rowspertable(20)

    listHtml = get_row_major_table(restypes_table,SCROLL_DOWN,False)
        
    return(listHtml)


def get_location_types_table(tableid,owner,callback) :
    """
    * -------------------------------------------------------------------------- 
    * function : get table of catefories
    * 
    * parms :
    *  tableid  - html table identifier
    *  owner    - table owner
    *  callback - javascript callback
    *
    * returns : 
    *  table html
    * --------------------------------------------------------
    """

    loctypesHeader        =   [""]
    loctypesRows          =   []
    loctypesWidths        =   [100]
    loctypesAligns        =   ["left"]
    loctypesHrefs         =   []

    from dfcleanser.sw_utilities.sw_utility_model import get_List
    loctypeslist    =   get_List("Location_Types")

    for i in range(len(loctypeslist)) :
        
        loctypesrow = [loctypeslist[i]]
        loctypesRows.append(loctypesrow)
        loctypesHrefs.append([callback])
        
    loctypes_table = None
                
    loctypes_table = dcTable("Location Types",tableid,owner,
                             loctypesHeader,loctypesRows,
                             loctypesWidths,loctypesAligns)
            
    loctypes_table.set_refList(loctypesHrefs)
    
    loctypes_table.set_small(True)
    loctypes_table.set_smallwidth(98)
    loctypes_table.set_smallmargin(10)

    loctypes_table.set_border(True)
        
    loctypes_table.set_checkLength(True)
            
    loctypes_table.set_textLength(22)
    loctypes_table.set_html_only(True) 
    
    loctypes_table.set_tabletype(ROW_MAJOR)
    loctypes_table.set_rowspertable(20)

    listHtml = get_row_major_table(loctypes_table,SCROLL_DOWN,False)

    return(listHtml)




"""
#--------------------------------------------------------------------------
#  bulk geocode display methods
#--------------------------------------------------------------------------
"""
def display_bulk_geocode_inputs(geocid,geotype,tabletype=sugm.COLNAMES_TABLE,showfull=False) :
    """
    * --------------------------------------------------------- 
    * function : display the input form for geoocoding
    * 
    * parms :
    *  geocid       - geocode identiifier
    *  geotype      - geocode command type   
    *  tabletype    - html table identifier
    *  showfull     - show full parm list flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(geocid == None) :
        geocid = cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocid == None) :
            geocid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocid,True)
    
    if (geotype == sugm.QUERY) :
        if(tabletype==sugm.GEOCODERS_TABLE) :
            geo_parms_html = sugw.get_geocoder_table(True) 
            
        elif(tabletype==sugm.COLNAMES_TABLE) :
            
            df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
            
            from dfcleanser.common.display_utils import get_df_col_names_table
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_df_col_names_table(df,"gegdfcolnamesTable",cfg.SWGeocodeUtility_ID,"bg_add_df_column",str(sugm.GoogleId) + "," + str(sugm.QUERY))
            elif(geocid == sugm.ArcGISId) :  
                geo_parms_html = get_df_col_names_table(df,"geadfcolnamesTable",cfg.SWGeocodeUtility_ID,"bg_add_df_column",str(sugm.ArcGISId) + "," + str(sugm.QUERY))
            elif(geocid == sugm.BingId) :
                geo_parms_html = get_df_col_names_table(df,"geadfcolnamesTable",cfg.SWGeocodeUtility_ID,"bg_add_df_column",str(sugm.BingId) + "," + str(sugm.QUERY))
            elif(geocid == sugm.BaiduId) :
                geo_parms_html = get_df_col_names_table(df,"geadfcolnamesTable",cfg.SWGeocodeUtility_ID,"bg_add_df_column",str(sugm.BaiduId) + "," + str(sugm.QUERY))
                
        elif(tabletype==sugm.LANGUAGE_TABLE) :
            geo_parms_html = get_languages_table("gedflanguagesTable",cfg.SWGeocodeUtility_ID,"gb_select_language")
            
        elif(tabletype==sugm.REGION_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_regions_table("gegdfregionsTable",cfg.SWGeocodeUtility_ID,"gb_select_region")
            else :
                geo_parms_html = get_regions_table("geadfregionsTable",cfg.SWGeocodeUtility_ID,"gb_select_country",True)
        
        elif(tabletype==sugm.LOCATION_TYPES_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_location_types_table("gegdfltypesTable",cfg.SWGeocodeUtility_ID,"gbr_add_location_type")
                
        else :
            geo_parms_html = get_categories_table("gedfregionsTable",cfg.SWGeocodeUtility_ID,"gb_select_category")

        # get the correct input form            
        if(geocid == sugm.GoogleId) :
            if(tabletype==sugm.COLNAMES_TABLE) :
                form    =   bulk_google_query_input_form
            else :
                form    =   [bulk_google_query_input_id,
                             bulk_google_query_input_idList,
                             bulk_google_query_ltypes_input_labelList,
                             bulk_google_query_input_typeList,
                             bulk_google_query_input_placeholderList,
                             bulk_google_query_ltypes_input_jsList,
                             bulk_google_query_input_reqList]  
                
        elif(geocid == sugm.ArcGISId) :
            form    =   batch_arcgis_query_form
            inparms     =   cfg.get_config_value(batch_arcgis_query_id+"Parms")
            if(not (inparms is None)) :
                inparms[7]  =   str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))
            else :
                inparms     =   ["","","","","","","","","","",""]
                inparms[7]  =   str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))
                
            cfg.set_config_value(batch_arcgis_query_id+"Parms",inparms)
            
        elif(geocid == sugm.BingId) :
            form    =   bulk_bing_query_input_form
        
        elif(geocid == sugm.BaiduId) :
            form    =   bulk_baidu_query_input_form
            
    else :
        
        if(tabletype==sugm.GEOCODERS_TABLE) :
            from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_geocoder_table
            geo_parms_html = get_geocoder_table(True) 
        
        elif(tabletype==sugm.COLNAMES_TABLE) :
            
            df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
            
            from dfcleanser.common.display_utils import get_df_col_names_table
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_df_col_names_table(df,"gegdfcolnamesTable",cfg.SWGeocodeUtility_ID,"bg_add_df_column",str(sugm.GoogleId) + "," + str(sugm.REVERSE))
            elif(geocid == sugm.BingId) :
                geo_parms_html = get_df_col_names_table(df,"geadfcolnamesTable",cfg.SWGeocodeUtility_ID,"bg_add_df_column",str(sugm.BingId) + "," + str(sugm.REVERSE))
            
        elif(tabletype==sugm.ADDRESS_COMPONENTS_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_address_components_table("graddrcompsTable",cfg.SWGeocodeUtility_ID,"gbr_google_add_addrcomp")
        
        elif(tabletype==sugm.RESULT_TYPES_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_result_types_table("grresulttypesTable",cfg.SWGeocodeUtility_ID,"gbr_add_result_type")
                
        elif(tabletype==sugm.LOCATION_TYPES_TABLE) :
            if(geocid == sugm.GoogleId) :
                geo_parms_html = get_location_types_table("grlocationtypesTable",cfg.SWGeocodeUtility_ID,"gbr_add_location_type")
            
        elif(tabletype==sugm.LANGUAGE_TABLE) :
            geo_parms_html = get_languages_table("gedflanguagesTable",cfg.SWGeocodeUtility_ID,"gbr_select_language")

        else :
            from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_geocoder_parms_table
            geo_parms_html = get_geocoder_parms_table(geocid)


        # get the correct input form            
        if(geocid == sugm.GoogleId) :
            form    =   bulk_google_reverse_input_form
        elif(geocid == sugm.BingId) :
            form    =   bulk_bing_reverse_input_form
        elif(geocid == sugm.BaiduId) :
            form    =   bulk_baidu_reverse_input_form
            

    # build the input form
    from dfcleanser.common.html_widgets import InputForm
    geofunc_input_form = InputForm(form[0],
                                   form[1],
                                   form[2],
                                   form[3],
                                   form[4],
                                   form[5],
                                   form[6])
    
    # add select true false lists
    if (geotype == sugm.QUERY) :
        
        selectDicts     =   []
        from dfcleanser.sw_utilities.sw_utility_model import get_Dict
        
        geofunc_input_form.set_gridwidth(680)
        
        if(geocid == sugm.ArcGISId) :
            geofunc_input_form.set_custombwidth(120)
        elif(geocid == sugm.BingId) :
            geofunc_input_form.set_custombwidth(120)
        elif(geocid == sugm.BaiduId) :
            geofunc_input_form.set_custombwidth(120)
        else :
            geofunc_input_form.set_custombwidth(92)
            
        geofunc_input_form.set_fullparms(True) 
        
        if(geocid == sugm.GoogleId) :
            
            
            df_list     =   cfg.get_dfc_dataframes_titles_list()
            default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            
            dataframes  =   {"default" : default_df,
                             "list" : df_list,
                             "callback" : "change_bulk_df"}
            selectDicts.append(dataframes)
            
            savecoords      =   {"default" : "Latitude,Longitude",
                                 "list" : ["Latitude,Longitude","[Latitude,Longitude]"]}
            selectDicts.append(savecoords)
            
            regions             =   {}
            regions.update({"default": "United States"})

            regionsdict     =   get_Dict("Country_Codes")
            regionslist     =   list(regionsdict.keys())
            regionslist.sort()
            regions.update({"list":regionslist})
            selectDicts.append(regions)

            languages       =   {}
            languages.update({"default": "English"})
            
            langdict        =   get_Dict("Language_Codes")
            languageslist   =   list(langdict.keys())
            languageslist.sort()
            languages.update({"list":languageslist})
            selectDicts.append(languages)
            
            saveloctype     =   {"default" : "False",
                                 "list" : ["True","False"]}
            selectDicts.append(saveloctype)
           
            get_select_defaults(geofunc_input_form,
                                bulk_google_query_input_id,
                                bulk_google_query_input_idList,
                                bulk_google_query_input_typeList,
                                selectDicts)
            
        elif(geocid == sugm.ArcGISId) :
            
            df_list     =   cfg.get_dfc_dataframes_titles_list()
            default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            
            dataframes  =   {"default" : default_df,
                             "list" : df_list,
                             "callback" : "change_bulk_df"}
            selectDicts.append(dataframes)

            regions             =   {}
            regions.update({"default": "United States"})

            regionsdict     =   get_Dict("Country_Codes")
            regionslist     =   list(regionsdict.keys())
            regionslist.sort()
            regions.update({"list":regionslist})
            selectDicts.append(regions)
            
            categories       =   {}
            categories.update({"default": "Address"})
            catdict         =   get_Dict("ArcGIS_Categories")
            catslist        =   list(catdict.keys())
            catslist.sort()
            categories.update({"list":catslist})
            selectDicts.append(categories)
            
            get_select_defaults(geofunc_input_form,
                                batch_arcgis_query_id,
                                batch_arcgis_query_idList,
                                batch_arcgis_query_typeList,
                                selectDicts)

        elif(geocid == sugm.BingId) :
            
            df_list     =   cfg.get_dfc_dataframes_titles_list()
            default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            
            dataframes  =   {"default" : default_df,
                             "list" : df_list,
                             "callback" : "change_bulk_df"}
            selectDicts.append(dataframes)
            
            savecoords      =   {"default" : "Latitude,Longitude - 2 columns",
                                 "list" : ["Latitude,Longitude - 2 columns","[Latitude,Longitude] - 1 column"]}
            selectDicts.append(savecoords)
            
            countries       =   {}
            countries.update({"default": "United States"})
            
            countrydict     =   get_Dict("Country_Codes")
            countrylist     =   list(countrydict.keys())
            countrylist.sort()
            countries.update({"list":countrylist})
            selectDicts.append(countries)
 
            includecomp     =   {"default" : "False",
                                 "list" : ["True","False"]}
            selectDicts.append(includecomp)
            selectDicts.append(includecomp)
           
            get_select_defaults(geofunc_input_form,
                                bulk_bing_query_input_id,
                                bulk_bing_query_input_idList,
                                bulk_bing_query_input_typeList,
                                selectDicts)
        
        elif(geocid == sugm.BaiduId) :
            
            df_list     =   cfg.get_dfc_dataframes_titles_list()
            default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            
            dataframes  =   {"default" : default_df,
                             "list" : df_list,
                             "callback" : "change_bulk_df"}
            selectDicts.append(dataframes)
            
            get_select_defaults(geofunc_input_form,
                                bulk_baidu_query_input_id,
                                bulk_baidu_query_input_idList,
                                bulk_baidu_query_input_typeList,
                                selectDicts)


    # bulk reverse   
    else :
        
        selectDicts     =   []
        from dfcleanser.sw_utilities.sw_utility_model import get_Dict
        
        geofunc_input_form.set_gridwidth(680)
        
        if(geocid == sugm.GoogleId) :
            geofunc_input_form.set_custombwidth(90)
        else :
            geofunc_input_form.set_custombwidth(120)
            
        geofunc_input_form.set_fullparms(True)
        
        if(geocid == sugm.GoogleId) :
            
            df_list     =   cfg.get_dfc_dataframes_titles_list()
            default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            
            dataframes  =   {"default" : default_df,
                             "list" : df_list,
                             "callback" : "change_bulk_reverse_df"}
            selectDicts.append(dataframes)

            lengthFlag      =   {"default":"short","list":["short","long"]}
            selectDicts.append(lengthFlag)
            
            languages       =   {}
            languages.update({"default": "English"})

            langdict        =   get_Dict("Language_Codes")
            languageslist   =   list(langdict.keys())
            languageslist.sort()
            languages.update({"list":languageslist})
            selectDicts.append(languages)
            
            get_select_defaults(geofunc_input_form,
                                bulk_google_reverse_input_id,
                                bulk_google_reverse_input_idList,
                                bulk_google_reverse_input_typeList,
                                selectDicts)
            
        elif(geocid == sugm.BingId) :
            
            df_list     =   cfg.get_dfc_dataframes_titles_list()
            default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            
            dataframes  =   {"default" : default_df,
                             "list" : df_list,
                             "callback" : "change_bulk_reverse_df"}
            selectDicts.append(dataframes)
            
            countries       =   {}
            countries.update({"default": "United States"})
            
            countrydict     =   get_Dict("Country_Codes")
            countrylist     =   list(countrydict.keys())
            countrylist.sort()
            countries.update({"list":countrylist})
            selectDicts.append(countries)
 
            includecomp     =   {"default" : "False",
                                 "list" : ["True","False"]}
            selectDicts.append(includecomp)
           
            get_select_defaults(geofunc_input_form,
                                bulk_bing_reverse_input_id,
                                bulk_bing_reverse_input_idList,
                                bulk_bing_reverse_input_typeList,
                                selectDicts)
            
        elif(geocid == sugm.BaiduId) :
            
            df_list     =   cfg.get_dfc_dataframes_titles_list()
            default_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            
            dataframes  =   {"default" : default_df,
                             "list" : df_list,
                             "callback" : "change_bulk_reverse_df"}
            selectDicts.append(dataframes)
            
            get_select_defaults(geofunc_input_form,
                                bulk_baidu_reverse_input_id,
                                bulk_baidu_reverse_input_idList,
                                bulk_baidu_reverse_input_typeList,
                                selectDicts)

    print("\n")
    
    geofunc_input_html = ""
    geofunc_input_html = geofunc_input_form.get_html()
    
    if (geotype == sugm.QUERY) :
        geofunc_heading_html    =   "<div>" + sugm.get_geocoder_title(geocid) + " Bulk Geocoding</div>"
    else :
        geofunc_heading_html    =   "<div>" + sugm.get_geocoder_title(geocid) + " Bulk Reverse Geocoding</div>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [geofunc_heading_html,geo_parms_html,geofunc_input_html]
   
    if(geotype == sugm.QUERY) : 
    
        display_generic_grid("geocode-query-wrapper",gridclasses,gridhtmls)

    else :
        
        display_generic_grid("geocode-query-wrapper",gridclasses,gridhtmls)
        

def display_bulk_geocoding(geocid,geotype) :
    """
    * -------------------------------------------------------------------------- 
    * function : display bulk geocoding input forms
    * 
    * parms :
    *  optionId  - identify get coords or get address
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat  =   opStatus()
    
    if(not (cfg.is_a_dfc_dataframe_loaded())) :
            
        sugw.display_geocode_main_taskbar() 
        opstat.set_status(False)
        opstat.set_errorMsg("No dataframe is imported which is required for bulk geoocoding  ")
        display_exception(opstat)
            
    else :
    
        if(geotype == sugm.QUERY) :
        
            cfg.set_config_value(cfg.BULK_GEOCODE_MODE_KEY,sugm.QUERY)
            
            if( not( geocid in sugm.supported_Bulk_Geocoders) ) :
                sugw.display_geocode_main_taskbar() 
                opstat.set_status(False)
                print("\n")
                opstat.set_errorMsg("Bulk geoocoding is not supported for the currently selected geocoder")
                display_exception(opstat)
                return()
                
            else :
                
                display_bulk_geocode_inputs(geocid,sugm.QUERY)    
                
        else :
            
            cfg.set_config_value(cfg.BULK_GEOCODE_MODE_KEY,sugm.REVERSE)            
            
            if( not( geocid in sugm.supported_Bulk_Reverses) ) :
                sugw.display_geocode_main_taskbar() 
                opstat.set_status(False)
                opstat.set_errorMsg("Bulk reverse geoocoding is not supported for the currently selected geocoder")
                print("\n")
                display_exception(opstat)
                return()
                
            else :
                
                display_bulk_geocode_inputs(geocid,sugm.REVERSE)    


def display_bulk_geocoders(geocodeid,showfull=False) :
    """
    * ---------------------------------------------------------
    * function : display bulk geocoder parm screens
    * 
    * parms :
    *
    *   geocodeid  -   geocoder id
    *   showfull   -   show all parms flag
    *    
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    cfg.display_data_select_df(cfg.SWGeocodeUtility_ID)
    print("\n")
    
    listHtml = sugw.get_geocoder_table(True)
    
    if(geocodeid == None) :
        geocodeid       =   cfg.get_config_value(cfg.CURRENT_GEOCODER_KEY)
        if(geocodeid == None) : 
            geocodeid = sugm.GoogleId
            cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,geocodeid,True)

    geocoder_input_form = None
    
    if( (geocodeid == None) or (geocodeid == sugm.GoogleId) ) :

        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.GoogleId,True)
        geocoder_input_form   =   [google_bulk_geocoder_id,
                                   google_bulk_geocoder_idList,
                                   google_bulk_geocoder_labelList,
                                   google_bulk_geocoder_typeList,
                                   google_bulk_geocoder_placeholderList,
                                   google_bulk_geocoder_jsList,
                                   google_bulk_geocoder_reqList]

    elif(geocodeid == sugm.BingId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.BingId,True)
        geocoder_input_form   =   [bing_bulk_geocoder_id,
                                   bing_bulk_geocoder_idList,
                                   bing_bulk_geocoder_labelList,
                                   bing_bulk_geocoder_typeList,
                                   bing_bulk_geocoder_placeholderList,
                                   bing_bulk_geocoder_jsList,
                                   bing_bulk_geocoder_reqList]
        
    elif(geocodeid == sugm.ArcGISId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.ArcGISId,True)
        geocoder_input_form   =   [batch_arcgis_geocoder_id,
                                   batch_arcgis_geocoder_idList,
                                   batch_arcgis_geocoder_labelList,
                                   batch_arcgis_geocoder_typeList,
                                   batch_arcgis_geocoder_placeholderList,
                                   batch_arcgis_geocoder_jsList,
                                   batch_arcgis_geocoder_reqList]
    
    elif(geocodeid == sugm.BaiduId) :
        
        cfg.set_config_value(cfg.CURRENT_GEOCODER_KEY,sugm.BaiduId,True)
        geocoder_input_form   =   [baidu_bulk_geocoder_id,
                                   baidu_bulk_geocoder_idList,
                                   baidu_bulk_geocoder_labelList,
                                   baidu_bulk_geocoder_typeList,
                                   baidu_bulk_geocoder_placeholderList,
                                   baidu_bulk_geocoder_jsList,
                                   baidu_bulk_geocoder_reqList]
        

    from dfcleanser.common.html_widgets import InputForm
    geocode_input_form = InputForm(geocoder_input_form[0],
                                   geocoder_input_form[1],
                                   geocoder_input_form[2],
                                   geocoder_input_form[3],
                                   geocoder_input_form[4],
                                   geocoder_input_form[5],
                                   geocoder_input_form[6])
    
    if(geocodeid == sugm.GoogleId) :
        
        selectDicts     =   []
        geocsel         =   {"default":"False","list":["True","False"]}
        selectDicts.append(geocsel)
           
        get_select_defaults(geocode_input_form,
                            geocoder_input_form[0],
                            geocoder_input_form[1],
                            geocoder_input_form[3],
                            selectDicts)
        
    elif(geocodeid == sugm.BingId) :
        
        selectDicts     =   []
        geocsel         =   {"default":"True","list":["True","False"]}
        selectDicts.append(geocsel)
        selectDicts.append(geocsel)
        
        get_select_defaults(geocode_input_form,
                            geocoder_input_form[0],
                            geocoder_input_form[1],
                            geocoder_input_form[3],
                            selectDicts)
    
    elif(geocodeid == sugm.BaiduId) :
        
        selectDicts     =   []
        geocsel         =   {"default":"True","list":["True","False"]}
        selectDicts.append(geocsel)
        selectDicts.append(geocsel)
        
        get_select_defaults(geocode_input_form,
                            geocoder_input_form[0],
                            geocoder_input_form[1],
                            geocoder_input_form[3],
                            selectDicts)
        
    geocode_input_form.set_gridwidth(720)
    geocode_input_form.set_custombwidth(90)
    
    if(showfull) :
        geocode_input_form.set_fullparms(True)
    
    geocode_input_html = ""
    geocode_input_html = geocode_input_form.get_html() 
    
    geocode_heading_html =   "<br><div>Bulk Geocoder Connector Parms - " + sugm.get_geocoder_title(geocodeid) + "</div><br>"

    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [geocode_heading_html,listHtml,geocode_input_html]
    
    display_generic_grid("geocode-connector-wrapper",gridclasses,gridhtmls)
    

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  bulk geocode input validation methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_bulk_input_parms(geocid,geotype,inputs) :
    
    if(geotype == sugm.QUERY) :
        if(geocid == sugm.GoogleId) :
            return(get_parms_for_input(inputs,bulk_google_query_input_idList))
        elif(geocid == sugm.BingId) :
            return(get_parms_for_input(inputs,bulk_bing_query_input_idList))
        elif(geocid == sugm.BaiduId) :
            return(get_parms_for_input(inputs,bulk_baidu_query_input_idList))
        else :
            return(get_parms_for_input(inputs,batch_arcgis_query_idList))

    else :
        if(geocid == sugm.GoogleId) :
            return(get_parms_for_input(inputs,bulk_google_reverse_input_idList))
        elif(geocid == sugm.BingId) :
            return(get_parms_for_input(inputs,bulk_bing_reverse_input_idList))
        elif(geocid == sugm.BaiduId) :
            return(get_parms_for_input(inputs,bulk_baidu_reverse_input_idList))


def validate_google_bulk_parms(geotype,inputs,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}

    if(geotype == sugm.QUERY) :
        
        fparms = get_parms_for_input(inputs,bulk_google_query_input_idList)

        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe selected defined")
        else :
                
            if(opstat.get_status()) :
                if(len(fparms[1]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dataframe address column name(s) defined")
                
            if(opstat.get_status()) :
                if(len(fparms[2]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dataframe lat lng column name(s) defined")

        if(opstat.get_status()) :
            
            df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                
            bulk_geocode_kwargs.update({bulk_google_query_input_labelList[0] : fparms[0]})
            bulk_geocode_kwargs.update({bulk_google_query_input_labelList[1] : fparms[1]})
            bulk_geocode_kwargs.update({bulk_google_query_input_labelList[2] : fparms[2]})
            
            cfg.set_config_value(cfg.CURRENT_GEOCODE_DF,fparms[0])
                
            if(len(fparms[3]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[3] : fparms[3]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[3] : "None"})
                
            if(len(fparms[4]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[4] : fparms[4]})    
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[4] : "None"}) 
                
            if(len(fparms[5]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[5] : fparms[5]}) 
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[5] : "en"})
                
            if(len(fparms[6]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[6] : fparms[6]}) 
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[6] : "ALL"})

            bulk_geocode_kwargs.update({bulk_google_query_input_labelList[7] : fparms[7]})
           
            if(len(fparms[8]) > 0) :
                if(int(fparms[8]) > len(df)) :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[8] : len(df)}) 
                else :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[8] : fparms[8]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[7] : len(df)}) 
                    
            if(len(fparms[9]) > 0) :
                if(int(fparms[9]) > 100) :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[9] : "2"}) 
                else :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[9] : fparms[9]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[9] : "2"}) 
            
            if(len(fparms[10]) > 0) :
                if(int(fparms[10]) < 0) :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[10] : "10000"}) 
                else :
                    bulk_geocode_kwargs.update({bulk_google_query_input_labelList[10] : fparms[10]})
            else :
                bulk_geocode_kwargs.update({bulk_google_query_input_labelList[10] : "10000"}) 
                    
    else :
                
        # check the required reverse parms
        fparms = get_parms_for_input(inputs,bulk_google_reverse_input_idList)
        
        if( (len(fparms[0]) == 0) and (len(fparms[1]) == 0) and (len(fparms[2]) == 0) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("No api key or client id and secret parm(s) defined")
        else :
                
            # check the required query parms 
            if(len(fparms[0]) == 0) :
                if( (len(fparms[1]) == 0) or (len(fparms[2]) == 0) ) :   
                    opstat.set_status(False)
                    opstat.set_errorMsg("No client id and secret parm(s) defined")
                        
            if(opstat.get_status()) :
                if(len(fparms[3]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No lat lng column name defined")
                
            if(opstat.get_status()) :
                if(len(fparms[4]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No address column name defined")
        
        # validate non required parmsd            
        if(opstat.get_status()) :
            
            df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[0] : fparms[0]})
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[1] : fparms[1]})
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[2] : fparms[2]})
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[3] : fparms[3]})
            bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[4] : fparms[4]})
                
            if(len(fparms[5]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[5] : fparms[5]})
            else :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[5] : ""})
                         
            if(len(fparms[6]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[6] : fparms[6]})
            else :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[6] : "short"})    
    
            if(len(fparms[7]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[7] : fparms[7]}) 
            else :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[7] : len(df)}) 
                
            if(len(fparms[8]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[8] : fparms[8]}) 
            else :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[8] : "2"})
                
            if(len(fparms[9]) > 0) :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[9] : fparms[9]}) 
            else :
                bulk_geocode_kwargs.update({bulk_google_reverse_input_labelList[9] : "10000"}) 
    
                
    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)


def validate_arcgis_bulk_parms(geotype,inputs,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    bulk_geocode_kwargs     =   {}
    
    if(geotype == sugm.QUERY) :

        fparms  =   get_parms_for_input(inputs,batch_arcgis_query_idList)  
        
        bulk_geocode_kwargs.update({batch_arcgis_query_labelList[0] : fparms[0]})
        
        # check the required parms 
        if(len(fparms[1]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No " + bulk_google_query_input_labelList[1] + " defined")
        else :
            bulk_geocode_kwargs.update({batch_arcgis_query_labelList[1] : fparms[1]})    
            if(len(fparms[2]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("No " + bulk_google_query_input_labelList[2] + " defined")
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[2] : fparms[2]})
                
        if(opstat.get_status()) :
            
            if(len(fparms[3]) > 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[3] : fparms[3]})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[3] : "None"})
            
            if(len(fparms[4]) > 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[4] : fparms[4]})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[4] : "US"})    
            
            if(len(fparms[5]) > 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[5] : fparms[5]}) 
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[5] : "None"})    
            

            if(len(fparms[6]) > 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : fparms[6]}) 
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : "None"})    
                
            if(len(fparms[7]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[6] : str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY))})
            else :
                batch_size  =   int(fparms[7])
                if(batch_size > cfg.get_config_value(cfg.ARCGIS_BATCH_MAX_BATCH_SIZE_KEY)) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("batch size exceeds arcGIS suggested max batch size of "+ str(cfg.get_config_value(cfg.ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY)))
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[7] : fparms[7]})    
 
            if(len(fparms[8]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : "85"})
            else :
                bulk_score  =   int(fparms[8])
                if( (bulk_score > 100) or (bulk_score < 0) ) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("bulk score is not within limit of 0 - 100 ")
                else :
                    bulk_geocode_kwargs.update({batch_arcgis_query_labelList[8] : fparms[8]}) 

            if(len(fparms[9]) == 0) :
                df_title    =   fparms[0]
                df          =   cfg.get_dfc_dataframe_df(df_title)
            
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : str(len(df))})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[9] : fparms[9]}) 
            
            if(len(fparms[10]) == 0) :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[10] : "5"})
            else :
                bulk_geocode_kwargs.update({batch_arcgis_query_labelList[10] : fparms[10]}) 

    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)
        
    
def validate_bing_bulk_parms(geotype,inputs,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}

    if(geotype == sugm.QUERY) :
        
        fparms = get_parms_for_input(inputs,bulk_bing_query_input_idList)

        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe selected defined")
        else :
                
            if(opstat.get_status()) :
                if(len(fparms[1]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dataframe address column name(s) defined")
                
            if(opstat.get_status()) :
                if(len(fparms[2]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dataframe lat lng column name(s) defined")

        if(opstat.get_status()) :
                
            bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[0] : fparms[0]})
            bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[1] : fparms[1]})
            bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[2] : fparms[2]})
            
            # full address column name
            if(len(fparms[3]) > 0) :
                bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[3] : fparms[3]})
            else :
                bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[3] : "None"})
            
            # user location    
            if(len(fparms[4]) > 0) :
                
                try :
                    
                    if(not(fparms[4] == "None")) :
                        
                        user_location   =   fparms[4].split(",")
                        
                        if( (len(user_location) > 1) and (len(user_location) < 4) ) :
                            for i in range(len(user_location)) :
                                try :
                                    float(user_location[i])    
                                except :
                                    opstat.set_status(False)
                                    opstat.set_errorMsg("user_location is not a valid geopy.Point")
                                    break
                        
                            if(opstat.get_status()) :
                                bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[4] : fparms[4]})
                            
                        else :
                            opstat.set_status(False)
                            opstat.set_errorMsg("user_location is not a valid geopy.Point")
                            
                    else :
                        bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[4] : ""})    
                        
                        
                except :
                    opstat.set_status(False)
                    opstat.set_errorMsg("user_location is not a valid geopy.Point")
                
            else :
                bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[4] : "None"})
                
            if(opstat.get_status()) :    
                
                # culture
                if(len(fparms[5]) > 0) :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[5] : fparms[5]})    
                else :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[5] : "en"}) 
                
                # neighborhood
                if(len(fparms[6]) > 0) :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[6] : fparms[6]}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[6] : "False"})
            
                # country code
                if(len(fparms[7]) > 0) :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[7] : fparms[7]}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[7] : "False"})
                
                if(len(fparms[8]) > 0) :
                    df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                    if(int(fparms[8]) > len(df)) :
                        bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[8] : len(df)}) 
                    else :
                        bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[8] : fparms[8]})
                else :
                    df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[8] : len(df)}) 
                    
                if(len(fparms[9]) > 0) :
                    if(int(fparms[9]) > 100) :
                        bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[9] : "5"}) 
                    else :
                        bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[9] : fparms[9]})
                else :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[9] : "5"}) 
                    
                if(len(fparms[10]) > 0) :
                    if(int(fparms[10]) < 0) :
                        bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[10] : "10000"}) 
                    else :
                        bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[10] : fparms[10]})
                else :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[10] : "10000"}) 
                
                    
    else :
        
        try :
                
            # check the required reverse parms
            fparms = get_parms_for_input(inputs,bulk_bing_reverse_input_idList)
        
            if(len(fparms[0]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("No dataframe selected defined")
            else :
                
                if(opstat.get_status()) :
                    if(len(fparms[1]) == 0) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("No dataframe lat_lng name(s) defined")
      
            # validate non required parmsd            
            if(opstat.get_status()) :
                
                bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[0] : fparms[0]})
                bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[1] : fparms[1]})

                if(len(fparms[2]) > 0) :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[2] : fparms[2]}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[2] : "False"})
            
                if(len(fparms[3]) > 0) :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[3] : fparms[3]}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[3] : "False"})
                
                if(len(fparms[4]) > 0) :
                    df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                    if(int(fparms[4]) > len(df)) :
                        bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[4] : len(df)}) 
                    else :
                        bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[4] : fparms[4]})
                else :
                    df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[4] : len(df)}) 
                    
                if(len(fparms[5]) > 0) :
                    if(int(fparms[5]) > 100) :
                        bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[5] : "2"}) 
                    else :
                        bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[5] : fparms[5]})
                else :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[5] : "2"}) 

                if(len(fparms[6]) > 0) :
                    if(int(fparms[6]) < 0) :
                        bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[6] : "10000"}) 
                    else :
                        bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[6] : fparms[6]})
                else :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[6] : "10000"}) 
                    
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Error validating parms")
                
    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)
    
    
def validate_baidu_bulk_parms(geotype,inputs,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}

    if(geotype == sugm.QUERY) :
        
        fparms = get_parms_for_input(inputs,bulk_baidu_query_input_idList)

        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe selected defined")
        else :
                
            if(opstat.get_status()) :
                if(len(fparms[1]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dataframe address column name(s) defined")
                
            if(opstat.get_status()) :
                if(len(fparms[2]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dataframe lat lng column name(s) defined")

        if(opstat.get_status()) :
                
            bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[0] : fparms[0]})
            bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[1] : fparms[1]})
            bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[2] : fparms[2]})
            
            if(len(fparms[3]) > 0) :
                df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                if(int(fparms[3]) > len(df)) :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[3] : len(df)}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[3] : fparms[8]})
            else :
                bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[3] : len(df)}) 
                    
            if(len(fparms[4]) > 0) :
                if(int(fparms[4]) > 100) :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[4] : "2"}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[4] : fparms[4]})
            else :
                bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[4] : "2"}) 
            
            if(len(fparms[5]) > 0) :
                if(int(fparms[5]) < 0) :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[5] : "10000"}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[5] : fparms[5]})
            else :
                bulk_geocode_kwargs.update({bulk_bing_query_input_labelList[5] : "10000"}) 
                    
    else :
                
        # check the required reverse parms
        fparms = get_parms_for_input(inputs,bulk_bing_reverse_input_idList)
        
        if(len(fparms[0]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No dataframe selected defined")
        else :
                
            if(opstat.get_status()) :
                if(len(fparms[1]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No dataframe lat_lng name(s) defined")
      
        # validate non required parmsd            
        if(opstat.get_status()) :
                
            bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[0] : fparms[0]})
            bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[1] : fparms[1]})

            if(len(fparms[2]) > 0) :
                
                df  =   cfg.get_current_chapter_df(cfg.SWGeocodeUtility_ID)
                if(int(fparms[4]) > len(df)) :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[2] : len(df)}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[2] : fparms[2]})
            else :
                bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[2] : len(df)}) 
                    
            if(len(fparms[3]) > 0) :
                if(int(fparms[3]) > 100) :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[3] : "2"}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[3] : fparms[3]})
            else :
                bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[3] : "2"}) 

            if(len(fparms[4]) > 0) :
                if(int(fparms[4]) < 0) :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[4] : "10000"}) 
                else :
                    bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[4] : fparms[4]})
            else :
                bulk_geocode_kwargs.update({bulk_bing_reverse_input_labelList[4] : "10000"}) 
                
    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)
    

def validate_bulk_parms(geocid,geotype,inputs,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : validate the bulk geocode parms
    * 
    * parms :
    *  geocid       - geocoder id
    *  geotype      - geocoder operation type
    *  inputs       - geocode input parms
    *  opstat       - operation status object
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    bulk_geocode_kwargs     =   {}
    
    if(geocid == sugm.GoogleId) :
        bulk_geocode_kwargs     =   validate_google_bulk_parms(geotype,inputs,opstat)       
                
    elif(geocid == sugm.ArcGISId) :
        bulk_geocode_kwargs     =   validate_arcgis_bulk_parms(geotype,inputs,opstat)
    
    elif(geocid == sugm.BingId) :
        bulk_geocode_kwargs     =   validate_bing_bulk_parms(geotype,inputs,opstat)  
    
    elif(geocid == sugm.BaiduId) :
        bulk_geocode_kwargs     =   validate_baidu_bulk_parms(geotype,inputs,opstat)  
        
    if(opstat.get_status()) :  
        return(bulk_geocode_kwargs)
    else :
        return(None)


def get_bulk_form_id(geocid,gtype) :
    """
    * ---------------------------------------------------------
    * function : get the form id for a geocoder
    * 
    * parms :
    *  geocid  - geocoder id
    *  gtype   - geocoder type - QUERY or REVERSE
    *
    * returns : 
    *  geocoder form id
    * --------------------------------------------------------
    """
 
    if(gtype == sugm.GEOCODER)  :
         if(geocid == sugm.ArcGISId)            : return(batch_arcgis_geocoder_id)   
         elif(geocid == sugm.GoogleId)          : return(google_bulk_geocoder_id)
         elif(geocid == sugm.BingId)            : return(bing_bulk_geocoder_id)
         elif(geocid == sugm.BaiduId)           : return(baidu_bulk_geocoder_id)
         
    elif(gtype == sugm.QUERY)  :
         if(geocid == sugm.ArcGISId)            : return(batch_arcgis_query_id) 
         elif(geocid == sugm.GoogleId)          : return(bulk_google_query_input_id)
         elif(geocid == sugm.BingId)            : return(bulk_bing_query_input_id)
         elif(geocid == sugm.BaiduId)           : return(bulk_baidu_query_input_id)
         
    elif(gtype == sugm.REVERSE)  :
         if(geocid == sugm.GoogleId)            : return(bulk_google_reverse_input_id)
         if(geocid == sugm.BingId)              : return(bulk_bing_reverse_input_id)
         if(geocid == sugm.BaiduId)             : return(bulk_baidu_reverse_input_id)



