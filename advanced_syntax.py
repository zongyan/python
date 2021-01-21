# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:54:57 2021

@author: yan
"""
"""
下面的这段代码就是给出了Fibonacci series: 斐波纳契数列的生成方式的了。
我本来是按照solution 1的方式来写代码的，但是呢，没有想到我的solution 1
的方式是不正确的，然后就是没有办法，就是只能够根据tutorial的分析，把solution
1修改成了现在的形式，然后才能够运行成功的了。
"""
print('================1st step for python==========================')
print("https://www.runoob.com/python3/python3-step1.html")
print('================1st step for python==========================')
# solution 1
a = 0
b = 1
while b < 10:
    print(b)
    n = b
    m = a + b
    a = n
    b = m

# solution 2    
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
    
a, b = 0, 1
while b < 200:
    print(b,  end=',');
    a, b = b, a+b # 计算方式为先计算右边表达式，然后同时赋值给左边

print('================conditional statements==========================')
print("https://www.runoob.com/python3/python3-conditional-statements.html")
print('================conditional statements==========================')
age = int(input("请输入你家狗狗的年龄"))
print("")
if age < 0:
    print("你是在逗我的吧！")
elif age == 1:
    print("相当于14岁的人")    
elif age == 2:
    print("相当于22岁的人")    
elif age > 2:
    human = 22 + (age-2)*5
    print(f"对应人类的年龄: {human}")
## 推出提示
input("点击enter键退出")    
"""
python中使用如下的if...elif...else的循环，还有就是while循环，但是呢，就是没有
switch-case循环的了。
"""
print('================Loop==========================')
print("https://www.runoob.com/python3/python3-loop.html")
print('================Loop==========================')
"""
python有while&for两种循环结构，但是呢，没有do...while...这一种
"""
n = 100
summ = 0
count = 0
while count <= n:
    summ = summ + count
    count = count + 1

print(count); print(summ)

var = 1
while var==1: 
    num=int(input("输入一个数字："))
    print(f"你输入的数字是：{num}")

print("Good Bye!")
# 使用 CTRL+C 来退出当前的无限循环。

count = 0
while count < 5:
    print(f"{count} is less than 5")
    count += 1
else:
    print(f"{count} is greater than 5")
# 上面的这个while...else...之前没有看到过，第一次在python里面看见

#  for循环可以遍历任何序列的项目，如一个列表或者一个字符串
# 这个for循环的用法，也是和其他语言非常的不一样的。
languages = ["C", "C++", "Perl", "Python"] 
for x in languages:
    print (x)

sites= ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites: 
    if site == "Runoob": 
        print("菜鸟教程")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# 需要遍历数字序列，可以使用内置range()函数。它会生成数列，
for i in range(5):
    print(i)
    
for i in range(5,9) :
    print(i)    
    
for i in range(0, 10, 3) :
    print(i)
    
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
    
"""
break 可以跳出for和while的循环体，剩余的部分是不执行的，而是会往下跳到上一级的代码
continue 也是跳出for和while的循环体，剩余的部分是不执行的，而是会往上跳到上一级的代码
具体的使用方法就是可以参见下面的这两段代码
"""
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("循环结束")

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print("循环结束")

for letter in 'Runoob':     # 第一个实例
   if letter == 'b':
      break
   print ('当前字母为 :', letter)
   
var = 10                    # 第二个实例
while var > 0:              
   print ('当期变量值为 :', var)
   var = var -1
   if var == 5:
      break
  
for letter in 'Runoob':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print ('当前字母 :', letter)    
   
var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:             # 变量为 5 时跳过输出
      continue
   print ('当前变量值 :', var)
   
# for 中也是可以使用else的了

#  pass是空语句，是为了保持程序结构的完整性。
while True:
    pass

print('================Iterator generator============')
print("https://www.runoob.com/python3/python3-iterator-generator.html")
print('================Iterator generator============')
llist=[1, 2, 3, 4]
it = iter(llist)
print(next(it))
print(next(it))

llist=[1, 2, 3, 4]
it = iter(llist)
for x in it:
    print(x, end=",")
    
# 下面的这个案例，我暂时还是没有办法理解，因为使用的高端的东西还是太多了。
import sys
llist=[1, 2, 3, 4]
it = iter(llist)
while True:
    try: 
        print(next(it))
    except StopIteration:
        sys.exit()

# 也是过了几个迭代器&生成器的例子，但是还是不明白这个iter() & next() 的价值
# 换句话说，我还是不太明白这个是使用在哪里的了。

"""
下面这部分的内容，也是研究这个迭代器&生成器的内容，只不过是从其他的地方找到的，主要
想着是用来理解这个两个概念的了。
"""
# https://blog.csdn.net/weixin_37589575/article/details/104973844
# 这个链接里面的内容非常的好，讲解的非常的详细，收益非常。但是因为我是刚刚学python，
# 就是只是看到section 3为止，后面的几个，就是仅仅是看了结论而已了。
# 可迭代对象：
from collections import Iterable
l1 = [1, 2, 3] # list 
t1 = (1, 2, 3) # tuple
d1 = {"kei1":"Value1"} # dictionary
str1="string1" # string
s1 = {'a', 'b', 'c'} # set

isinstance(l1, Iterable)
isinstance(t1, Iterable)
isinstance(d1, Iterable)
isinstance(str1, Iterable)
isinstance(s1, Iterable)

class MyObject:
    def __init__(self):
        pass
    
class MyIter:
    def __init__(self):
        pass
    def __iter__(self):
        yield 1
        
a=MyObject()
b=MyIter()
isinstance(a, Iterable)
isinstance(b, Iterable)

# 迭代器
from collections import Iterable
from collections import Iterator

l1 = [1, 2, 3] # list 
t1 = (1, 2, 3) # tuple
d1 = {"kei1":"Value1"} # dictionary
str1="string1" # string
s1 = {'a', 'b', 'c'} # set

isinstance(l1, Iterable)
isinstance(t1, Iterable)
isinstance(d1, Iterable)
isinstance(str1, Iterable)
isinstance(s1, Iterable)

class MyObject:
    def __init__(self):
        pass
    
class MyIter:
    def __init__(self):
        pass
    def __iter__(self):
        yield 1

class MyIterator:
    def __init__(self):
        pass
    def __iter__(self):
        yield 1
    def __next__(self):
        return self
    
a=MyObject()
b=MyIter()
c=MyIterator()

print(isinstance(l1, Iterable))
print(isinstance(t1, Iterable))
print(isinstance(d1, Iterable))
print(isinstance(str1, Iterable))
print(isinstance(s1, Iterable))
print(isinstance(a, Iterable))
print(isinstance(c, Iterable))

print(isinstance(l1, Iterator))
print(isinstance(t1, Iterator))
print(isinstance(d1, Iterator))
print(isinstance(str1, Iterator))
print(isinstance(s1, Iterator))
print(isinstance(a, Iterator))
print(isinstance(c, Iterator))

l2=iter(l1)
t2=iter(t1)
d2=iter(d1)
str2=iter(str1)
s2=iter(s1)
print(isinstance(l2, Iterator))
print(isinstance(t2, Iterator))
print(isinstance(d2, Iterator))
print(isinstance(str2, Iterator))
print(isinstance(s2, Iterator))

# 生成器
def fib(n):
    i, a, b= 0, 0, 1
    while i < n:
        yield b # yield关键字的作用，就是把一个普通的函数变成
                # 生成器。当一个函数内出现yield关键字后，就会变
                # 异为生成器，其行为与普通函数不同。
        a, b = b, a + b
        i = i + 1
        
g1 = (x * x for x in range(1, 11))
g2 = fib(6)

print(isinstance(g1, Iterator))
print(isinstance(g2, Iterator))
for i in range(10):
    print(next(g1))
for i in range(6):
    print(next(g2))   
    
"""
从动态的角度，生成器在运行过程中：

