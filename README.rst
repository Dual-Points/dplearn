DP Learn Toolkit in Python
############################################################


|PyPI Version| |PyPI Platform| |PyPI License| |PyPI Doc|





Why Should I Use This?
************************************************************

This is a Python package for data analysis which contains some very useful functions. 


Installation
************************************************************

.. code-block:: bash
 
 $ pip install dplearn


Or, you can download the source and

.. code-block:: bash

 $ python setup.py install


Add sudo in the beginning if you met problem.



Modules
************************************************************

- tools
- math
- extra



Usage
************************************************************


Use As A Python Module
------------------------------------------------------------

.. code-block:: python
   
 from dplearn.tools import clean
 data = clean(data)
 print(data)



Documentation
************************************************************

Check out the latest ``dplearn`` documentation at `Read the Docs <https://dp-learn.readthedocs.io/en/latest/>`_



Contributing
************************************************************

Please send pull requests, very much appriciated. 


1. Fork |org_repo| on Github. 
2. Make a branch off of master and commit your changes to it. 
3. Create a Pull Request with your contribution. 







|Sen LEI Website| |Sen LEI Github|







.. |PyPI Platform| image:: https://img.shields.io/pypi/pyversions/dplearn.svg?logo=python&logoColor=white
   :target: https://pypi.python.org/pypi/dplearn

.. |PyPI License| image:: https://img.shields.io/pypi/l/dplearn.svg
   :target: https://opensource.org/licenses/BSD-3-Clause

.. |PyPI Version| image:: https://img.shields.io/pypi/v/dplearn.svg
   :target: https://pypi.python.org/pypi/dplearn

.. |PyPI download| image:: https://img.shields.io/pypi/dm/dplearn.svg
   :target: https://pypi.python.org/pypi/dplearn

.. |PyPI Doc| image:: https://readthedocs.org/projects/dp-learn/badge
   :target: https://dp-learn.readthedocs.io/en/latest/



.. |Sen LEI Github| image:: https://img.shields.io/badge/Github-Sen%20LEI-orange.svg?logo=github&longCache=true&style=flat&logoColor=white
   :target: https://github.com/Listen180

