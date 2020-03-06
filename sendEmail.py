#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:37:53 2019

@author: yang
"""

import smtplib
from email.mime.text import MIMEText


def sendEmailMassage(user, user_pass, target, massage):
    try:
        gmail_user = user
        gmail_password = user_pass
        
        msg = MIMEText(massage)           #sent masage
        msg['Subject'] = 'comic'             #email title
        msg['From'] = gmail_user
        msg['To'] = target
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        print('Email sent over.')
    except:
        print('email send system error.')
    
#massage = 'Function test'
#sendEmailMassage('yanghometcl@gmail.com','andy60136','andy831201@gmail.com', massage)

