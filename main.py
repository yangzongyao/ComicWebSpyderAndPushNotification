#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 02:22:23 2019

@author: yang
"""

import comic
import sys
import os


if len(sys.argv) >= 2: 
    arg = sys.argv[1]
    if arg == '-new':
        if len(sys.argv) == 3:
            newComicNum = sys.argv[2]
            comic.comic(newComicNum)
            exit()
        else:
            print('argv error.')
    else:
        print('parameters error.')
        
checkComicNumber = os.listdir('/home/yang/Desktop/Program/Python/ForFun/Comic/book_me/')
for i in checkComicNumber:
    comic.comic(i)

    
    
         
