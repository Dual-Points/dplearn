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

