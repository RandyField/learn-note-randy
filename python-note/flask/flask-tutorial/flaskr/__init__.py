# 包含应用工厂
# __init__.py标识文件夹是看作为一个包

import os
from flask import Flask

def create_app(test_config=None):
    # 创建注册一个应用
    app=Flask(__name__,instance_relative_config=True) 
    #__name__当前python模块的名称-应用需要知道在哪里设置路径 
    # instance_relative_config=True告诉应用 配置文件是相对于实例文件夹的相对路径

 

    #设置一个应用的默认配置
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite')
    )

    
    # SECRET_KEY 是被 Flask 和扩展用于保证数据安全的。
    # 在开发过程中， 为了方便可以设置为 'dev' ，
    # 但是在发布的时候应当使用一个随机值来 重载它。

    # DATABASE SQLite 数据库文件存放在路径。
    # 它位于 Flask 用于存放实例的 app.instance_path 之内。


    # test_config为测试的配置文件，正式部署时test_config为空，则加载config.from_pyfile
    if test_config is None:
        # 使用config.py中的值来重载默认配置
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        # 确保app.instance_path exist
        # Flask 不会自动 创建实例文件夹，但是必须确保创建这个文件夹，
        # 因为 SQLite 数据库文件会被 保存在里面。
        os.makedirs(app.instance_path)
    except OSError:
        pass



    @app.route('/hello')
    def hello():
        return 'hello,randy,welcome flask web'

    # @app.before_request
    # def before_request():
    #     from . import db
    #     db.init_app(app)
    return app
    