当生成器函数被调用的时候，生成器函数不执行内部的任何代码，直接立即返回一个迭代器。
当所返回的迭代器第一次调用 next 的时候，生成器函数从头开始执行，如果遇到了执行 yield x，next立即返回 yield 的值 x。
当所返回的迭代器继续调用next的时候，生成器函数从上次yield语句的下一句开始执行，直到遇到下一次执行yield。
任何时候遇到函数结尾，或者 return 语句，抛出 StopIteration 异常。
"""    

def g():
    print('L1')
    yield 1
    print('L2')
    yield 2
    print('L3')
    yield 3
    print('L4')


it = iter(g())
print('............')
v = next(it)
print(v)
v = next(it)
print(v)
v = next(it)
print(v)
v = next(it)
print(v)     

"""
下面的内容，又是来自于runoob.com的网站上了。
"""
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:            
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclasss = MyNumbers()
myiters = iter(myclasss)

for x in myiters:
  print(x)
  
print('================Function============')
print("https://www.runoob.com/python3/python3-function.html")
print('================Function============')  
# 不定长参数, 这个是之前从来没有遇到过的
def printinfo(arg1, *vartuple):
    "打印任何传入的数据"
    print("输出：")
    print(arg1)
    print(vartuple)
    
printinfo(10), #如果就是没有对这个元素进行赋值，那么就是一个空的元组
printinfo( 70, 60, 50 )

# 可写函数说明
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)

# 这里就是需要备注说明一下，*代表的是元组tuple，**代表的是字典dictionary，这个还是
# 有所区别的了。

#匿名函数, 用lambda来表示声明
summ = lambda arg1, arg2: arg1 + arg2

print("相加后的值为 :", summ(10,20))
print("相加后的值为 : ", summ( 20, 20 ))

# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 
# 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
    
f(10, 20, 30, d=40, e=50, f=60)
# 暂时就是先是放在这里，我也不知道后面是不是会用到，这个太复杂了。

print('================Data structure============')
print("https://www.runoob.com/python3/python3-data-structure.html")
print('================Data structure============')  
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
# 计数()中相应数的个数
a.insert(2, -1) # 在a[2]位置插入-1
a.append(333) #在最后插入333
print(a)
print(a.index(333)) # 打印出第一个333的index
a.remove(333) #删除第一个333
print(a)
a.reverse() #倒序排列
print(a)
a.sort() #从小到达重新排列
print(a)

#列表当作堆栈使用，即后进先出
stack = [3, 4, 5]
print(stack)
stack.append(6)
stack.append(7)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

#列表当作队列使用，即FIFO
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") 
queue.append("Graham")          # Graham arrives
queue.popleft() # 需要区分这个popleft和pop的区别，
queue.popleft() 
queue

# 列表推导式
vec = [2, 4, 6]
[3*x for x in vec]
[[x, x**2] for x in vec]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit] # trip() 方法用于移除字符串头尾指定的字符

# 以上是在列表中使用for，下面的内容是在列表中使用if

[x*x for x in vec if x > 3] # 只有满足x>3的的元素才是可以执行
[x*x for x in vec if x < 2] # 只有满足x<2的的元素才是可以执行

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
[x*y for x in vec1 for y in vec2]
[x+y for x in vec1 for y in vec2]
[vec1[i]*vec2[i] for i in range(len(vec1))]
# 注意上面三个的区别，这个一个非常重要的特性了。

[str(round(355/113, i)) for i in range(1, 6)]

# 嵌套列表解析
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(f"{matrix}") # 3x4的矩阵，但是print功能不像matlab一样强大，不是很直观
[[row[i] for row in matrix] for i in range(4)]

transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])
    
transposed=[]
for i in range(4):
    transposed_row=[]
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    
#上面三种实现matrix的transpose的方式的主要思想都是类似的，但是我还是不太熟悉，需要再回归
    
# del语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)    
del a[2:4]
print(a)    
del a[:] # 注意这个和下面一个del a的区别
print(a)
del a # 这个是删除了实体变量，但是上面一个仅仅是删除了里面的所有元素
print(a)

# 元组和序列
t =12345, 54321, "hello!"
print(t[0])
print(t)
u = (t, (1,2,3,4,5))
print(u)
#从上面就是可以看出，元组定义的时候，是可以不存在圆括号的，
#虽然这个很好，但是还是尽量的避免，因为就是可能引起不必要的bug出现

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k, v)
# 这个倒是一个很有意思的功能，k代表的是key，v代表的是value，
# 还是可以这么使用。
    
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
    
questions = ["name", "quest", "favirite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# 这一个样子的功能，我之前还真的是没有见过呢，   

# 知道了这一种用法，但是还是不明白这个的用法，
for i in range(1, 10, 2):
    print(i)

for i in reversed(range(1, 10, 2)):
    print(i) 
    
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for f in sorted(set(basket)):
    print(f)    
    
print('================Module============')
print("https://www.runoob.com/python3/python3-module.html")
print('================Module============')  
import sys # import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法

print("命令行参数如下：")
for i in sys.argv:
    print(i)
    
print("\n\nPython 路径为：", sys.path, "\n")
 
# 这个功能还是很重要的，但是关于怎么创建一个module，然后import，这个就是需要
# 在后期的过程中再研究一下的   
import support
support.print_func("Yan")

import fib
print(fib.fib(1000))
print(fib.fib2(10))

# todo: 这个就是一件非常有意思的事情，我就是用sys.path查看当前的path的时候，就是可以
# 看到，这个module的py文件是可以放在当前的目录下的了，比如说，我定义support的形式
# 但是诡异的是，我没有办法成功的导入support
# 后来我就是把这个另外一个module fib放到了C:\\ProgramData\\Anaconda3，其实这两个都是
# 在当前的path下面，这个就是一件非常诡异的事情了。

# 这里就是需要修改一下，如果只是单纯的用F9执行相应行的代码，就是会报错的了。
# 但是呢，如果就是使用F5执行整个file里面的代码，同一个path里面的module都是可以正常
# 的使用的了。

"""
https://www.runoob.com/python3/python3-module.html
这个文件里面介绍的包的使用方式，已经包的调用还是非常的好的，就是通俗易懂的感觉。

