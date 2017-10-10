##创建另外一种进程的方法--子类创建子进程。
from multiprocessing import Process
import time

##这里已经是创建了Process的子类了，MyNewProcess就是Process的子类。
class MyNewProcess(Process):
    def run(self):
        while True:
            print("---1---")
            time.sleep(1)

p = MyNewProcess()

##这里就是延伸一个问题，就是，上面并没有代入target,就是没有带入函数，
##但是调用start()方法的时候，里面的start()包含了run方法了。
p.start()



while True:
    print("---2----")
    time.sleep(1)