# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file, which is used to learn python from 
the following link:
https://www.runoob.com/python3/python3-tutorial.html
"""
# hello, world
print("hello, world!")
print("=================Basic Syntax==========================")
if True:
    print("Answer")
    print("true")
else:
    print("Answer")
    print("false")
    
print("next learning point")
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
            item_three
print("total")
print(total)

str="Runoob"

print(str)
print(str[0:-1])
print(str[0])
print(str[0:6])
print(str[2:5])
print(str[2:])
print(str[1:5:2])
print(str+str)
print(str*2)
print(str+"你好")
print("---------------")
print('------------------')
print("hello\nstr")
print(r"hello\nstr")
# the following three lines are used for learning the command input
#input("\n\n按下 enter 键后退出。")
#a = input("input:")
#print("this following is from the input command:"); print(a); print("end")
cc = 1;
print(cc); print("test")
print(cc, end=""); print("test")

import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
print("=================Second Test==========================")
for i in sys.argv:
    print (i)
print(sys.argv)
print("sys.argv")
print("=================Data Type==========================")
m=1
print(m, end="")
m=2
print(m, end="")
counter=100
miles=100.0
name="zongyan"
print(counter)
print(miles)
print(name)
a,b,c=1,2,"zongyan"
print(a,b,c)
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
