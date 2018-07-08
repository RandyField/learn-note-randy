from flask import Flask,render_template

app=Flask(__name__)


@app.route('/<name>')
def hello(name):
    if name=="randy":
        return render_template('index.html',name=name)

    else:
        return render_template('index.html',name='world')

if __name__=="__main__":
    app.run()

# render_template把 Jinja2 模板引擎集成到了程序中
# render_template 函数的第一个参数是模板的文件名
# 随后的参数都是键值对，表示模板中变量对应的真实值。

