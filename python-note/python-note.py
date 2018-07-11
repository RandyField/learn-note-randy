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






# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# 【虚拟环境】

# 建议在开发环境和生产环境下都使用虚拟环境来管理项目的依赖。
# 为什么要使用虚拟环境？随着你的 Python 项目越来越多，你会发现不同的项目会需要 不同的版本的 Python 库。同一个 Python 库的不同版本可能不兼容。
# 虚拟环境可以为每一个项目安装独立的 Python 库，这样就可以隔离不同项目之间的 Python 库，也可以隔离项目与操作系统之间的 Python 库。
# Python 3 内置了用于创建虚拟环境的 venv 模块。


# 【创建一个虚拟环境】

# 1、创建一个项目文件夹
# 2、创建一个虚拟环境
# 3、创建完成后项目文件夹中会有一个 venv 文件夹
# mkdir mywebapp
# cd mywebapp
# python -m venv venv

# 【激活虚拟环境】

# 在开始工作前，先要激活相应的虚拟环境：
# 
# Linux下为. venv/bin/activate
# 在 Windows 下：
# venv\Scripts\activate

# 步骤，cd到目录，执行venv\Scripts\activate

# pip list


# 【安装Flask】

# 在已激活的虚拟环境中可以使用pip install Flask 来安装Flask


# 【活在当下】---使用最新版本的Flask

# 如果想要在正式发行之前使用最新的 Flask 开发版本，可以使用如下命令从主分支 安装或者更新代码：

# pip install -U https://github.com/pallets/flask/archive/master.tar.gz

# 【导出FLASK_APP 环境变量】
# 可以使用 flask 命令或者 python 的 -m 开关来运行这个应用。在 运行应用之前，需要在终端里导出 FLASK_APP 环境变量:

# $ export FLASK_APP=hello.py
# $ flask run
#  * Running on http://127.0.0.1:5000/

# 如果是在 Windows 下，那么导出环境变量的语法取决于使用的是哪种命令行解释器。 在 Command Prompt 下:

# C:\path\to\app>set FLASK_APP=hello.py

# 在 PowerShell 下:

# PS C:\path\to\app> $env:FLASK_APP = "hello.py"

# 还可以使用 python -m flask:

# $ export FLASK_APP=hello.py
# $ python -m flask run
#  * Running on http://127.0.0.1:5000/

# 这样就启动了一个非常简单的内建的服务器。




# 【外部可见的服务器】

# 运行服务器后，会发现只有你自己的电脑可以使用服务，而网络中的其他电脑却 不行。
# 缺省设置就是这样的，因为在调试模式下该应用的用户可以执行你电脑中 的任意 Python 代码。

# 如果你关闭了调试器或信任你网络中的用户，那么可以让服务器被公开访问。
# 只要在命令行上简单的加上 --host=0.0.0.0 即可:

# flask run --host=0.0.0.0  

# 这行代码告诉你的操作系统监听所有公开的 IP 。这样只要开放了5000端口，任何能访问的ip都能访问



# 【非法导入名称】

# FLASK_APP 环境变量中储存的是模块的名称，
# 运行 flask run 命令就 会导入这个模块。
# 如果模块的名称不对，那么就会出现导入错误。
# 出现错误的时机是在 应用开始的时候。
# 如果调试模式打开的情况下，会在运行到应用开始的时候出现导入 错误。
# 出错信息会告诉你尝试导入哪个模块时出错，为什么会出错。
# 最常见的错误是因为拼写错误而没有真正创建一个 app 对象。


# 【调试模式】

# 虽然 flask 命令可以方便地启动一个本地开发服务器，但是每次应用代码 修改之后都需要手动重启服务器。
# 这样不是很方便， Flask 可以做得更好。
# 如果你打开 调试模式，那么服务器会在修改应用代码之后自动重启，
# 并且当应用出错时还会提供一个 有用的调试器。

# 如果需要打开所有开发功能（包括调试模式），
# 那么要在运行服务器之前导出 FLASK_ENV 环境变量并把其设置为 development:

# $ export FLASK_ENV=development
# $ flask run

# （在 Windows 下需要使用 set 来代替 export 。）
# 这样可以实现以下功能：

#     激活调试器。
#     激活自动重载。
#     打开 Flask 应用的调试模式。

# 还可以通过导出 FLASK_DEBUG=1 来单独控制调试模式的开关。


# 【唯一的 URL / 重定向行为】

# 以下两条规则的不同之处在于是否使用尾部的斜杠。:

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# projects 的 URL 是中规中举的，尾部有一个斜杠，看起来就如同一个文件夹。 访问一个没有斜杠结尾的 URL 时 Flask 会自动进行重定向，帮你在尾部加上一个斜杠。

# about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误。这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。


# 【URL 构建】

# url_for() 函数

# 【HTTP 方法】
# from flask import request

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':

# 【静态文件】
# url_for('static', filename='style.css')

# 【渲染模板】
# from flask import render_template

# @app.route('/hello/')
# @app.route('/hello/<name>')

# Flask 会在 templates 文件夹内寻找模板。因此，如果你的应用是一个模块， 那么模板文件夹应该在模块旁边；如果是一个包，那么就应该在包里面：

# 情形 1 : 一个模块:

# /application.py
# /templates
#     /hello.html

# 情形 2 : 一个包:

# /application
#     /__init__.py
#     /templates
#         /hello.html

# 【请求数据】
# 在 Flask 中由全局 对象 request 来提供请求信息

# 【请求对象】
# 【文件上传】
# 【Cookies】
# 【重定向和错误】


# 初始化数据库文件

# 现在 init-db 已经在应用中注册好了，可以与 flask 命令一起使用了。 使用的方式与前一页的 run 命令类似。

# Note

# 如果你还在运行着前一页的服务器，那么现在要么停止该服务器，要么在新的 终端中运行这个命令。
# 如果是新的终端请记住在进行项目文件夹【激活环境， 参见 激活虚拟环境】 。同时还要像前一页所述设置 FLASK_APP 和 FLASK_ENV 。

# 运行 init-db 命令：

# flask init-db
# Initialized the database.

# 现在会有一个 flaskr.sqlite 文件出现在项目所在文件夹的 instance 文件夹 中。