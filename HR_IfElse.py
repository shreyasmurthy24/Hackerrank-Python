# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:41:34 2020

@author: shreyas
"""

n = int(input().strip())
if n%2 != 0:
    print("Weird.")
elif 2 < n <=5 :
        print("Not Weird..")
elif 6 > n <= 20:
        print("Weird...")
elif n > 20:
        print("Not Weird....")