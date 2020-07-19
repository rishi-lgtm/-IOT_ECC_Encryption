# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:09:10 2018

@author: distroter
"""
from flask import Flask,request
from cryptography.fernet import Fernet
import MySQLdb
app = Flask(__name__)

@app.route("/",methods=['POST'])
def hello():
    ECID = request.form['ECID'] 
    EPW = request.form['EPW']
    key = request.form['key']
    choice = request.form['choice']
    
    key = key.encode('utf-8')
    print(key)
    choice = int(choice)
    cipher_suite = Fernet(key)
    
    DCID = cipher_suite.decrypt(ECID.encode('utf-8'))
    DPW = cipher_suite.decrypt(EPW.encode('utf-8'))
    
    conn = MySQLdb.connect(user="root", passwd="rishi26071997", db="rishi")
    cur = conn.cursor()
    ans=""
    if choice == 1 :
        sql='select count(*) from iot where CID IN %s'
        args=[[DCID.decode('utf-8')]]
        cur.execute(sql,args)
        row = cur.fetchone()
        ct = int(row[0])
        if ct > 0:
            ans = "Not unique username"
        else :
            cur.execute("insert into iot values ( %s , %s )",(DCID.decode('utf-8'),DPW.decode('utf-8')))
            ans = "Registered"
    elif choice == 2 :
        sql='SELECT PW FROM iot WHERE CID IN %s'
        args=[[DCID.decode('utf-8')]]
        cur.execute(sql,args)
        row = cur.fetchone()
        if DPW.decode('utf-8') == str(row[0]):
            ans = "Matched" 
        else:
            ans ="Not Matched" 
    conn.commit()
    cur.close()
    conn.close()    
    return ans
        
               
        

        
        
        
            

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=5000)