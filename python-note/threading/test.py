#!/usr/bin/python3
import threading
# import _thread #_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
import time

#为线程定义一个函数

def print_time(thredName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s计数器：%d"%(thredName,count))
        print("%s:%s"%(thredName,time.ctime(time.time())))

#创建两个线程

try:
    threading._start_new_thread(print_time,("线程1",2))
    threading._start_new_thread(print_time,("线程2",4))
except expression as identifier:
    print("Error:无法启动线程")

while 1:
    pass



    # threading.currentThread(): 返回当前的线程变量。
    # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

    # run(): 用以表示线程活动的方法。
    # start():启动线程活动。

    # join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    # isAlive(): 返回线程是否活动的。
    # getName(): 返回线程名。
    # setName(): 设置线程名。
