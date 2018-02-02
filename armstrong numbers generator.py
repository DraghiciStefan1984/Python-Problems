#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:41:53 2018

@author: user
"""

def armstrong_number_list():
    number=int(input("enter a number: "))
    if type(number)!=int:
        raise Exception("Enter a valid integer")

    armstrong_numbers_list=[]
    
    for num in range(1, number+1):
        
        number_length=len(str(num))
        digit_list=[]
        digit_sum=0
        
        for digit in str(num):
            digit_list.append(int(digit))
        
        for i in digit_list:
            digit_sum+=i**number_length
        
        if digit_sum==num:
            armstrong_numbers_list.append(num)
    
    return armstrong_numbers_list