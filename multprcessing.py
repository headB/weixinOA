##创建另外一种进程的方法--子类创建子进程。
from multiprocessing import Process
import time

##这里已经是创建了Process的子类了，MyNewProcess就是Process的子类。

##添加参数，看看父进程的处理方法，不过啦，应该是一样的啦。！！
class MyNewProcess(Process):
    def run(self):
        for y in range(6):
            print("---1---")
            time.sleep(1)

p = MyNewProcess()

##这里就是延伸一个问题，就是，上面并没有代入target,就是没有带入函数，
##但是调用start()方法的时候，里面的start()包含了run方法了。
p.start()



for x in range(3):
    print("---2----")
    time.sleep(1)
