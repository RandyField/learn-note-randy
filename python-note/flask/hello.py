# 从flask包导入一个Flask类
from flask import Flask

# 将 __name__ 参数传给 Flask 类的构造函数
# 创建了一个程序实例 app
# 也就创建了一个 Flask 集成的开发 Web 服务器
app=Flask(__name__)

# Web 浏览器把请求发送给 Web 服务器
# Web 服务器再把请求发送给 Flask 程序实例
# 那么程序实例就需要知道对每个 URL 请求应该运行哪些代码
@app.route("/")
# @app.route("/index")
def index():
    return "hello world!"

@app.route("/randy/")
def randy():
    return "hello randy!"

@app.route("/<user_name>")
def hello(user_name):
    print("|")
    return '<h1>hello,%s !</h1>'%user_name
    
# 当我们运行该脚本的时候
# 启动 Flask 集成的开发 Web 服务器
if __name__=="__main__":
    # app.run()
    app.run(host='0.0.0.0',port=8080,debug=False)

# Flask 提供的 Web 服务器不适合在生产环境中使用，后面我们会介绍生产环境中的 Web 服务器。