记住，使用 from Package import specific_submodule 这种方法永远不会有错。事实上，
这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。

如果就是需要定义包，开始结构化的话，就是需要再重新过一下这个功能的了。特别是最后两个小节
"""

print('================IO============')
print("https://www.runoob.com/python3/python3-inputoutput.html")
print('================IO============')  

s="hello, yan"
str(s) # 用户易读的表达形式
repr(s) # 解释器易读的表达形式，但是我还是没看出，这两者有什么区别的了。
str(1/7)
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4)) #rjust是右对齐的意思
    
for x in range(1, 11):
    print("{0:2d}{1:3d} {2:4d}". format(x, x*x, x*x*x))
for x in range(1, 11):
    print("{0:2d}{0:3d} {0:4d}". format(x, x*x, x*x*x))    
# 但是这个例子，他就是没有解释的了，我也不太明白，但是大概是能够看明白的了。

"12".zfill(5)

print("{}网址：'{}！'".format("菜鸟教程", "zongyan.github.io"))

print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
# 上面两行例子就是非常的好，就是说如果是使用这个format的形式，会出现排序的现象
# 系统也是会自动的选择排序的了。

print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 上面这个例子也是很好的，这个就是有点类似于字典的形式的了，但是就是不完全是字典的形式

import math
print("the value of PI is equal to {}.".format(math.pi))
print("the value of PI is equal to {!r}.".format(math.pi))
#!a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr())
print("the value of PI is equal to {0:.3f}".format(math.pi))
#可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化，上面这个就是对
#pi去后三位小数的了。

tab={"Google":1, "Runoob":2, "Taobao":3}
for name, number in tab.items():
    print("{0:20} ==> {1:10d}".format(name, number))
# 明白了，对于这个冒号：后面的数，如果不加d，就是右边空格一段空白，如果后面加了d，就是
# 左边是会空格出一段空白的了，另外，这个0 & 1的意思，就是说，这个其实是一个index的意思
# 而不是其他的意思，所以必须就是从0开始，而且这个数字还是不能不写的

tab={"Google":1, "Runoob":2, "Taobao":3}
print("run:{0[Runoob]:d}; Google:{0[Google]:d}; TaoBae:{0[Taobao]:d}".format(tab))
# 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
# 也可以通过在 table 变量前使用 ** 来实现相同的功能：    
print("Runoob: {Runoob:d}; Google :{Google:d};Taobao:{Taobao:d}".format(**tab))

"""
上面这部分的内容，都是在讲解这个format是怎么使用的，但是呢，我还是对这个冒号前面的
数字还是不够理解，我的理解他是一个index的感觉，然后这个index是从零开始的，这个理解是
正确的。另外一种感觉，这个前面的数值，感觉总是0，这个也就是让我是有点匪夷所思的了，我
就是不太明白，这个冒号前面的数字，到底是一个什么样子的作用存在

