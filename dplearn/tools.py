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


def continue_check (prompt):
    """
    """
    check_vlaue = input(prompt)
    while True:
        try:
            if check_value not in ['n', 'N', 'y', 'Y']:
                error_message = """[Invalid input] please type 'y' as yes or 'n' as no. """
                print(error_message)
                raise ValueError(error_message)
            else:
                return check_value
        except ValueError:
            check_value = input(prompt)
            continue
