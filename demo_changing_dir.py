# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:55:19 2021

@author: Yan Zong

The following code shows how to use the os package to change the working directory;
Please see the following link for more details. 
https://linuxize.com/post/python-get-change-current-working-directory/#:~:text=To%20find%20the%20current%20working,chdir(path)%20.
"""

import os 
# print the current working directory
print(f"the current folder path is as follows: {os.getcwd()}")

# change the current working directory to the sub folder
os.chdir("./data") # this is the relative path (recommended), NOT the absolute path
# print the current working directory
print(f"the current folder path is as follows: {os.getcwd()}")

# change the current working directory to the parent folder
os.chdir("..")
# print the current working directory
print(f"the current folder path is as follows: {os.getcwd()}")