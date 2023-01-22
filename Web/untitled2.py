# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:28:25 2022

@author: choji
"""
userinput= input("Please enter nucleotide sequence: ")
charT = 0
charA = 0
charC = 0
charG = 0

for char in userinput:
    if char == 'T' :
        charT = charT +1
    if char == 'A' :
        charA = charA +1
    if char == 'C' :
        charC = charC +1
    if char == 'G' :
        charG = charG +1

topEquation = charG + charC
bottomEquation = charA + charT + charG + charC

gcContent = (topEquation / bottomEquation) *100
print (f'GC-content : {gcContent}')

