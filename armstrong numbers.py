#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:41:53 2018

@author: user
"""

def armstrong():
    number=int(input("enter a number: "))
    if type(number)!=int:
        raise Exception("Enter a valid integer")
        
    number_length=len(str(number))
    digit_list=[]
    is_armstrong=False
    digit_sum=0
    
    for digit in str(number):
        digit_list.append(int(digit))
    
    for i in digit_list:
        digit_sum+=i**number_length
    
    if digit_sum==number:
        is_armstrong=True
        return digit_sum
    return is_armstrong