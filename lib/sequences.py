#!/usr/bin/env python3

def print_fibonacci(number):
    my_list=[]
    if number > 0:
        my_list.append(0)
    if number > 1:
        my_list.append(1)
    if number > 2:
        for i in range(2,number):
              my_list.append(my_list[i-1]+ my_list[i-2]) 
    print(my_list)