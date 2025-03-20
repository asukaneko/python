#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:23:46 2021

@author: pi
"""

import PySimpleGUI as sg

def ChatBot():
    layout= [
            [sg.Text('聊天室', size=[40,1])],
            [sg.Output(size=(80.20))],
            [sg.Multiline(size=[70,5], enter_submits=True)],
            [sg.Button('send', button_color=(sg.YELLOWS[0], sg.BLUES[0]))],
            [sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]
    ]
            
        
    window = sg.Window('chat window', layout=layout, default_element_size=(30,2))
    
    while True:
        event, value=window.read()
        if event in 'send':
            print(value)
        else:
            break
    
    window.close()
            
ChatBot()      
            