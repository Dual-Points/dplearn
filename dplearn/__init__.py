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
                                                                      
                  Mac version 
                  Copyright 2018 Sen LEI
                  All Rights Reserved
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
                                                                      
                  Linux version
                  Copyright 2018 Sen LEI
                  All Rights Reserved
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
                                                                      
                  Windows version
                  Copyright 2018 Sen LEI
                  All Rights Reserved
                '''
        print(info)
        time.sleep(2)


avatar()
