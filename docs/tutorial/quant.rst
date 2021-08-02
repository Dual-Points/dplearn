Tutorial on module dplearn.quant
================================

wrapKLine
---------

This is a function of wrapping K-Line dataframe into longer-duration one. 

.. code-block:: python

   import dplearn.data_sample as ds
   from dplearn.quant import wrapKLine

   data = ds.kLine()
   open_c = "open"
   close_c = "close"
   high_c = "high"
   low_c = "low"
   vol_c = "vol"
   ts_c = "time"
   ts_format = "%Y-%m-%d %H:%M:%S"
   wrap = "1h"

   df_new = wrapKLine(data, open_c, close_c, high_c, low_c, vol_c, ts_c, ts_format, wrap)

   pritn(df_new.head())