from multiprocessing import Process
import time
print("测试兼容多平台的多进程")

def test():
    while True:
        print('--test--')
        time.sleep(1)

test1 = Process(target=test)
#Process是大写的，不然变量冲突吧???

test1.start()

while True:
    print("hello!!")
    time.sleep(1)