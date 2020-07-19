# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 21:37:20 2018

@author: distroter
"""
import pyotp,time
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret,interval=60)
otp = totp.now() 
print(otp)
totp.verify('415082')