#!/usr/bin/python3
#文件名：server.py

#导入 socket、sys模块
import socket
import sys

#创建socket对象
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名
host=socket.gethostname();

port=9999

#绑定端口
serversocket.bind((host,port))

print("主机%s，监听%d端口 "%(host,port))

#设置最大连接数，炒股后排队
serversocket.listen(5)

while True:
    #建立客户端连接
    clientsocket,addr=serversocket.accept()

    print("客户端：%s 连接了"%str(addr))

    clientsocket.send(("欢迎连接").encode('utf-8'))

    clientsocket.close()


# 协议	功能用处	端口号	Python 模块
# HTTP	网页访问	80	httplib, urllib, xmlrpclib
# NNTP	阅读和张贴新闻文章，俗称为"帖子"	119	nntplib
# FTP	文件传输	20	ftplib, urllib
# SMTP	发送邮件	25	smtplib
# POP3	接收邮件	110	poplib
# IMAP4	获取邮件	143	imaplib
# Telnet	命令行	23	telnetlib
# Gopher	信息查找	70	gopherlib, urllib