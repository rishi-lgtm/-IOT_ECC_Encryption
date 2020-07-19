# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:31:32 2018

@author: distroter
"""

import random
import requests


r1 = requests.post("http://localhost:5001/t1", data={})
response=r1.text
print(response)
point,public_key = response.split()
public_key=int(public_key)
point=int(point)
M = 242
k = random.randint(1,100)
c1 = k * point
c2 = M + k * public_key
f=455
n=9
temp1 = (3 * n + f + 3)/2

for count in range(1,10):
    if count == 1 :
        temp = temp1 + k * public_key
        r = requests.post("http://localhost:5001", data={'C1': c1,'C2':c2,'temp':float(temp),'count':count,'point':point,'public_key':public_key})
        print (r.text)
        ans='1'
        if ans == '1' :
            print("confirmed")
            continue
        else :
            print("not confirmed")
            break;
    elif count == 8 :
        temp1 = (3 * temp1 + f + 3)/2
        temp = temp1 + k * public_key
        r = requests.post("http://localhost:5001/", data={'C1': c1,'C2':c2,'temp':float(temp+2),'count':count,'point':point,'public_key':public_key})
        ans=str(r.text)
        if ans == '1' :
            print("confirmed")
            continue
        else :
            print("Not confirmed")
            break;
            
    else:
        temp1 = (3 * temp1 + f + 3)/2
        temp = temp1 + k * public_key
        r = requests.post("http://localhost:5001/", data={'C1': c1,'C2':c2,'temp':float(temp),'count':count,'point':point,'public_key':public_key})
        ans=str(r.text)
        if ans == '1' :
            print("confirmed")
            continue
        else :
            print("Not confirmed")
            break;
            
            

        
    
    



