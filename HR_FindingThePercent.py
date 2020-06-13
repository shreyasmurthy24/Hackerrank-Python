# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 01:56:51 2020

@author: shreyas
"""

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    query_name = input()
    