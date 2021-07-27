# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2021-07-26 17:03
# * Last modified : 2021-07-27 13:17
# * Filename      : quant.py
# * Description   : 
# *********************************************************

import pandas as pd
import os
import json
from datetime import timedelta, datetime
from dplearn.tools import tick_start, tick_end


# =============================================================================
# ##### K Line Wrapping #####
# =============================================================================
def wrapKLine(data, open_c, close_c, high_c, low_c, vol_c, ts_c, ts_format, wrap):
    """
    This is a function of wrapping K-Line dataframe into longer-duration one. 

    Input:
        data:       [pandas dataframe] K-Line dataframe
        open_c:     [string] Column name of open price
        close_c:    [string] Column name of close price
        high_c:     [string] Column name of highest price
        low_c:      [string] Column name of lowest price
        vol_c:      [string] Column name of lowest price
        ts_c:       [string] Column name of timestamp
        ts_format:  [string] Format of timestamp in input data (eg: "%Y-%m-%d %H:%M:%S")
        wrap:       [string] Time range that you want to wrap

    Output:
        Pandas dataframe
    """
    tick_start("Wraping K Line data")
    
    col_list = [open_c, close_c, high_c, low_c, vol_c, ts_c]
    df = data[col_list]
    
    df[ts_c] = pd.to_datetime(df[ts_c], format=ts_format)
    
    # df["time_group"] = df[ts_c].dt.strftime("%Y-%m-%d@%H")
    
    vol_new = df.groupby(pd.Grouper(key=ts_c, freq=wrap))[vol_c].agg('sum')
    open_new = df.groupby(pd.Grouper(key=ts_c, freq=wrap))[open_c].first()
    close_new = df.groupby(pd.Grouper(key=ts_c, freq=wrap))[close_c].last()
    high_new = df.groupby(pd.Grouper(key=ts_c, freq=wrap))[high_c].max()
    low_new = df.groupby(pd.Grouper(key=ts_c, freq=wrap))[low_c].min()
    
    df_new = pd.DataFrame()
    df_new[open_c] = open_new
    df_new[close_c] = close_new
    df_new[high_c] = high_new
    df_new[low_c] = low_new
    df_new[vol_c] = vol_new
    
    tick_end()
    return df_new












