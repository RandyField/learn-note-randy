#!/usr/bin/python3
#文件名：server.py

#导入 SMTP发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 第三方 SMTP 服务
mail_host="smtp.exmail.qq.com"  #设置服务器
mail_user="zhangdeng@zhiyuanhui.com"    #用户名
mail_pass="Aa287572291"   #口令 

#发送者
sender='zhangdeng@zhiyuanhui.com'

#接受者
receivers=['287572291@qq.com']

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#内容
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')

#发件人
message['From'] = Header("张登 <zhangdeng@zhiyuanhui.com>", 'utf-8')

#收件人
message['To'] =  Header("停摆Dê时针 <287572291@qq.com>", 'utf-8')

#标题
subject="python SMTP 邮件测试"

message['Subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error:无法发送邮件，发生异常,异常信息%s"%str(e))