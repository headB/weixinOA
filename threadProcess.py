import time,threading

def printTest():
    global y
    time.sleep(1)
    y=y+'ccc1'
    print(y)
    print("我要并发打印！！")



class newThread(threading.Thread):
    def run(self):
        for i in  range(4):
            global y1
            y1=y1+'ddd1'
            time.sleep(1)
            print("I'm "+self.name+str(i))

#定义全局变量
y='kumanxuan1'
y1='kumanxuan2'

if __name__=="__main__":
    for x in range(5):
        t = threading.Thread(target=printTest)
        t.start()
        #t.join()
    time.sleep(3)
    #print(y)

#创建thread的子类来执行运行多线程、

if __name__ == "__main__":
        t=newThread()
        t.start()
        t1=newThread()
        t1.start()
        #print(y1)
        #print('hello world!!')