.. |Sen LEI Website| image:: https://img.shields.io/badge/Author-Sen%20LEI-orange.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+PHN2ZyAgIHhtbG5zOm9zYj0iaHR0cDovL3d3dy5vcGVuc3dhdGNoYm9vay5vcmcvdXJpLzIwMDkvb3NiIiAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgICB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIgICB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiICAgd2lkdGg9IjUwMCIgICBoZWlnaHQ9IjUwMCIgICBpZD0ic3ZnMiIgICB2ZXJzaW9uPSIxLjEiICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45MSByMTM3MjUiICAgc29kaXBvZGk6ZG9jbmFtZT0iRFAuLXdoaXRlc3ZnLnN2ZyI+ICA8bWV0YWRhdGEgICAgIGlkPSJtZXRhZGF0YTIyIj4gICAgPHJkZjpSREY+ICAgICAgPGNjOldvcmsgICAgICAgICByZGY6YWJvdXQ9IiI+ICAgICAgICA8ZGM6Zm9ybWF0PmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdD4gICAgICAgIDxkYzp0eXBlICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPiAgICAgICAgPGRjOnRpdGxlPjwvZGM6dGl0bGU+ICAgICAgPC9jYzpXb3JrPiAgICA8L3JkZjpSREY+ICA8L21ldGFkYXRhPiAgPHNvZGlwb2RpOm5hbWVkdmlldyAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiICAgICBib3JkZXJvcGFjaXR5PSIxIiAgICAgb2JqZWN0dG9sZXJhbmNlPSIxMCIgICAgIGdyaWR0b2xlcmFuY2U9IjEwIiAgICAgZ3VpZGV0b2xlcmFuY2U9IjEwIiAgICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAiICAgICBpbmtzY2FwZTpwYWdlc2hhZG93PSIyIiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxNTQzIiAgICAgaW5rc2NhcGU6d2luZG93LWhlaWdodD0iODc3IiAgICAgaWQ9Im5hbWVkdmlldzIwIiAgICAgc2hvd2dyaWQ9ImZhbHNlIiAgICAgaW5rc2NhcGU6em9vbT0iMS4zMzUwMTc2IiAgICAgaW5rc2NhcGU6Y3g9IjI2MS4xMjMwMiIgICAgIGlua3NjYXBlOmN5PSIyNTUuNjIyOTMiICAgICBpbmtzY2FwZTp3aW5kb3cteD0iMCIgICAgIGlua3NjYXBlOndpbmRvdy15PSIwIiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMCIgICAgIGlua3NjYXBlOmN1cnJlbnQtbGF5ZXI9ImcxNCIgLz4gICAgPGRlZnMgICAgIGlkPSJkZWZzNCI+ICAgIDxsaW5lYXJHcmFkaWVudCAgICAgICBpZD0ibGluZWFyR3JhZGllbnQ1NjQwIiAgICAgICBvc2I6cGFpbnQ9InNvbGlkIj4gICAgICA8c3RvcCAgICAgICAgIHN0eWxlPSJzdG9wLWNvbG9yOiNmZmZmZmY7c3RvcC1vcGFjaXR5OjE7IiAgICAgICAgIG9mZnNldD0iMCIgICAgICAgICBpZD0ic3RvcDU2NDIiIC8+ICAgIDwvbGluZWFyR3JhZGllbnQ+ICAgIDxmaWx0ZXIgICAgICAgaGVpZ2h0PSIxLjAwNDgiICAgICAgIHdpZHRoPSIxLjAwNDgiICAgICAgIHk9Ii0wLjAwMjQiICAgICAgIHg9Ii0wLjAwMjQiICAgICAgIGlkPSJzdmdfMl9ibHVyIj4gICAgICA8ZmVHYXVzc2lhbkJsdXIgICAgICAgICBzdGREZXZpYXRpb249IjAuMTQ2IiAgICAgICAgIGluPSJTb3VyY2VHcmFwaGljIiAgICAgICAgIGlkPSJmZUdhdXNzaWFuQmx1cjciIC8+ICAgIDwvZmlsdGVyPiAgICA8ZmlsdGVyICAgICAgIGlua3NjYXBlOmNvbGxlY3Q9ImFsd2F5cyIgICAgICAgc3R5bGU9ImNvbG9yLWludGVycG9sYXRpb24tZmlsdGVyczpzUkdCIiAgICAgICBpZD0iZmlsdGVyNTY3OCIgICAgICAgeD0iLTAuMDEyIiAgICAgICB3aWR0aD0iMS4wMjQiICAgICAgIHk9Ii0wLjAxMiIgICAgICAgaGVpZ2h0PSIxLjAyNCI+ICAgICAgPGZlR2F1c3NpYW5CbHVyICAgICAgICAgaW5rc2NhcGU6Y29sbGVjdD0iYWx3YXlzIiAgICAgICAgIHN0ZERldmlhdGlvbj0iMC40MDUiICAgICAgICAgaWQ9ImZlR2F1c3NpYW5CbHVyNTY4MCIgLz4gICAgPC9maWx0ZXI+ICA8L2RlZnM+ICA8ZyAgICAgaWQ9Imc5Ij4gICAgPHRpdGxlICAgICAgIGlkPSJ0aXRsZTExIj5iYWNrZ3JvdW5kPC90aXRsZT4gICAgPHJlY3QgICAgICAgZmlsbD0ibm9uZSIgICAgICAgaWQ9ImNhbnZhc19iYWNrZ3JvdW5kIiAgICAgICBoZWlnaHQ9IjUwMiIgICAgICAgd2lkdGg9IjUwMiIgICAgICAgeT0iLTEiICAgICAgIHg9Ii0xIiAvPiAgPC9nPiAgPGcgICAgIGlkPSJnMTQiPiAgICA8dGl0bGUgICAgICAgaWQ9InRpdGxlMTYiPkxheWVyIDE8L3RpdGxlPiAgICA8ZWxsaXBzZSAgICAgICBmaWx0ZXI9InVybCgjc3ZnXzJfYmx1cikiICAgICAgIHN0cm9rZT0iIzAwMDAwMCIgICAgICAgcnk9IjczIiAgICAgICByeD0iNzMiICAgICAgIGlkPSJzdmdfMiIgICAgICAgY3k9IjE4MS43OTcxMTkiICAgICAgIGN4PSIyNTAiICAgICAgIHN0cm9rZS13aWR0aD0iMS41IiAgICAgICBmaWxsPSIjMDAwMDAwIiAgICAgICBzdHlsZT0iZmlsbC1vcGFjaXR5OjE7ZmlsbDojZmZmZmZmO3N0cm9rZTpub25lO2ZpbGwtcnVsZTpldmVub2RkO2ZpbHRlcjp1cmwoI3N2Z18yX2JsdXIpIiAvPiAgICA8ZWxsaXBzZSAgICAgICBzdHJva2U9IiMwMDAwMDAiICAgICAgIHJ5PSI0MC40OTk5OTkiICAgICAgIHJ4PSI0MC40OTk5OTkiICAgICAgIGlkPSJzdmdfMSIgICAgICAgY3k9IjMzNS4yOTcxMjEiICAgICAgIGN4PSIyNDkuOTk5OTk5IiAgICAgICBzdHJva2Utd2lkdGg9IjEuNSIgICAgICAgZmlsbD0iIzAwMDAwMCIgICAgICAgc3R5bGU9InN0cm9rZTpub25lO2ZpbGwtb3BhY2l0eToxO2ZpbGw6I2ZmZmZmZjtmaWxsLXJ1bGU6ZXZlbm9kZDtmaWx0ZXI6dXJsKCNmaWx0ZXI1Njc4KSIgLz4gIDwvZz48L3N2Zz4=&longCache=true&style=flat&logoColor=white
   :target: https://listen180.github.io/LEI-Sen/



.. |org_repo| image:: https://img.shields.io/badge/-repository-green.svg?logo=github&longCache=true&style=flat&logoColor=white
   :target: https://github.com/Dual-Points/dplearn
