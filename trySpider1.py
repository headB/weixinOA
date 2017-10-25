from multiprocessing import Pool
import urllib.request
import time
import os
#引入异步模块
import asyncio

##定义进程池
##定义好数量


def pachong(y):
    time.sleep(1)

    #fileName = "hello world!!"+str(y)
    #print(fileName)
    #print("F:\pythonTest\weixinOA\\"+str(y))
    #f = open("F:\pythonTest\weixinOA\\"+'test'+str(y)+".txt",'w')
    baseDir = os.getcwd()
    f = open('xx'+str(y)+'.txt','w')
    #f = open(baseDir+'\\test'+str(y)+".txt",'w')
    f.write("hello world"+str(y))
    f.close()
    #如何将内容生成在本地文件呢？？问的好，现在就去看看
    #res = urllib.request.urlopen("www.baidu.com")

##程序必写的这句话

def main():

    urlSite = ["http://www.baidu.com","http://163.com","http://www.520it.com"]
##定义进程池
##定义好数量
#定义好进程池之后，下面就可以写个循环，把任务代入进程池进行。
    pa = Pool(3)
    for x in range(3):
            pa.apply_async(pachong,args=(x,))
    pa.close()
    pa.join()

if __name__ == "__main__":
    main()

    #print(os.getcwd())

