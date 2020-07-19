# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:53:45 2019

@author: distroter
"""



p,q = 53,59 


n = p*q
 
e = 3


# encrypt

str = input();
temp = 0
for ch in str:
    temp = 10 * temp + ord(ch) - ord('a') + 1
    

print(temp)



encrypt = pow(temp,e) % n


print(encrypt)



# decrypt

temp = (p-1)*(q-1)
k=2

d = (k*temp + 1)/e
d=int(d)
ans = pow(encrypt,d) % n
ans=ans.__str__()
ans1= ''.join(chr(i+96) for i in map(int,ans))
print(ans1) 