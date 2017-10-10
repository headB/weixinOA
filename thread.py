import time
import os

print("测试进程")

ret = os.fork()
#print(ret)
##ret里面的值，应该是返回新建的子进程的pid来的。
#print("+++")
#print(os.getpid())

if ret ==0:
   while True:
     print('xx,我已经是子进程来的')
     time.sleep(1)

else:
  while True:
   print("yy，我已经是父进程控制的，应该是")
   time.sleep(2)
