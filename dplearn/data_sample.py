# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2021-08-02 10:39
# * Last modified : 2021-08-02 10:39
# * Filename      : data_sample.py
# * Description   : 
# *********************************************************

import pkg_resources
import pandas as pd


def kLine():
    """
    """
    f_path = "data/kLine.csv"
    stream = pkg_resources.resource_stream(__name__, f_path)
    df = pd.read_csv(stream,  encoding='utf-8')
    return df
