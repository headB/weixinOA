from multiprocessing import Process
import time
print("测试兼容多平台的多进程")

def test():
    for i in range(5):
        print('--test--')
        time.sleep(1)

test1 = Process(target=test)
#Process是大写的，不然变量冲突吧???

test1.start()

##调用对象的方法，就是，拥塞，等待子进程执行完之后我再继续执行
##意义何在？？？
test1.join()

#while True:
#    print("hello!!")
#    time.sleep(1)