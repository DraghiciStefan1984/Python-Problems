# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:57:51 2018

@author: Stefan Draghici
"""
import time

#/first attempt, brute force, worst time
def prime_numbers_generator_1():
    max_number=int(input("enter a number: "))
    if type(max_number)!=int:
        raise Exception("Enter a valid integer")
    prime_list=[]
    
    start_time=time.clock()
    for number in range(0, max_number+1):
        factors=0
        for factor in range(1, number+1):
            if number%factor==0:
                factors+=1
        if factors==2:
            prime_list.append(number)
    end_time=time.clock()
    
    print("Time taken: ", (end_time-start_time))
    return prime_list

# second attempt
def prime_numbers_generator_2():
    max_number=int(input("enter a number: "))
    if type(max_number)!=int:
        raise Exception("Enter a valid integer")
    prime_list=[]
    
    def factor_count(num):
        factors=0
        for i in range(2, num//2+1):
            if num%i==0:
                factors+=1
        if factors==0:
            prime_list.append(num)
    
    start_time=time.clock()
    for number in range(0, max_number+1):
        factor_count(number)
    end_time=time.clock()
    
    print("Time taken: ", (end_time-start_time))
    #return prime_list
    
# third attempt
def prime_numbers_generator_3():
    max_number=int(input("enter a number: "))
    if type(max_number)!=int:
        raise Exception("Enter a valid integer")
    prime_list=[]
    
    def prime_test(num):
        prime=True
        for i in range(3, (num//2+1), 2):
            if num%i==0:
                prime=False
                return prime
        return prime
    
    start_time=time.clock()
    for number in range(0, max_number+1):
        if prime_test(number)==True:
            prime_list.append(number)
    end_time=time.clock()
    
    print("Time taken: ", (end_time-start_time))
    #return prime_list