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
    
    
    
    
    