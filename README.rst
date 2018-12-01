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

.. |Sen LEI Website| image:: https://img.shields.io/badge/Author-Sen%20LEI-orange.svg?logo=data:image/png;base64,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&longCache=true&style=flat&logoColor=white
   :target: https://listen180.github.io/LEI-Sen/



.. |org_repo| image:: https://img.shields.io/badge/-repository-green.svg?logo=github&longCache=true&style=flat&logoColor=white
   :target: https://github.com/Dual-Points/dplearn
