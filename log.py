import time
import subprocess
print("以下展示的是关于历史消息（日志）系统原理")
#date=time.asctime(time.localtime())
date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(date)
#file = open("log.txt","a+")
file = open("log.txt","a+")

#sysinfo = os.system('uptime')
sysinfo = subprocess.getoutput("uptime")
file.write("%s\n" %sysinfo )

file.close()

