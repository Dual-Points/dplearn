#!/Users/leisen/anaconda3/bin/python3
# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-28 16:58
# * Last modified : 2018-11-28 16:58
# * Filename      : math.py
# * Description   : 
# *********************************************************


from math import atan, acos, asin, tan, sin, cos, radians, fabs, sqrt







def cord_distance(Lng_A, Lat_A, Lng_B, Lat_B):
    """
    Function for calculating distance by using cordinates. 


    INPUT: 
    	Lng_A: 
    	Lat_A: 
    	Lng_B: 
    	Lat_B: 

    OUTPUT: 
    	distance: [number] (unit: km)
    """
    if (Lng_A == Lng_B and Lat_A == Lat_B):
        distance = 0
    else:
        ra = 6378.140  
        rb = 6356.755  
        flatten = (ra - rb) / ra 
        rad_lat_A = radians(Lat_A)
        rad_lng_A = radians(Lng_A)
        rad_lat_B = radians(Lat_B)
        rad_lng_B = radians(Lng_B)
        pA = atan(rb / ra * tan(rad_lat_A))
        pB = atan(rb / ra * tan(rad_lat_B))
        xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
        c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2.0 / cos(xx / 2.0) ** 2.0
        c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2.0 / sin(xx / 2.0) ** 2.0
        dr = flatten / 8.0 * (c1 - c2)
        distance = ra * (xx + dr)
    return distance


