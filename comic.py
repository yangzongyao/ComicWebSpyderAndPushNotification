#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 02:10:39 2019

@author: yang
"""

import sendEmail
import comicSpyder

def comic(comicName):
    comicInformation = comicSpyder.ComicNewVersionInformation(comicName)
    if comicInformation == 1:
        filename = '/home/yang/Desktop/Program/Python/ForFun/Comic/book_me/' + comicName
        with open(filename, 'r') as f:
            comicNum, comicVersion = f.read().splitlines()
        massage = comicNum + " have newest version!\n https://tw.manhuagui.com/comic/" + comicNum + "/"
        sendEmail.sendEmailMassage('yanghometcl@gmail.com', 'andy60136', 
                                   'andy831201@gmail.com',massage)
    elif comicInformation == 0:
        print(comicName , 'only have old version.')
    else:
        print("creat new comic :",comicName)