#!/usr/bin/python
# -*- coding: UTF-8 -*-

#以上为中文编码

#数据类型

#数字Numbers
a=1
b=2

#字符串String
s='randyfield'

#列表List-【Python 中使用最频繁的数据类型】-列表可以完成大多数集合类的数据结构实现加号 + 是列表连接运算符，星号 * 是重复操作。
testlist=['randy','field',25,'四川省']

#元组Tuple 类似List () 只读
Tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )

#字典Dictionary
dict={}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
tinydict.keys() # 所有键
tinydict.values() # 所有值

# 有时候，我们需要对数据内置的类型进行转换，
# 数据类型的转换，你只需要将数据类型作为函数名即可。

# 运算符 +-*/%  **幂  //取整除

#if else   if elif elif else

# 循环 while for 

import time
ticks=time.time()
localtime=time.localtime(ticks)

# 函数
def FunctionName(args):
    
# 可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
   return
 
# 调用printinfo函数
printinfo( age=50, name="miki" );    

# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2;

# 模块
def print_func(par):
    
# From…import 语句
from modname import name1[, name2[, ... nameN]]

# 搜索路径
#
# 当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
#
#    1、当前目录
#    2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
#    3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
#
# 模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

# "import module_name" 的本质是将"module_name.py"中的全部代码加载到内存并赋值给与模块同名的变量写在当前文件中,
# 这个变量的类型是'module'；<module 'module_name' from 'E:\\PythonImport\\module_name.py'>

# 导入一个模块
import model_name
# 导入多个模块
import module_name1,module_name2
# 导入模块中的指定的属性、方法（不加括号）、类
from moudule_name import moudule_element [as new_name]


#dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
import math
 
content = dir(math)
 
print content

# reload() 函数
#
# 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。

reload(module_name)


# 包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。 
# package_runoob/runoob1.py
def runoob1():
   print "I'm in runoob1"

# package_runoob/runoob2.py
def runoob2():
   print "I'm in runoob2"

#package_runoob/__init__.py
if __name__ == '__main__':
    print '作为主程序运行'
else:
    print 'package_runoob 初始化'

#调用包
from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2
 
runoob1()
runoob2()

#异常
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码


class Employee:
       '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


    # self代表类的实例，而非类

    # empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。
    # 你可以在内部类或外部类使用 Employee.empCount 访问。

    # 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，
    # 当创建了这个类的实例时就会调用该方法

    # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。

    # 名称 Employee 来实例化，并通过 __init__ 方法接受参数。

    emp1 = Employee("Zara", 2000)


class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print "调用父类构造函数"
 
   def parentMethod(self):
      print '调用父类方法'
 
   def setAttr(self, attr):
      Parent.parentAttr = attr
 
   def getAttr(self):
      print "父类属性 :", Parent.parentAttr
#  继承
class Child(Parent): # 定义子类
   def __init__(self):
      print "调用子类构造方法"
 
   def childMethod(self):
      print '调用子类方法'

# 两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
 
counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter.__secretCount  # 报错，实例不能访问私有变量


# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。


