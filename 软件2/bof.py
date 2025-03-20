#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 21:26:38 2021

@author: pi
"""

import os
import time

def bf():
    try:
        print("独家播放,Ctrl+C退出")
        time.sleep(2)
        os.system('mpv 君がいる世界へ.mp3')
    except Exception:
        pass