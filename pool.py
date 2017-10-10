from multiprocessing import Pool
import os
import random
import time

##定义一个普通函数
def worker():
    #那下面这里是这样定义咯，随机返回一个数来循环。
    for i in range(10):
        print("-=--pid =%d "%(i))
        time.sleep(1)
#
pool = Pool(3)

for i in range(10):
    pool.apply_async(worker)


##close是什么???
pool.close()
pool.join()

