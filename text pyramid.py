#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:10:33 2018

@author: user
"""

def text_pyramid():
    number=int(input("enter the number of levels: "))
    character=input("enter the character for the pyramid: ")
    
    for i in range(0, number):
        s=i*character