# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:57:39 2020

@author: user
"""

file = open("pokemon.jpg","rb")
img =file.read()
file.close()

file = open("pokemon fans.jpg","wb")
img =file.write(img)
file.close()