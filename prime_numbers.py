# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:57:51 2018

@author: Stefan Draghici
"""

def prime_numbers_generator():
    max_number=int(input("enter a number: "))
    if type(max_number)!=int:
        raise Exception("Enter a valid integer")
    prime_list=[]
    for number in range(0, max_number+1):
        factors=0
        for factor in range(1, number+1):
            if number%factor==0:
                factors+=1
        if factors==2:
            prime_list.append(number)
    return prime_list