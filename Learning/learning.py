# # -*- coding: utf-8 -*-
# """
# Created on Wed Jan 12 18:31:38 2022

# @author: HP

"""
IN THIS FILE, I AM GOING TO BE HANDY WHILE LEARNING DIFFERENT DATA 
STRUCTURES AND SOME ALOGARITHMS.

"""
# ALL ABOUT COMPUTATIONAL ANALYSIS

import matplotlib.pyplot as plt
import time
import random
import numpy as np



# Defining usual sum, it will have order N $$ O(N) $$

def sum_num(N):
    sum_ = 0
    for n in range(N + 1):
        sum_ += n
    return sum_

# Defining a mathemetical trick of finding the sum of N values using Gauss formula
# SO, this function has an order 1, $$ O(1) $$ because we are runnig one instruction, compare to 
# previous one where we had to execute N instructions hence order N

def sum_gauss(N):
    return N*(N + 1)//2

def compute(n_avgs, func, N):
    times = []
    for _ in range (n_avgs):
        ts = time.time()
        func(N)
        times.append(time.time() - ts)
    return sum(times)/float(len(times)) * 1000 # in milliseconds

n_avgs = 10
time_sum = []
time_gauss = []
N_range = range(10, 100000, 5000)

for N in N_range:
    time_sum.append(compute(n_avgs, sum_num, N))
    time_gauss.append(compute(n_avgs, sum_gauss, N))
    
# print(f'The long time is {time_sum}')
# print(f'The short time is {time_gauss}')
plt.plot(N_range, time_sum, 'o-', label='Sum Numbers')
plt.plot(N_range, time_gauss, 'o-', label='Gauss')
plt.xlabel('N')
plt.ylabel( 'Average time (ms)')
plt.legend()

# lis = ['a', 'b', 'c']
# ped = [1, 3, 5]

# print([ped.append(i) for i in lis])


"""Another Example using lists to search for an element"""
# COMPUTATIONAL COMPLEXITIES

# a function to define the finding the element 
def find_element(list_, ele):
    for element in list_:
        if element == ele:
            return True
    return False

# making a random list

def random_list(N, sort=False):
    list_ = [random.randint(0, N*10) for number in range(N)]
    return sorted(list_) if sort else list_

# defining the function that times the runnig time of a fuction 

def time_func(func, *args):
    ts = time.time()
    func(*args)
    return time.time() - ts

# Defining the function to do the timing of the search

def compute_with_list(n_avgs, N, sort, *funcs):
    ans = []
    for _ in range(n_avgs):
        # defining a random list_r created using the function created above 
        list_r = random_list(N, sort)
        # defining the number to find in the list
        n_to_find = random.randint(0, 10*N)
        # appending the number of times in the ans[] as the functions are running 
        ans.append([time_func(func, list_r, n_to_find) for func in funcs])    
        
    # finding the average time within those time that we have in the list
    return np.array(ans).mean(axis=0)*1000  # converting the answer in milliseconds

n_avgs = 40
N_range = range(10, 100000, 10000)
time_list = np.array([compute_with_list(n_avgs, N, False, find_element) for N in N_range ])

plt.title("Graph of finding element in all elements of the list")
plt.plot(N_range, time_list, 'o-')

"""Using a sorted list to search an element from the list"""

def find_element_sorted(list_, ele):
    for element in list_:
        if element == ele:
            return True
        if element > ele:
            return False
    return False

n_avgs = 40
N_range = (10, 100000, 10000)
time_list = np.array([compute_with_list(n_avgs, N, True, find_element, find_element_sorted) for N in N_range])

plt.plot(N_range, time_list[:,0], 'o-', label='find_element function')
plt.plot(N_range, time_list[:,1], 'o-', label='find_element_sorted function')
plt.legend()

""" Using binary serching alogarithm"""

# defining a function that will search and divides the lists each time we loop through to find the element

def find_element_binary(list_, ele):
    if len(list_) < 1:
        return False
    mid_point = len(list_)//2
    if list_[mid_point] == ele:
        return True
    elif list_[mid_point] > ele:
        return find_element_binary(list_[:mid_point], ele)
    else:
        return find_element_binary(list_[mid_point+1:], ele)
    
# Checking the codes



    










