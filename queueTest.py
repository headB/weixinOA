from multiprocessing import Process,Queue
import time,random,os

def write(q):
    for value in ['A','B','C']:
        q.put(value)
        print("this is %s"%value)
        time.sleep(random.random())



def read(q):
    while True:
        value = q.get(True)
        print("get %s" %value)

if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))


    pw.start()
    #启动子进程的PW


    pr.start()

    pw.join()

    pr.terminate()