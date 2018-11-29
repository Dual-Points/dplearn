Tutorial on module dplearn.tools
========================================

continue_check
--------------------

.. code-block:: python

 from dplearn.tools import continue_check
 check_value = continue_check("Do you want to continue this procedure? [Y/n]: ")

 if check_value in ['n', 'N']:
    break
 else:
    pass