我后来看了一下所有的代码，感觉这个冒号前面的数值，就是index的意思，但是呢，对于最后一个
例子中，为什么总是0，我就是有点匪夷所思了，对了，这个也是可以理解的，因为format中就是仅仅
是有一个数值，所以就是总是0的了

也就是说，这个冒号前面的数值，就是index的意思的了。
"""

import math
print("常量PI的近似值是%5.3f" % math.pi)

#str.format()是一个比较新的函数，而是用%形式就是一个比较旧的语法，所以尽量还是使用
#新的语法结构了

name="Runoob"
print(f"hello, {name}")

strr=input("请输入：")
print(f"您输入的是：{strr}")

import os
from pathlib import Path

filepath = "./test.txt"
full_filepath = os.path.join(os.path.dirname(__file__),filepath)

f = open(full_filepath, "w") 
f.write("Python is a good programming language\n Yes, it is!!!\n")
f.close()

"""
这一段程序，就是用来打开某一段代码的程序，本来我的想法，就是使用F9运行，就是可以打开
某一个文件，然后就是可以往里面写字符串的了。
但是呢，就是遇到了这么一个问题，就是我用F9运行的时候，就是不清楚这个文件是创建在哪一个
文件夹中的了，这个就是一个非常让人头疼的问题，就是不清楚这个spyder的path在哪里的了

