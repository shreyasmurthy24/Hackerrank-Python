# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 01:14:07 2020

@author: shreyas
"""
marksheet=[]
scorelist=[]

list = [('Harry', 37.21),('Berry', 37.21),('Tina',37.2),('Akrithi',41),('Harsh',39)]
for _ in range(int(input())):
    name = input()
    score = float(input())        
    marksheet+=[[name,score]]
    scorelist+=[score]
    b=sorted(list(set(scorelist)))[1]

    for a,c in sorted(marksheet):
        if c==b:
            print(a)