#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:04:48 2021

@author: pi
"""

from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=2)

def a():
    try:
        import bof
    except Exception:
        print("没有找到播放文件")

def b():
    s = 0
    for i in range(10000):
        s += 1
        print(s)
        
a()
b()
    