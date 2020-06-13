# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:54:11 2020

@author: shreyas
"""

list = [('Harry', 37.21),('Berry', 37.21),('Tina',37.2),('Akrithi',41),('Harsh',39)]
list1 = [name for (name, marks) in list if marks > [-2]]
print(list1)
print(list1[-2])