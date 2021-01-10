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

# https://www.cnblogs.com/shuopython/p/11922641.html
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
    
print("=================Number==========================")    
print(0xA0F)
print(complex(1.11, 2.2))
#注意这三点的区别，//并不一定返回的总是int，也是可能是浮点型的
print(7//2);print(7//2.0);print(7.0//2); 

tax = 12.5 / 100
price = 100.50
price * tax
# price + _ # 这个_很奇怪，在台式机上面就是可以正常的运行的了，但是呢，在这个
            # surface pro上就是没有办法运行的了，这个是一个很奇怪的现象。
            # 也是可以运行的，但是这一种运行方式，是基于之前已有的数据，如果之前console
            # 没有任何的数据，这里就是会报错的了。
"""
这里注意这个_的用法，这个就是表示，用户所见到的那个数，
比如说就是现在console上面的那个数据
"""

abs(-10) #数字的绝对值
# ceil(10.2) # 向上去整数，就是11
# 很奇怪，就是在surface上面没有办法识别这个函数            
# exp(1)
# log(100, 1)    
# 这一些的函数都是没有办法识别出来的了，ToDo：我的理解就是需要库的支持
"""    
https://www.runoob.com/python3/python3-number.html
上面这个链接中的，数学函数，随机数函数，三角函数&数学常量都是没有办法在
surface中成功运行的了，我的理解并不是IDE的问题，而是需要相应的库支持
ToDo    
"""

print("=================Python3 String==========================")
var1 = 'Hello World!'
#这个和C语言中的print的使用方式还是非常的类似的了。
#https://www.runoob.com/python3/python3-string.html 中就是有各种不同符号数据格式的
#解释
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
name = "Runoob"
print('hello %s' % name)
# 上面的这个是旧版本的打印形式，下面的这个是python 3.6之后引入的新的方式，两者通用
# f-string， { }里面是代表变量的意思
name="Runoob"
print(f"hello, {name}")
print(f"{1+2}")
w={"name": "Runoob", "url":"www.runoob.com"}
print(f"{w['name']}: {w['url']}")
print(f'{w["name"]}: {w["url"]}')
# print(f"{w["name"]}: {w["url"]}") 这一个就是运行不起来，主要的原因还是在于变量
#name & url应该是使用单引号，而不能够使用双引号，这个倒是非常有意思的呢
#也就是说，在一行代码中，不能够同时使用两次双引号

# toDo: 我还是不明白  “Python 的字符串内建函数” 是什么意思

print("=================Python3 List==========================")

llist = ["Google", "Runoob", 1997, 2000]
print(llist[3])
llist[3]=2021# 更新列表里面的第三个数
print(llist)
del llist[2]#删除列表中的第三元素
print(llist)
print(len(llist))#打印出列表的长度
#ToDo： 列表函数&方法
"""
其实呢，不管是列表，还是其他的函数，我可以暂时不理解，但是还是需要过一边的了，这样子心里
就是有一个大概的概念，就是都是有一些什么类型的函数的了，这样子，也是可以方便以后查找的
了。但是呢，这个工作暂时也是不太勉强，毕竟我现在的主要任务就是得先是把这个python的一些
基本的用法过一遍，学习python不是主要的目的，而是需要学习后面的PyTorch，这个才是我们的
重中之重的了。
"""

print("=================Python3 Tuple==========================")
"""
元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 ( )，列表使用方括号 [ ]。
"""

print("=================Python3 Dictionary==========================")
dictt={"Name":"Runoob", "Age":'7', "Class":"First"}
print(dictt)
dictt["Age"] = 8 # 修改字典中的value的内容
dictt["Class"] = "Second" # 修改字典中的value的内容
print("ductt['Age']", dictt["Age"])
print("ductt['Classs']", dictt["Class"])

del dictt["Name"] # 删除Name对应的这个数值
print(dictt)
dictt.clear() # 清空字典，意思是说，删除字典中所有的数值了。
print(dictt)
del dictt     # 删除字典，意思就是说这个dictt这个字典变量了。
# print(dictt)

dictt={"Name": "Runoob", "Age": "7", "Name": "小菜鸟"}
print(f"dictt['Name']: {dictt['Name']}")
# 上面的这个例子就是说明了，如果字典中出现了两次Name，那么第二次的数值就是会
# 对第一次进行覆盖的了。

print("=================Python3 Set==========================")
a = {x for x in "abracadabra" if x not in "abc"}
print(f"{a}") 

Thisset = {"Google", "Baidu", "Tencent"}
Thisset.add("Facebook") # 向Thisset添加一个变量
print(Thisset)
Thisset.update("{Apple}", "{TaoBao}") # 这个和上面add的区别的区别就是在于
                    # add可以增加一个字符串，但是这个就是不会增加一个字符串，而是
                    # 会把每一个字符串改编成一个个的character的形式的了。
print(Thisset)
Thisset.remove("Google") # 移除一个string
print(Thisset)
Thisset.discard("Google") # 这个和remove的区别就是在于 如果某一个element不存在的话
                    # remove就是会报错，但是呢，使用discard就是不会报错
                    
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()
m = thisset.pop() # pop是随机的选取一个数出来
print(x,m)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear() # 清空集合
print(thisset)