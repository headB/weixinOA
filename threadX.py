import time
import os

print("测试进程")

ret = os.fork()
#print(ret)
##ret里面的值，应该是返回新建的子进程的pid来的。
#print("+++")
#print(os.getpid())

if ret ==0:
   #while range(1,4):
#就是假设父进程已经结束了，子进程还在执行程序，fork函数创建出来的
#父进程就不等了，各位发展。
     print('xx,我已经是子进程来的')
     print('xx,我已经是子进程来的')
     print('xx,我已经是子进程来的')
     print('xx,我已经是子进程来的')
     print('xx,我已经是子进程来的')
     time.sleep(4)

else:
  #while range(1,3):
   print("yy，我已经是父进程控制的，应该是")
   time.sleep(3)

print("the end")
