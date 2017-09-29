import time
import os

print("测试进程")

ret = os.fork()

print(ret)