后来就是没有办法，我就是只是能够使用nick提供的代码了，然后就是用另外一种方式来读写
文件的了。但是呢，这个也是遇到了另外一个问题，就是没有办法使用F9运行特定部分的代
码（__file__）会报错，必须是新建一个file文件，然后就是使用F5的形式，才能够完成代码的
运行
"""

#关于这个文件的读写部分，就是先是在另外一个文件中学习了，这个文件在相同的目录下面，
#名字是叫做r_w_file.py

print('================File methods============')
print("https://www.runoob.com/python3/python3-file-methods.html")
print('================File methods============')  

"""
没有实质性的代码，就是一些介绍性的文字内容，过了一下
"""

print('================OS file methods============')
print("https://www.runoob.com/python3/python3-os-file-methods.html")
print('================OS file methods============')  

"""
没有实质性的代码，就是一些介绍性的文字内容，感觉这部分的内容还是很重要的，
但是我对这部分的代码不太熟悉，没有太多的实质性质的上手的内容
"""
print('================errors execptions============')
print("https://www.runoob.com/python3/python3-errors-execptions.html")
print('================errors execptions============')  

while True:
    try: 
        x =int(input("请输入一个数字，而非字母或其他符号"))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
"""    
这个except倒是挺好用的，不过就是有一个难点，就是需要搞明白可能发生的各种bug，
就是except 后面的这个Error，如果error的种类不对的话，那么这个error就是会被触发
所以，对于不同的error种类来讲，这个确实是一个难点
RuntimeError, TypeError, NameError, ValueError

