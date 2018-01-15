# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:31:50 2018

@author: Stefan Draghici
"""

import math

def calculator():
    num=float(input("enter a number: "))
    if type(num) not in (int, float):
        raise Exception("Enter a valid number")
    else:
        print(math.sqrt(num))
        print(num**3)