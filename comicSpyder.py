#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 01:05:58 2019

@author: yang
"""

import re                   #Regular Expression
import requests
import sendEmail
import time
from selenium import webdriver
from bs4 import BeautifulSoup


def findComicInfomation(comicNum):
    try:
        url = 'https://tw.manhuagui.com/comic/' + str(comicNum) + '/'
        r = requests.get(url).text
        sp = BeautifulSoup(r, 'html.parser')
        adult = sp.find(id=["checkAdult"])
        if adult != None:
            driver = webdriver.Firefox()
            driver.get(url)
            time.sleep(3)
            driver.find_element_by_id("checkAdult").click()
            #r = requests.get(url).text
            #sp = BeautifulSoup(r, 'html.parser')
        find = sp.find(id=["chapter-list-1", "chapter-list-0"])
        f = find.find_all('a')
        find_title = sp.find_all('div')
        
        text_list = []
        
        pattern = re.compile('\d+')         #number and repeat more then one
        
        for i in f:
            classOfWeb = i.get('class')
            t = i.get('title')
            if classOfWeb == ['status0'] and t != None:
                text = t
                text = pattern.findall(text)
                if len(text) > 0:
                    text_list.append(int(text[0]))
        
        for j in find_title:
            if j.get('class') == ['book-title']:
                title = j.h1.string
        
        return max(text_list), title
    except:
        massage = 'Spyder system error.'
        sendEmail.sendEmailMassage('yanghometcl@gmail.com', 'andy60136', 
                                   'andy831201@gmail.com',massage)

    
#findComicInfomation('14735')
#findComicInfomation('24579')

import os

def ComicNewVersionInformation(comicName):
    filename = '/home/yang/Desktop/Program/Python/ForFun/Comic/book_me/' + str(comicName)
    if os.path.exists(filename):
        with open(filename,'r') as f:
            text = f.read().splitlines()
        comicNum, watched_version = text
        watched_version = int(watched_version)
        now_version = findComicInfomation(comicNum)[0]
        if watched_version < now_version:           #have new version
            filename = '/home/yang/Desktop/Program/Python/ForFun/Comic/book_me/' + comicName
            with open(filename,'w') as f:
                f.write(comicNum+'\n')
                f.write(str(now_version))
            return 1
        else:
            return 0
    else:
        comicNum = comicName
        now_version, filename = findComicInfomation(comicNum)
        filename = '/home/yang/Desktop/Program/Python/ForFun/Comic/book_me/' + filename
        with open(filename, 'w') as f:
            f.write(comicNum+'\n')
            f.write(str(now_version))
        return filename
            




