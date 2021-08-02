# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2021-08-02 10:39
# * Last modified : 2021-08-02 10:39
# * Filename      : data_sample.py
# * Description   : 
# *********************************************************

import pandas as pd
import os

CWD = os.getcwd()

def kLine():
    """
    """
    f_path = CWD + "/data_sample/kLine.csv"
    df = pd.read_csv(f_path)
    return df
