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


import time
import pandas as pd
import re


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



def clean (data_org, col_name, replace=False):
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
            print(f"""          {data.loc[i, col_name]} --> {sub_string}""")
            print(f"""Progress: {i}/{total_len}""", end='\r')
            result_list.append(result)
    print(f"""Progress: {i}/{total_len}""")
    tick_end()
    
    return data






