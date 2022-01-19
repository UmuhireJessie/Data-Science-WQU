"""
IN THIS FILE, I AM GOING TO BE HANDY WHILE LEARNING DIFFERENT DATA 
STRUCTURES AND SOME ALOGARITHMS.

 THEY ARE SOME DATA STRUCTURES CONTAINED IN COLLECTIONS MODULE
- daque: is in form of a list that could be more faster than a list
- counter: counts element in another data structure and outputs dictionary like strure
It has helper methods, counter.common(n), where n: 2, 3, 4 common elements
- default dict: to count elts in the dict. """

# ~ ALL ABOUT COMPUTATIONAL ANALYSIS ~

import matplotlib.pyplot as plt
import time
import random
import numpy as np
from collections import defaultdict
from functools import lru_cache


# # TIME COMPLEXITIES 

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

lis = ['a', 'b', 'c']
ped = [1, 3, 5]

print([ped.append(i) for i in lis])


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
"""This function has $$ O(log(n)) because if I want to take another step (maybe having a for loop), the left of the list has to double
Having the double the input mean that I have an exponential growth (2**n), analysing it the opposite means that log2 (n), the nbr of steps that we are doing grows logarithmically"""

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
    
# MEMOIZATION

# Defining a recussive function, a fibonacci_numbers

def fibonacci_recussive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recussive(n-1) + fibonacci_recussive(n-2)
   
# print(fibonacci_recussive(6)) # why can't we call the function insttead of the print function???

# Let's see how many recussive calls we do as we call the function
""" I DON'T GET HOW WE CALCULATE 
def fibonacci_count(n, d):
    d[n] += 1
    if n == 0:
        return n, d
    elif n == 1:
        return 1
    else:
        n1, _ = fibonacci_count(n-1, d)
        n2, _ = fibonacci_count(n-2, d)
        return n1 + n2, d
        
N = 5
d = fibonacci_count(N, defaultdict(int))
                         
for i in range(N):
    print(i, d[i])  """
    
# Initialising the idea of storing the values in a dict rather calling several same numbers which farster if you test it with time library

def fibonacci_mem(n, d):
    if n in d:
        return d[n]
    elif n == 0:
        ans = 0
    elif n == 1:
        ans = 1
    else:
        ans = fibonacci_mem(n-1, d) + fibonacci_mem(n-2, d)
    d[n] = ans
    return ans()

# EXERCISE
## Write the recussive calls, determnine if memoization could work on it and implement it
# 1) 
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
factorial(5)
# 2) Memeoization can't be used bcz no repetition
# 3) Memeization can be used if we will be using that same factorial many times. We may need to store the value so that each time we use it we don't repeat ourselves.
# Generally, memoization is used in programs where we expect to use a lot of he same results over and over again. We can store them and "loopup" in the future.

## ALTENATIVELY ##
# explicit implementation of memoization
fibonacci_cache = {}
def fibonacci_dict(n):
    # return the value if it already exist
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # do the nth value
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_dict(n-1) + fibonacci_dict(n-2)
    # cashing the value
    fibonacci_cache[n] = value
    return value
for n in range(1, 11):
    print(fibonacci_dict(n))
    
# Use of a module lru_cache which means least recently used cache

@lru_cache(maxsize=1000)   
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recussive(n-1) + fibonacci_recussive(n-2)

for n in range(1, 101):
    print(fibonacci(n))   

## ~ MEMORY COMPLEXITIES ~ ##
# In the book 