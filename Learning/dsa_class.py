# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 10:49:14 2022

@author: HP
"""

import time

# Checking the codes  with list comprehension 
""" CODES FROM TATENDA SHARED DOC WEEK 2"""

def test1():
    ts = time.time()
    l = []
    for i in range(10):
        l = l + [i]
    print(l)
    print(f'time: {time.time() - ts}')
    
def test2():
    ts = time.time()
    l = []
    for i in range(10):
        l.append(i)
    print(l)
    print(f'time: {time.time() - ts}')
    
def test3():
    ts = time.time()
    l = [i for i in range(10)]
    print(l)
    print(f'time: {time.time() - ts}')
    
def test4():
    ts = time.time()
    l = list(range(10))
    print(l)
    print(f'time: {time.time() - ts}')
    
test4()