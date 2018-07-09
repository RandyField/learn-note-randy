# 从flask包导入一个Flask类
from flask import Flask,url_for,request,render_template,Markup

# 将 __name__ 参数传给 Flask 类的构造函数
# 创建了一个程序实例 app
# 也就创建了一个 Flask 集成的开发 Web 服务器
app=Flask(__name__)
# app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。
# 让flask.helpers.get_root_path函数通过传入这个名字确定程序的根目录，以便获得静态文件和模板文件的目录。
# __name__是模块文件名
# __main__是运行文件名



# Web 浏览器把请求发送给 Web 服务器
# Web 服务器再把请求发送给 Flask 程序实例
# 那么程序实例就需要知道对每个 URL 请求应该运行哪些代码
@app.route("/")
# @app.route("/index")
def index():
    return "hello world!"

@app.route("/randy")
def randy():
    return "hello randy!"

@app.route("/hello/<user_name>")
def hello(user_name):
    print("|")
    return '<h1>hello,%s !</h1>'%user_name

with app.test_request_context():
    print(url_for('index'))
    print(url_for('randy'))
    print(url_for('hello',user_name='kobe'))
    print(url_for('static',filename='test.css'))
    # print(url_for('mywebapp',filename='test.css')) 只有static有效，其余名称无效
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        return "POST"
    else:
        return "GET"
# 模板渲染
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

@app.route('/markup/html')
def haha():
    return Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
    #输出Hello <blink>hacker</blink>!
    
# 当我们运行该脚本的时候
# 启动 Flask 集成的开发 Web 服务器
if __name__=="__main__":
    # app.run()
    app.run(host='0.0.0.0',port=8080,debug=False)

# Flask 提供的 Web 服务器不适合在生产环境中使用，后面我们会介绍生产环境中的 Web 服务器。