不过这个问题也是会有一个出路的，因为如果存在多个except的时候，最后一个except是可以
不指明具体的错误内容的，我们就是可以使用这个点，
不过我是觉得，主要还是依靠经验的积累了。
"""  

import sys

for arg in sys.argv[1:]:
    try:
        f=open(arg, 'r')
    except IOError:
        print("cannot open", arg)
    else:
        print(arg, "has", len(f.readlines()), "lines")
        f.close()      
'''
上面这几行代码，我也不知道为什么不能够运行的了，但是主题思想还是很清楚的了，就是先是
执行try里面的代码，如果报错，就是会执行except的代码，并结束，否则就是会执行
else里面的代码，
'''

def this_fails():
    x = 1/0
    
try:
    this_fails()
except ZeroDivisionError as err:
    print("handling run-time error:", err)

try:
    this_fails()
except:
    print("handling run-time error, yan zong") 
"""
通过这个上面的两个例子，就是可以看出，try不仅仅是可以侦测本行的代码，而且是可以侦测这个
调用的函数里面的错误。
另外一个，就是except不一定是需要指定相应的错误的，也是可以不需要输入相应的错误代码的，
这个也是可以使用的了。
"""    

try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')
"""
上面是介绍了这个try-except，try-except-else的使用，最后一个例子是try-except-finally
的使用，就是从中间是可以看出来的，在finally的语句，总是会执行的，这个和else还是有点区别
的
"""

x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
    
try:
    raise NameError("Hi there")
except NameError: 
    print("An exception flew by!")
    raise
    
try:
    raise NameError("Hi there")
except: 
    print("An exception flew by!")
    raise    
    
try:
    raise NameError("Hi there")
except: 
    print("An exception flew by!")
    #raise  
"""
最后两个例子就是可以看到，这个Hi there的异常是抛出来了，这个是由于except里面的raise
引起的，但是我还是不明白，这个的用法，到底是用在哪里的了。
"""      

# 最后，还是有一个“用户自定义异常”，这个我就是暂时是没有看的了，如果以后需要用到，就是
# 再返回来就是可以的了。
# https://www.runoob.com/python3/python3-errors-execptions.html

try:
    raise KeyboardInterrupt
finally:
    print("goodbye, yan")

"""
如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 
except 把它截住，那么这个异常会在 finally 子句执行后被抛出。

换句话说，这个try的语句里面，如果出现了异常，如果没有except的话，就是会被finally抛出
异常；如果有了except的话，就是可以会通过这个except进行抛出的了。

而raise的作用，不像是except那样，是会用比如print的形式，把这个相应的字符串打印出来的
了，而是会直接从系统层面返回一个error，或者是其他什么，就是以traceback开头的

"""    

"""
对这个“定义清理行为”我还是不明白，不知道是个什么都关系，里面的代码我是看得明白的了。
另外，还是提到了“预定义的清理行为”，我的理解，这个在file中使用得比较的多，比如说就是
这个打开了文件之后，一定要记得关闭。现在就是就是可以用with的方式打开文件，他是会
自动关闭的了。
"""

print('================assert============')
print("https://www.runoob.com/python3/python3-assert.html")
print('================assert============')  
# Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
assert True
assert False
assert 1==1
assert 1==2
# 不过这个我还没有想好就是怎么用的了，暂时没有这个try except else finally实用

print('================class============')
print("https://www.runoob.com/python3/python3-class.html")
print('================class============')  
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return "hello world"
    
# 实例化类
x = MyClass()

#访问类的属性和方法
print("MyClass类的属性i为",x.i)
print("MyClass类的方法f输出为",x.f())

#上面这个例子，便是一个简单的类的生命以及使用
#我不太理解这个属性，方法的含义，我就是认为这个
#就是一个类的变量，还有函数了。

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

"""
从这个例子就是可以看出，在class类的定义里面，就是必须是带
有一个def的了。 不过为什么在第一个例子没有__init__()
, 但是第二个例子里面就是有__init()__，我不清楚是为啥
然后呢，在def里面，就是会有一个self，这个
self的作用是个啥，具体我也说不清楚，但是不是一个变量，
下面的这个就是有一定的解释
"""

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
        
t=Test()
t.prt()

"""
类的方法与普通的函数只有一个特别的区别——它们必须有一个
额外的第一个参数名称, 按照惯例它的名称是 self。

self代表的是类的实例，代表当前对象的地址，而self.class则是指向
类

