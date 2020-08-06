# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:38:45 2020

@author: user
"""

d={}

import os.path
def choose_list():
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("1.scores")
    print("2.all scores")
    print("3. search scores")
    print("4.leave")
    
if os.path.isfile("score.txt"):
    new=open("scores.txt",'r')
    print("open old file")
else:
    new=open ("scores.txt",'w')
    print("new file")
    
    

while True:
           choose_list()
           hhh=int(input("enter num"))
           #輸入選項
           #if
           if hhh==1:
               name=str(input("enter name"))
               score=str(input("enter score"))
               if name=='0':
                   break
               elif name not in d:
                   d[name]=score
                   for k,v in d.items:
                       add=open("score.txt","a")
                       add.write(k)
                       add.write(":")
                       add.write(v)
                       add.write("\n")
               else:
                    print("此成績已輸入")