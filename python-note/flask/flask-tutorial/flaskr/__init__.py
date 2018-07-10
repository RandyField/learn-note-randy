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

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app
    