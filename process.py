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
##意义何在？？？还是有意思的，可能添加超时，超时之后，父进程继续执行程序

#test1.join()

#然后到主进程执行
#print("终于等到你！！！")

##上面的执行过程就是，等到海枯石烂了，我都继续等你。

##然后现在开始，我只等你3秒，然后我就走了。

test1.join(3)

print("不知道有没有等到了，如果等到你过来了，可能我们已经在一起，不然我就自己一个人走了。")

##我是意思，请向我看齐
##但是还是说明了一个问题，就是，父进程还是会执行程序，但等到最后，父进程还是会等子进程。

