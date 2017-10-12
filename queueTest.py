from multiprocessing import Process,Queue
import time,random,os

def write(q):
    for value in ['A','B','C']:
        time.sleep(1)
        q.put(value)
        print("this is %s"%value)
        time.sleep(random.random())

def write1(q):
    for value in ['c','A','B']:
        time.sleep(3)
        q.put(value)
        print("this is %s"%value)
        time.sleep(random.random())



def read(q):
    while True:
        value = q.get(True)
        print("get %s" %value)

if __name__ == "__main__":
    q = Queue()
    q1= Queue()
    pw = Process(target=write,args=(q,))
    pw1 = Process(target=write1,args=(q1,))
    
    pr = Process(target=read,args=(q,))
    pr1 = Process(target=read,args=(q1,))


    pw.start()
    pw1.start()
    #启动子进程的PW

#pw.join()
    pr.start()
    pr1.start()
##为什么一定要写在这个位置呢？？？请问、？？
##大概懂了是什么意思了，就是，假如，这个位置不设置一个拥塞等待的话，
##下面的pr.teminate由于不是子线程的一部分，会继续执行，然后退出。   
    pw.join()
    pw1.join()

    pr.terminate()
    pr1.terminate()
