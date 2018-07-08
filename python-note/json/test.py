#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : '百度',
    'url' : 'http://www.baidu.cn'
}

#转换为json字符串
json_str = json.dumps(data)

print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])


# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：

# # 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)

# # 读取数据
# with open('data.json', 'r') as f:
#     data = json.load(f)