另外，self不是一个关键字，我们是可以换成其他的，也是可以的
"""

class Test:
    def prt(yan):
        print(yan)
        print(yan.__class__)
        
t=Test()
t.prt()

"""
虽然self不是关键字，但是我还是会坚持用self的，延续这个
传统吧
"""

class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说： 我%d岁。"%(self.name, self.age))

#实例化类
p=people("yan", 27, 100)
p.speak()
"""
但是我还是不清楚为什么第一个就是需要使用__init__，第二个
就是不需要使用的了，另外，为什么有的class里面就是会有
__init__，但是有的里面就是没有的了。
"""
#类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说： 我%d岁。"%(self.name, self.age))

#单继承示例
class student(people):
    grade = ""
    def __init__(self, n, a, w, g):
        # 调用父类的函数
        people.__init__(self, n, a, w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s说： 我%d岁，我在都%d年纪。"%(self.name, self.age, self.grade))
        
s = student('ken',10,60,3)
s.speak()


# -------------------------
#类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说： 我%d岁。"%(self.name, self.age))

#单继承示例
class student(people):
    grade = ""
    def __init__(self, n, a, w, g):
        # 调用父类的函数
        people.__init__(self, n, a, w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s说： 我%d岁，我在都%d年纪。"%(self.name, self.age, self.grade))
        
#另一个类，多重继承之前的准备
class speaker():
    topic=""
    name=""
    def __init__(self, n, t):
        self.name=n
        self.topic=t
    def speak(self):
        print("我叫%s,我是一名演说家，我演讲的主题是%s"%(self.name, self.topic))
    
#多重继承的

class sample(speaker, student):
    a= ""
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)
    
test = sample("Tim", 25, 80, 4, "Python")
test.speak()

# 方法重写，就是父类的功能不能够满足你，所以就是可以重新构造子类

class Parent:
    def myMethod(self):
        print("调用父类方法")
        
class Child(Parent):
    def myMethod(self):
        print("调用子类方法")
        
c = Child() # 子类实例
c.myMethod() # 子类调用重写方法
super(Child, c).myMethod() # 用子类对象调用父类已被覆盖的方法
# 这个super倒是一个非常有意思的函数，

#类的私有变量&方法
class JustCounter:
    __secreCount=0 # 因为前面个有两个下划线，所以是私有变量
    publicCount=0 # 公开变量
    
    def count(self):
        self.__secreCount += 1
        self.publicCount += 1
        print(self.__secreCount)
        
counter=JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount) # 这个就是会报错，就是因为这个变量
                    #是类的私有变量
                    
class Site:
    def __init__(self, name, url):
        self.name = name # public
        self.__url= url #private
    
    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self): # 私有方法
        print('这是私有方法')
        
    def foo(self):
        print('这是公共方法')
        self.__foo()
    # 就算是_foo & foo后面部分相同，但是还是不同类

x=Site("Yan Zong", "yzong.com")
x.who()
x.foo()        

# 上面就是给出了私有变量，私有方法的方式，就是在名字前面加两个下划线即可
#如果是加了__，就算名字后面是完全一样的，两者还是不同的变量，或者不同的方法

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

print('================namespace & scope============')
print("https://www.runoob.com/python3/python3-namespace-scope.html")
print('================namespace & scope============')  

import builtins
dir(builtins)

num=1
def fun1():
    global num #要使用global来声明
    print(num)
    num=123
    print(num)
    
fun1()
print(num)
"""
从这个例子中就是可以看出，num刚开始是全局变量，然后就是经过
function中的global声明之后，此时num就是和函数外的num相链接
了，这样子，函数里面就是可以访问函数外面的变量了。

或者话说，就是因为使用这个global之后，这个函数外面的变量和
函数里面的变量是链接在一起了。
"""

"""
外部的变量数值想传递函数内部，其实就是有两种方式，第一种方式就是在函数
内部使用global声明一下；第二种方式就是使用变量传递传递的形式，如solution 2
"""
# solution 1
a = 10
def test():
    global a
    a = a + 1
    print(a)
test()

# solution 2
a = 10
def test(a):
    a = a + 1
    print(a)
test(a)

print('================standard library============')
print("https://www.runoob.com/python3/python3-stdlib.html")
print('================standard library============')  

import os
os.getcwd()#返回当前的工作目录
os.chdir('C:/Users/yan/Documents/Projects/python')#修改当前工作目录
os.getcwd()
"""
以上这个例子，我也是终于明白了之前的读写file总是没有办法成功的原因了
因为之前就是F9直接运行，而工作目录并不是我们想要的文件目录下面，所以
就是需要修改一下文件目录的了。我们可以做如下的实验
"""

import os
os.getcwd()
os.chdir('C:/Users/yan/Documents/Projects/python')#修改当前工作目录

filepath = "./test.txt"
f=open(filepath, 'w')
f.write("Dr. Yan Zong Love Miss. Yuxin Song")
f.close()

"""
对的，上面的实验是验证通过的，当时就是因为这个工作目录不一致导致的了。
"""

#另外，建议使用import os, 而不是from os import *

import os
dir(os)
help(os)
