# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 17:38:06 2021

@author: yan
"""

print('================IO============')
print("https://www.runoob.com/python3/python3-inputoutput.html")
print('================IO============')  

import os
from pathlib import Path

filepath = "./test.txt"
full_filepath = os.path.join(os.path.dirname(__file__),filepath)

f = open(full_filepath, "w") 
f.write("Python is a good programming language\n Yes, it is!!!\n")
f.close()

f = open(full_filepath, "r") 
print(f.read())
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

f=open(full_filepath, 'w')
# num=f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
num=f.write("my personal website is yzong.com \n")
print(f"the printed number is {num}")
num=f.write("my personal website is yzong.com \n test test test \n")
print(f"the printed number is {num}")
f.close()
#根据测试，这个f.write返回的数值，应该就是写入的character的个数的了。
#同时，这个里就是有一个问题，我就是准备是写入这个中文的时候，就是没有办法写入成功
#电脑是会报错的，但是呢，写入英文的话，就是可以的了，我的理解，主要还是因为有某一种
#库没有引入，导致的这个错误的了。

f=open(full_filepath, 'w')
value=("yzong.com", "test")
s=str(value)
print(f.tell()) # 返回文件对象当前所处的位置，它是从文件开头开始算起的字节数。
                # 所以这里就是应该是0了
f.write(s)
print(f.tell()) # 返回文件对象当前所处的位置
f.close()
# 从这个就是可以看出，就是仅仅是能够写入字符串的了，同时呢，如果不是字符串的话
# 就是需要先是强制转换成字符串的形式的了。

f = open(full_filepath, 'rb+')
f.write(b"0123456789abcdef")
print(f.seek(5)) # 这个就是默认的是从起始位置开始向后移动
print(f.read(1))
print(f.seek(5,0)) # 这个就是从起始位置开始向后移动
print(f.seek(1,1)) # 这个就是从当前位置开始向后移动
print(f.read(1))
print(f.seek(-4,2)) # 表示从文件的结尾往前移动x个字符
print(f.read(1))
f.close()

with open(full_filepath, 'r') as f:
    read_data = f.read()
    print(read_data)
print(f.closed)
"""
其实，使用一般的f.open的时候，就是需要自己主动关闭的了，即使用f.close()功能的了
但是呢，如果是使用这个with open的话，系统就是可以自动关闭打开的这个文件了
"""

import pickle

fpath = "./test.pkl"
full_picklepath = os.path.join(os.path.dirname(__file__),fpath)
#注意这里就是和test.txt是不一样的了。

data1= {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append([1, 2, 3])
print(selfref_list)

output = open(full_picklepath, 'wb')

# Pickle dictionary using protocol 0.
print(pickle.dump(data1, output)) # 这个我倒是看明白了，即使把data1 pickle到文件中

# Pickle the list using the highest protocol available.
print(pickle.dump(selfref_list, output, -1)) # 这个我倒是看明白了，即使
# 把selfref_list pickle到文件中,但是这个-1是highes protocol的文件，这个我还是不明白
# 这个highest protocol到底是一个什么意思的了。

output.close()

#上面关于这个pickle的代码，还是不明白是一个什么意思的了。

import pprint, pickle

pkl_file=open(full_picklepath, "rb")

data3=pickle.load(pkl_file)
pprint.pprint(data3)

data4 = pickle.load(pkl_file)
pprint.pprint(data4)

pkl_file.close()