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

# # COMPUTATIONAL COMPLEXITIES





