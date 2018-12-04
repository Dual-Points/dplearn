############################################################
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


1. |org_repo| on Github. 
2. Make a branch off of master and commit your changes to it. 
3. Create a Pull Request with your contribution. 









|

|


************************************************************

|Sen LEI Website|  |Sen LEI Github|















.. |org_repo| image:: https://img.shields.io/badge/-Fork%20this%20repository-green.svg?logo=github&longCache=true&style=flat&logoColor=white
   :target: https://github.com/Dual-Points/dplearn




.. |PyPI Platform| image:: https://img.shields.io/pypi/pyversions/dplearn.svg?logo=python&logoColor=white
   :target: https://pypi.python.org/pypi/dplearn

.. |PyPI License| image:: https://img.shields.io/github/license/Dual-Points/dplearn.svg
   :target: https://github.com/Dual-Points/dplearn/blob/master/LICENSE

.. |PyPI Version| image:: https://img.shields.io/pypi/v/dplearn.svg
   :target: https://pypi.python.org/pypi/dplearn

.. |PyPI download| image:: https://img.shields.io/pypi/dm/dplearn.svg
   :target: https://pypi.python.org/pypi/dplearn

.. |PyPI Doc| image:: https://readthedocs.org/projects/dp-learn/badge
   :target: https://dp-learn.readthedocs.io/en/latest/



.. |Sen LEI Github| image:: https://img.shields.io/badge/Github-Sen%20LEI-orange.svg?logo=github&longCache=true&style=flat&logoColor=white
   :target: https://github.com/Listen180

.. |Sen LEI Website| image:: https://img.shields.io/badge/Author-Sen%20LEI-orange.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANUAAADVCAMAAAD3nkWxAAACglBMVEUAAAD///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9xjI0NAAAA1XRSTlMAAQIDBAUGBwgJCgsMDg8REhQXGBkaGxwdHh8gIiMkJSYnKCkqKywtLi8wMTI0NTY3ODk6Ozw9Pj9AQUJDREVGR0hJSktMTU5PUFJTVVZZWltcXV5fYGFkZWZnaGlqb3BxcnN0dXZ3ent8fYCBgoOFh4iKi4yNkJGSk5SVlpeZmpydnp+hoqOmp6ipqqusra6vsbKztLW2ubu8vsDDxMXGx8jJy8zNzs/Q0dLT1NXW19jZ3N3e3+Dh4uPk5ebn6Onq6+zt7u/w8fLz9PX29/j5+vv8/f7yOdf5AAAEF0lEQVR42u3da1fVVRAG8Ocgl8BCBQtJirQwqCwIk8DMMpIuplCIXcyiUioLKcssLVMjNCrCrOhCaqGppd1LKSsijgUY4DnP9+kVbzDgv8/ZL2ZY8/sOs+dZs9bMhjHGGGOMMcYYY4wxxhhjjPElPaegeGFxfs55mBgSCh7a1t7FYV3tr67OD0G1tMq3uni2P5qXpUKr+Tv+5mhObb8OGi38lGNrXxKCMmUHOb4D10OTzMYoA2nOgBpVYQbVsxw6nPMCXTSmQYGcL+nmyEyIN6eTrk5eAeFKwnTXUwLRCnsZi37RLTmvm7EJ50OsGZ2M1fELIFRiO2O3PwkyPcd4NECk8ijjEb0ZAqX9yPj8PBnyPMt4rYc4eYOM18BsSPM247cLwsyOMH6RWZClkT7sgCjTh+jDYCYkeZR+PAxJDtOPgxCkgL7MgRx19OUxyNFGX96HGMm99KU3GVIU059CSLGS/qyAFBvoTwOk2E1/WiDFEfrzBaT4if58Dym66U8XpBigP/9CiFCE/kRCEOIf+nMKUvxKf05Aim/pzzFI8Qn9+RhSbKM/r0CKNfSnFlLcRn/KIcV0ehPNhBjf0JevIMfL9GUT5LiTvtwOOVLD9COcCkG204+tkKSMfsyHJAlf04ejIYhSTR8qIUvSDz5mFokQ5l7GrwbSJHzGeH2eAHHmRhifyDVwoCU2vQiJJh+NL9emQaS8Psau9zIIVcPY3QOx6hmrdRBsk4IZjLtJOxmLpkkQLfQ83b2UAOmeiNJNtA4KVHTTRXgpVMje6xL+cqBE8uP9DKavLgl6ZL3JIN6dCV1u+Ijj+bAU+hS3DnF0Q+8UQaep97WPNnZZmwHFLqxp7By5vvNadTb0m1q0on5LY0tbS+OWp6sLp8AYY4wxxhgjTfKVlbVPPbN+bdXV52KCuLxu/xCHDe2rz4N6iXft40gdlYlQ7aZj/D/f3QG9prVyNO+dD6VKj3N0vy+CSncPcixnHoBCj0Q5jjVQZ1mU44muhDJlgxzfmTKoMuUEg/gtE5o0M5hmKFLKoBZDjVAHgzoUghblDG4JtNjD4NqgRHaEwUWyoMMqulgNHXbTRSt06KGLcAgaZNHNDGiwiG5uhAZVdFMFDR6km1XQoJZuapW0Kzf3T8i6Wg4NSuhmHjTIoJtpUOEkXfwCHZro4nXoUOO4SqFDej+DO50OJXYxuCZocVWUgc2FGh8wqD1woOX88sClUGQDg2mAJikHGERHClTJ7eH4ui+CMkW9Dv9t6HFLP8fWtxgKzfuLY/nzWqiUvddh70qP5HWnRyupJ5Og18VvRHi2yM4c6DZrc/fI93zzJdAv5daNhweHE9KhjeXJmCgScxdULK1YkJsIY4wxxhhjjDHGGGOMMcYYY4wxxhhjjBnhP6hK+cPRlZTHAAAAAElFTkSuQmCC&longCache=true&style=flat&logoColor=white
   :target: https://listen180.github.io/LEI-Sen/


