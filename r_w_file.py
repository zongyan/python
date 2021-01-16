# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 17:38:06 2021

@author: yan
"""


import os
from pathlib import Path

filepath = "./test.txt"
full_filepath = os.path.join(os.path.dirname(__file__),filepath)

f = open(full_filepath, "w") 
f.write("Python is a good programming language\n Yes, it is!!!\n")
f.close()

f = open(full_filepath, 'r')
strr=f.readline() # 这个就是仅仅是会返回一行
print(strr)
f.close()

f = open(full_filepath, 'r')
strr=f.readlines() # 这个就是仅仅是会返回所有行
print(strr)
f.close()

f = open(full_filepath, 'r')
strr=f.readlines(1) # 这个就是仅仅是会返回一行，因为我们在里面设置了1
print(strr)
f.close()