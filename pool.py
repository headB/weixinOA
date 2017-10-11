from multiprocessing import Pool,Queue
import os
import random
import time


##假设在这里增加函数，应该不会被重复的，因为按照fork的方法，写在前面的代码应该不会复制过去执行。
##针对上面的言论，这个全局变量的函数，linux只会执行一次，所以，注意小心一点了。
##window和linux运行结果不一样，尽量以linux为准。
def printTest2():
    print("can program runing me ???if can, how many times??")

#printTest2()

##经过测试，上面如果调用了函数的话，在每一个进程都会被执行一次，哎，晕。。。。
##那意思就是，函数可以写好，但是不要随便调用，要调用的话，用下面那个pool.apply_async调用。

##定义一个普通函数
def worker(num):
    #那下面这里是这样定义咯，随机返回一个数来循环。
    for i in range(1):
        print("-=--pid =%d and num is %s"%(os.getpid(),num))
        value = os.getpid()
        #print(q)
        #q.put(value)
        time.sleep(1)
#

#我现在意识到，__name__是一个多么重要的函数，可以识别到当前执行的文件。
if __name__ == "__main__":
    pool = Pool(3)
    for i in range(3):
        pool.apply_async(worker,(i,))

    ##close是什么???
    pool.close()
    pool.join()
    printTest2()
    print("this is for a test!!")

#print(q.get(True))

##测试了，然后发现，是window的问题，在linux上是没有问题的。


def printTest():
    print("this is print by function printTest!!")

#printTest()

print(__name__)
#print("kumanxuan!!")
#q = Queue()
#q.put('xx')
#q.put('yy')
#q.get()
#q.get()

