import time
import threading

# 当前时间戳-时间戳单位最适于做日期运算
print(time.time())

print(time.localtime(time.time()))

time.sleep(2)
print(time.localtime())

print(time.asctime())


print ("本地时间为 :", time.asctime( time.localtime(time.time()) ))

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))  

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

import calendar
cal = calendar.month(2018, 7)
print ("以下输出2016年1月份的日历:")
print (cal)

    # %y 两位数的年份表示（00-99）
    # %Y 四位数的年份表示（000-9999）
    # %m 月份（01-12）
    # %d 月内中的一天（0-31）
    # %H 24小时制小时数（0-23）
    # %I 12小时制小时数（01-12）
    # %M 分钟数（00=59）
    # %S 秒（00-59）
    # %a 本地简化星期名称
    # %A 本地完整星期名称
    # %b 本地简化的月份名称
    # %B 本地完整的月份名称
    # %c 本地相应的日期表示和时间表示
    # %j 年内的一天（001-366）
    # %p 本地A.M.或P.M.的等价符
    # %U 一年中的星期数（00-53）星期天为星期的开始
    # %w 星期（0-6），星期天为星期的开始
    # %W 一年中的星期数（00-53）星期一为星期的开始
    # %x 本地相应的日期表示
    # %X 本地相应的时间表示
    # %Z 当前时区的名称
    # %% %号本身