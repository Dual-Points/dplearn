# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-28 17:23
# * Last modified : 2021-07-27 13:17
# * Filename      : extra.py
# * Description   : 
# *********************************************************

from dplearn.tools import tick_start, tick_end
from dplearn.tools import clean, clean_to
import pandas as pd

# =============================================================================
# ##### Brand Cleaning #####
# =============================================================================
def brand_cleaning (data_input, colname):
    """
    This function is to clean brands with specific rules. 
    
    
    Input: 
        data_input: [dataframe] with only one
        colname: [string] column name 
        
    OUTPUT: 
        data: [dataframe] modified dataset
    """
    tick_start('Cleaning')
    
    data = data_input.copy()
    
    ### Change °C|°c|° to 度
    data = clean_to(data, colname, org_regexpress='°c|°', target_text='度')
    
    
    ### Change + to plus
    data = clean_to(data, colname, org_regexpress='\+$', target_text=' plus')
    
    
    ## Clean special characters
    data = clean(data, colname, replace=False, print_each=False)
    
    
    tick_end()
    
    
    return data





def brand_cleaning2 (data_input):
    """
    This function is to clean brands with specific rules. 
    
    
    Input: 
        data_input: [dataframe] with only one
        colname: [string] column name 
        
    OUTPUT: 
        data: [dataframe] modified dataset
    """
    tick_start('Cleaning')
    
    data = pd.DataFrame(data_input)
    colname = "brand"
    data.columns = [colname]
    
    ### Change °C|°c|° to 度
    data = clean_to(data, colname, org_regexpress='°c|°', target_text='度')
    
    
    ### Change + to plus
    data = clean_to(data, colname, org_regexpress='\+$', target_text=' plus')
    
    
    ## Clean special characters
    data = clean(data, colname, replace=False, print_each=False)
    
    
    tick_end()
    
    
    return data
