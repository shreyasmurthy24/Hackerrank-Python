# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 04:15:42 2020

@author: shreyas
"""
#Find the max element in the list, remove the max, and print the max
n = int(input())
arr = map(int, input().split())
arr1 = set(arr)
arr1.remove(max(arr1))
print(max(arr1))