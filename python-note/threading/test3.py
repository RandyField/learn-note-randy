import queue
import threading
import time

# 标志位
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    # run方法
    def run(self):

        print ("开启线程：" + self.name)

        # 处理线程名-队列
        process_data(self.name, self.q)

        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()

        # 队列不为空
        if not workQueue.empty():
            # 获取队列
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]

# 线程上锁
queueLock = threading.Lock()

# 创建一个队列对象，给一个最大长度，如果最大长度为非正数，则这个队列长度是无限的
# workQueue = queue.Queue(10)
workQueue=queue.LifoQueue(10)
threads = []
threadID = 1

# 循环创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:  # 循环写入队列
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")