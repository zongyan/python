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