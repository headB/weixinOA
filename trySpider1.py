from multiprocessing import Pool
import urllib.request
import time
import os

##定义进程池
##定义好数量


def pachong():
    time.sleep(1)
    print("hello world!!")
    #res = urllib.request.urlopen("www.baidu.com")

##程序必写的这句话

def main():

    urlSite = ["http://www.baidu.com","http://163.com","http://www.520it.com"]
##定义进程池
##定义好数量
    #定义好进程池之后，下面就可以写个循环，把任务代入进程池进行。
    pa = Pool(3)
    for x in range(3):
        pa.apply_async(pachong)
    pa.close()
    pa.join()

if __name__ == "__main__":
    main()
    print(os.getcwd())

