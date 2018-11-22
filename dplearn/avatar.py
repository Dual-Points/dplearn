#!/home/leisen/anaconda3/bin/python3
# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-10-26 16:47
# * Last modified : 2018-10-26 16:47
# * Filename      : avatar.py
# * Description   : 
# *********************************************************




import time
import platform

class avatar(object):
    def __init__(self):
        self._judge()
        if self.n == 1:
            self.type_1()
        elif self.n == 2:
            self.type_2()
        elif self.n == 3:
            self.type_3()

    def _judge(self):
        os_type = platform.platform().split('-')[0]
        if os_type == 'Darwin':
            self.n = 1
        elif os_type == 'Linux':
            self.n = 2
        elif os_type == 'Windows':
            self.n = 3
        else:
            self.n = 2

    def type_1(self):
        info = '''
    ____              __   ____        _       __      
   / __ \__  ______ _/ /  / __ \____  (_)___  / /______
  / / / / / / / __ `/ /  / /_/ / __ \/ / __ \/ __/ ___/
 / /_/ / /_/ / /_/ / /  / ____/ /_/ / / / / / /_(__  ) 
/_____/\__,_/\__,_/_/  /_/    \____/_/_/ /_/\__/____/  
                                                                      
                  M version 1.0.0 
                  copyright 2018 Sen LEI
                '''
        print(info)
        time.sleep(2)

    def type_2(self):
        info = '''
    ____              __   ____        _       __      
   / __ \__  ______ _/ /  / __ \____  (_)___  / /______
  / / / / / / / __ `/ /  / /_/ / __ \/ / __ \/ __/ ___/
 / /_/ / /_/ / /_/ / /  / ____/ /_/ / / / / / /_(__  ) 
/_____/\__,_/\__,_/_/  /_/    \____/_/_/ /_/\__/____/  
                                                                      
                  L version 1.0.0 
                  copyright 2018 Sen LEI
                '''
        print(info)
        time.sleep(2)

    def type_3(self):
        info = '''
    ____              __   ____        _       __      
   / __ \__  ______ _/ /  / __ \____  (_)___  / /______
  / / / / / / / __ `/ /  / /_/ / __ \/ / __ \/ __/ ___/
 / /_/ / /_/ / /_/ / /  / ____/ /_/ / / / / / /_(__  ) 
/_____/\__,_/\__,_/_/  /_/    \____/_/_/ /_/\__/____/  
                                                                      
                  W version 1.0.0 
                  copyright 2018 Sen LEI
                '''
        print(info)
        time.sleep(2)

