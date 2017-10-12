import time,threading

def printTest():
    print("我要并发打印！！")

class newThread(threading.Thread):
    def run(self):
        for i in  range(4):
            time.sleep(1)
            print("I'm "+self.name+str(i))


#if __name__=="__main__":
#    for x in range(5):
#        t = threading.Thread(target=printTest)
#        t.start()

#创建thread的子类来执行运行多线程、
if __name__ == "__main__":
        t=newThread()
        #t.setDaemon(False)默认不用设置
        t.start()
        t1=newThread()
        #t1.setDaemon(False)
        t1.start()
        print('hello world!!')