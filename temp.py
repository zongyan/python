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
a = 111
isinstance(a, float) # no results, need to use the print function 
print(isinstance(a, float))
print(isinstance(a, int))
a = 2
print(a)
# del a # delete variable a 
print(a)
a=5
b=4
print(a+b, a - b, a/b, a//b, a%b, a**b)
llist = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
print(llist)
print(llist[0])
print(llist[1:3])
print(llist[2:])
print (llist + tinylist)
a=[0, 1, 2, 3, 4, 5, 6]
print(a[0])
print(a[2:5])
a[2:5] = [13, 14, 15]
print(a)
##define a function for reversing the word
def reverseWords(input):
    inputWords = input.split(" ")
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1]    
    
    # 重新组合字符串 https://www.runoob.com/python/att-string-join.html
    output = ' '.join(inputWords)
    return output

if __name__ == "__main__":
    inputs = "Yan like YuXin"
    rw = reverseWords(inputs)
    print(rw)

ttuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
print(ttuple)
print(ttuple[0])
print(ttuple[1:3])
print(ttuple[2:])
print(tinytuple * 2)    
print(tinytuple + ttuple)        
tup1 = () 
print(tup1)    
tup2 = (12,)     
print(tup2)        
sites = {"Google", "Taobao", "Runoob", "Facebook", "Zhihu", "Baidu"}
print(sites) # 怎样感觉输出的时候，没有一个特定的顺序输出的呢？这个没有看明白
sites = {"Google", "Taobao", "Runoob", "Facebook", "Zhihu", "Baidu", "Zhihu"}
print(sites)    
a=set("abracadabra"); b = set("alacazam")
print(a-b)  # a 和 b 的差集
print(a | b) # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b) # a 和 b 中不同时存在的元素

ddict={}
ddict["one"] = "1 - 菜鸟教程"
print(ddict["one"])
print(ddict)
ddict[2] = "2 - 菜鸟工具"
print(ddict[2])
print(ddict)
# 从上面这两个例子，就是可以清楚的明白，key的概念，还有value的概念的意思的了。
# 2，“one” 是key的概念，"1 - 菜鸟教程" 和 "2 - 菜鸟工具" 是数值的概念
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(tinydict.keys())
print(tinydict.values())
#下面是定义Dictionary的另外一些方式，可以看出这个python还是很多变的
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
print({x: x**2 for x in (2, 4, 6)})
print({x: x**3 for x in (2, 4, 6, 8)})
print(dict(Runoob=1, Google=2, Taobao=3))
# Python数据类型转换
# https://www.runoob.com/python3/python3-data-type.html

print("=================Basic operators==========================")
a = 21
b = 10
print(a+b)
print(a*b)
print(a-b)
print(a/b) # 除以
print(a//b) # 除取整数 注意这两者的区别
print(a%b) # 除取余数
print(b**a)
a=[1,2,3,4,5,6,7]
if (n := len(a)) > 10: # := 海象运算符，可在表达式内部为变量赋值
    print(f"List is too long ({n} elements, expected <= 10)")
    # 上面这个print应该是可以打印除变量n的，但是呢，就是没有办法打印出来，这个就是
    # 在以后的学习中需要注意一下

a = 10
b = 20
if ( a and b ):
   print ("1 - 变量 a 和 b 都为 true")
else:
   print ("1 - 变量 a 和 b 有一个不为 true")
   
if ( a or b ):
   print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("2 - 变量 a 和 b 都不为 true")   

# 修改变量 a 的值
a = 0
if ( a and b ):
   print ("3 - 变量 a 和 b 都为 true")
else:
   print ("3 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
   print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("4 - 变量 a 和 b 都不为 true")

if not( a and b ):
   print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("5 - 变量 a 和 b 都为 true")
   
a = 10
b = 20
llist = [1, 2, 3, 4, 5 ]

if (a in llist):
    print("a is in list")
else:
    print("a is NOT in the list")

if (b not in llist):
    print("b is NOT in the list")
else:
    print("b is in the list")
    
a = 2

if (a in llist):
    print("a is in the list")
else:
    print("a is NOT in the list")
    
a= b = 20
if (a is b):
    print("a is the same with b")
else:
    print("a is different from b")

# id()用来获取对象内存的地址    
if (id(a) == id(b)):
    print("a is the same with b")
else:
    print("the address of A is different from that of b")
    
b = 30

if (a is b):
    print("a is the same with b")
else:
    print("a is different from b")

if (a is not b):
    print("a is different from b")
else:
    print("a is teh same with b")
    
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
# and 拥有更高优先级:
x = True
y = False
z = False
 
if x or y and z:
    print("yes")
else:
    print("no")
    
    
    
    
    
    
    
    
    
