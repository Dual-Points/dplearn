#!/Users/leisen/anaconda3/bin/python3
# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-21 16:26
# * Last modified : 2018-11-21 16:26
# * Filename      : tools.py
# * Description   : 
# *********************************************************

import re
import time
import pandas as pd
import numpy as np
from math import atan, acos, asin, tan, sin, cos, radians, fabs, sqrt

def tick_start (contex):
    """
    """
    global t0
    t0 = time.time()
    print('\n')
    print(contex, '...')

def tick_end (contex=''):
    """
    """
    global t1
    global t_range
    t1 = time.time()
    t_range = round(t1 - t0, 4)
    print('...', contex, 'excution complete. (Time consumed:', t_range,'s) \n')




def continue_check (prompt):
    """
    """
    check_value = input(prompt)
    while True:
        try:
            if check_value not in ['n', 'N', 'y', 'Y']:
                error_message = """[Invalid input] please type 'y' as yes, or 'n' as no. """
                print(error_message)
                raise ValueError(error_message)
            else:
                return check_value
        except ValueError:
            check_value = input(prompt)
            continue



def clean (data_org, col_name, replace=False, print_each=True):
    """
    Function for removing all special chatacters. 
    
    INPUT: 
        data: pandas dataframe
        col_name: 
        
    OUTPUT: 
        pandas dataframe, with an extra cleaned column
    """
    if isinstance(data_org, pd.DataFrame):
        pass
    else:
        raise ValueError("Please use pandas dataframe as input. ")
    data = data_org.copy()
    total_len = len(data[col_name])
    
    ## Find all special characters exited in data
    tick_start("Finding all special characters exited in data")
    result_list = []
    pattern_org = re.compile(u'[^\u4E00-\u9FA5 a-zA-Z0-9]+')
    for i,string in enumerate(data[col_name]):
        result = pattern_org.search(string)
        if result:
            result = result.group(0)
            result_list.append(result)
    result_list = list(set(result_list))
    tick_end()
    
    ## Make sure to escape properly (get the modified version of reg-express)
    escape_list = ['*', '.', '?', '+', '$', '^', '[', ']', '(', ')', '{', '}', '|', '\\', '/']
    
    result_list_flat = [x for sublist in result_list for x in sublist]
    result_list_flat = list(set(result_list_flat))
    
    special_char_list = []
    for char in result_list_flat:
        if char in escape_list:
            special_char = "\\" + char
        else:
            special_char = char
        special_char_list.append(special_char)
    special_char = '|'.join(str(x) for x in special_char_list)
    special_char = ' |' + special_char
    
    ## Remove all special characters
    tick_start("Removing all special characters")
    if replace==True:
        col_name_new = col_name
    elif replace==False:
        col_name_new = col_name + '_cleaned'
        data[col_name_new] = data[col_name]
    else:
        raise ValueError("Please input either 'True' or 'False' for replace arguement. ")
    
    pattern = re.compile(special_char)
    
    for i,string in enumerate(data[col_name]):
        """
        """
        result = pattern.search(string)
        if result:
            sub_string = pattern.sub('', string)
            data.loc[i, col_name_new] = sub_string
            if print_each==True:
            	print(f'          {data_org.loc[i, col_name]} --> {sub_string}')
            elif print_each==False:
            	pass
            else:
            	raise ValueError("Please input either 'True' or 'False' for print_each arguement. ")
            print(f'Progress: {i+1}/{total_len}', end='\r')
            result_list.append(result)
    print(f'Progress: {i+1}/{total_len}')
    tick_end()
    
    return data





## Change from a text to another text
def clean_to (data_org, col_name, org_regexpress, target_text, replace=False, print_each=True):
    """
    """
    if isinstance(data_org, pd.DataFrame):
        pass
    else:
        raise ValueError("Please use pandas dataframe as input. ")
    data = data_org.copy()
    total_len = len(data[col_name])

    tick_start(f'Changing {org_regexpress} to {target_text}')
    
    result_list = []
    pattern = re.compile(org_regexpress)
    for i,string in enumerate(data[col_name]):
        result = pattern.search(string)
        if result:
            sub_string = pattern.sub(target_text, string)
            data.loc[i, col_name] = sub_string
            print(f"""          {data_org.loc[i, col_name]} --> {sub_string}""")
            print(f"""Progress: {i+1}/{total_len}""", end='\r')
            result_list.append(result)
    print(f"""Progress: {i+1}/{total_len}""")
    result_list = list(set(result_list))

    tick_end()

    return data












def cord_distance(Lng_A, Lat_A, Lng_B, Lat_B):
    """
    Function for calculating distance by using cordinates
    """
    if (Lng_A == Lng_B and Lat_A == Lat_B):
        distance = 0
    else:
        ra = 6378.140  
        rb = 6356.755  
        flatten = (ra - rb) / ra 
        rad_lat_A = radians(Lat_A)
        rad_lng_A = radians(Lng_A)
        rad_lat_B = radians(Lat_B)
        rad_lng_B = radians(Lng_B)
        pA = atan(rb / ra * tan(rad_lat_A))
        pB = atan(rb / ra * tan(rad_lat_B))
        xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
        c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2.0 / cos(xx / 2.0) ** 2.0
        c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2.0 / sin(xx / 2.0) ** 2.0
        dr = flatten / 8.0 * (c1 - c2)
        distance = ra * (xx + dr)
    return distance


