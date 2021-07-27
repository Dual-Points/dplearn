# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-21 16:26
# * Last modified : 2021-07-27 13:17
# * Filename      : tools.py
# * Description   : 
# *********************************************************

import re
import sys
import time
import pandas as pd
import numpy as np
import concurrent
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import create_engine
import getpass as gp
import datetime as dt


#####  #####
def tick_start (context):
    """
    
    INPUT: 
        context: string that specifying the task. 
    """
    global t0
    t0 = time.time()
    print('\n')
    print(context, '...')

#####  #####
def tick_end (context=''):
    """
    
    INPUT: 
        context: string; defult by eding with '... excution complete' and the time used. 
    """
    global t1
    global t_range
    t1 = time.time()
    t_range = round(t1 - t0, 4)
    print('...', context, 'excution complete. (Time consumed:', t_range,'s) \n')




#####  #####
def continue_check (prompt):
    """
    This function will help to check if the input is either 'n', 'N', 'y', or 'Y' 
    to make sure computer get the right value to continue. 
    
    Otherwise the prompt will show up again untill you input a valid value or 
    forced to quit the program. 
    
    
    INPUT: 
        prompt: [string] the text shown on the terminal explaining what task to be continued. 

    OUTPUT: 
        check_value: [string] either 'n', 'N', 'y' or 'Y'. 
    
    Example: 
        check_value = continue_check('Do you want to continue this procedure? [Y/n]: ')
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



#####  #####
def clean (data_org, col_name, replace=False, print_each=True):
    """
    This function is to remove all special chatacters. 
    
    
    INPUT: 
        data: pandas dataframe
        col_name: [string] the column name of the variable you want to serch for
        replace: [boolean]
        print_each: [boolean]
        
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





