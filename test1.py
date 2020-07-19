# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:53:33 2018

@author: distroter
"""

import MySQLdb
conn = MySQLdb.connect(user="root", passwd="", db="rishi")
cur = conn.cursor()
CID="rishi"
PW="gupta"

cur.execute("select * from iot;")

row = cur.fetchone()
while row is not None:
    print(row[0])
    print(row[1])
    row=cur.fetchone()
conn.commit()
cur.close()
conn.close()


