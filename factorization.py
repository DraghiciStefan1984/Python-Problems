# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:35:05 2018

@author: Stefan Draghici
"""

def factorization():
    number=int(input("enter a number: "))
    if type(number)!=int:
        raise Exception("Enter a valid integer")
    divisor_list=[]
    divisor=1
    while(divisor<number):
        if number%divisor==0:
            divisor_list.append(divisor)
        divisor+=1
    return divisor_list