##### Change from a text to another text #####
def clean_to (data_org, col_name, org_regexpress, target_text, replace=True, print_each=True):
    """
    This function is to change some value satisfying specific reg-expression to a specific text. 

    
    INPUT: 
        data: pandas dataframe
        col_name: [string] the column name of the variable you want to serch for
        org_regexpress: [string] the reg expression that you wnat to match with
        target_text: [string] the target text that you are going to change to
        replace: [boolean]
        print_each: [boolean]
    
    OUTPUT: 
        pandas dataframe, with an extra cleaned column
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

















#####  #####
def concurrent_run (time_out_max=0.5, time_out_count_max=10, max_workers=1):
    """
    INPUT: 
        time_out_max: [number] seconds that you want to wait at most for a single excuation
        time_out_count_max: [number] maximum number of consecutive Timeout Errors you may want to abort the procedure. 
    """

    time_out_count = 0
    time_out_index_list = []


    zh_list = []
    result_df = pd.DataFrame({"eng":eng_list, "zh":np.nan})
    total_len = len(result_df["eng"])


    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        
        to_lang = 'zh'
        translator = Translator(to_lang=to_lang)
        
        for i,text_eng in enumerate(result_df["eng"]):
            """
            """
            print(f"""    Progress: {i+1}/{total_len} """, end='\r')
            try:
                text_executor = executor.submit(translator.translate, text_eng)
                text_zh = text_executor.result(timeout=time_out_max)
                result_df.loc[i, "zh"] = text_zh
            except concurrent.futures.TimeoutError:
                time_out_count += 1
                time_out_index_list.append(i)
                print(f'        [TimeoutError] in translating {text_eng}. Jumped this item. ')
                
                if time_out_count>=time_out_count_max:
                    time_out_toolong = time_out_index_list[-time_out_count_max]==time_out_index_list[-1] - (time_out_count_max-1)
                    if time_out_toolong:
                        check_value = continue_check(f"""{time_out_count_max} consecutive TimeoutErrors occured. 
                            Type 'y' to continue (and reset timeout counter) or 'n' to abort: """)
                        if check_value in ['n', 'N']:
                            print('!!! Procedure aborted !!!')
                            break
                        else:
                            time_out_count = 0
                            time_out_index_list = []
                            pass
        print(f"""    Progress: {i+1}/{total_len} """)





##### pgSQL connector #####
def pg_conn(host_adress, port_adress, db_name):
    """
    pgSQL connector
    """
    DB_loc = host_adress + ':' + port_adress + ':' + db_name

    username = input(f"Please input your user name on ({DB_loc}): ")
    passcode = gp.getpass("Please input your passcode: ")

    address = 'postgresql://'+ username + ':' + passcode + '@' + host_adress + ':' + port_adress + '/' + db_name
    
    conn = create_engine(address, echo=False).connect()

    return conn









##### Extract and generate json style conversion #####
def json_convertor (data, col_from, col_to):
    """
    This function is to use a two-columns pair to generate a json style string 
    that can be used in the .replace() function in pandas. 
    
    INPUT: 
        data: pandas DataFrame
        col_from: column name to be used as 'before-change-value'
        col_to: column name to be used as 'after-change-value'
    
    OUTPUT: 
        json_string_long: json style string
    """
    json_string_long = []
    data = data.reset_index()
    total_length = len(data)
    for i in range(total_length):
        """
        """
        json_string = "'" + data.loc[i, col_from] + "'" + ":" + \
                      "'" + data.loc[i, col_to] + "'"
        json_string_long.append(json_string)
    json_string_long = "{" + (',').join(json_string_long) + "}"
    
    return json_string_long








##### Split sting in a column into several columns #####
def sep_expand (data, col_from, cols_to, sep=','):
    """
    This function is to split sting in a column into several columns. 
    
    INPUT: 
        data: pandas DataFrame
        col_from: column name to be used as 'before-split-value'
        cols_to: column names to be used as 'after-split-value'
        sep: seperator used to seperate the values
    
    OUTPUT: 
        data_expand: expanded columns (pandas DataFrame)
    """
    foo = lambda x: pd.Series([i for i in reversed(x.split(sep))])
    data_expand = data[col_from].apply(foo)
    data_expand.columns = cols_to
    
    return data_expand





def convert_time_diff_hour (diff):
    """
    """
    diff_window = int(diff.days * 24 + diff.seconds/3600 + 1)

    return diff_window



##### Check if it is in a n hour windows #####
def consecutive_check (data, col_name, sep, limit, window, unit, time_fmt='%Y%m%d%H',check_col_name='check'):
    """
    This function is to check if a record shown at least n times within m timestamps. 

    NOTE: 
        n shou be less or equal to m; 
        when m = n, meaning that you are finding consecutive n timestamp shown. 
    
    INPUT: 
        data: pandas DataFrame
        col_name: column name that stores all timestamps (string format, has specific seperator)
        sep: seperator used to seperate those timestamps
        limit: the minumun number of timestamps [int] 
        window: the length of the time window [int] (same unit with 'limit')
    
    OUTPUT: 
        DataFrame with an extra column told you True or False 
    """
    if limit > window:
        raise ValueError("Value of 'limit' should be less than or equal to that of 'window'. ")
    else:
        pass
    if unit == 'h' or unit == 'H':
        time_diff_func = convert_time_diff_hour
    
    data = data.reset_index().drop(columns=["index"])
    data[check_col_name] = False
    total_records = len(data)

    for i in range(len(data)):
        """
        """
        time_list = data.loc[i, col_name].split(sep)
        time_list = list(filter(None, time_list)) # remove the empty item(s) if exists
        time_list = [dt.datetime.strptime(ts, time_fmt) for ts in time_list]
        time_list.sort()
        
        for j, ts in enumerate(time_list):
            """
            """
            if j+limit <= len(time_list):
                first_date = time_list[j]
                end_date = time_list[j+limit-1]
                diff = end_date - first_date
                diff_window = time_diff_func(diff)
                if diff_window <= window:
                    data.loc[i, check_col_name] = True
                    break
                else:
                    continue
        p_perc = round((i+1) / total_records * 100, 2)
        sys.stdout.write("    Progress: %d/%d, %.2f%%   \r" % (i+1, total_records, p_perc) )
        sys.stdout.flush()
    
    return data








