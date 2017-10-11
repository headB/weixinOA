from multiprocessing import Pool
import os
import random
import time

##定义一个普通函数
def worker(num):
    #那下面这里是这样定义咯，随机返回一个数来循环。
    for i in range(1):
        print("-=--pid =%d and num is %s"%(os.getpid(),num))
        time.sleep(1)
#

if __name__ == "__main__":
    pool = Pool(3)

    for i in range(11):
        pool.apply_async(worker,(i,))

    ##close是什么???
    pool.close()
    pool.join()

