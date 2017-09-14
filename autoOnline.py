import pymysql
import re
import sys


class shortInputEx(Exception):
  def __init__(self,ip):
   self.ip=ip


##首先是数据库连接，新建一个数据库
db=pymysql.connect("localhost",'root','kumanxuan@gzitcast','xingzheng',charset='utf8')
mysql = db.cursor(pymysql.cursors.DictCursor)
print("this py is about autoOnline when get a new ip address")

ipAddressInfo = input("请输入你要设置上网的ip地址:")
print(ipAddressInfo)

##set a 正则匹配
matchInfo = re.search(r"^192\.168\.([1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\.(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))$",ipAddressInfo)


##将正则匹配的结果通过下面这些流程简单判断一下
##这个过程中，引用了一个自定义的异常类，见上方的 showInputEx(Exception)
##其实坦白讲，下面这个try去判断ip地址，是多9余的，只是我自己用来测试自己刚学到的《自定义异常类》
try:
  if(not matchInfo):
     raise shortInputEx(ipAddressInfo)
except  shortInputEx as BB:
     print('你输入的ip地址有误，这是你刚刚输入的ip地址%s' %(BB.ip))
else:
     print('check it out,OK')


##这里又重复一下去验证判断ip地址，重复的，仅仅用于自己学以致用中测试
if(matchInfo):
  print("got it")
else:
  print("ERROR,you input a wrong IP")
  sys.exit()


##如果流程能到这里，就可以使用单独去检测该获取到的ip是否存在在数据库中
##这台服务器里面是有专门记录所有小码哥课室网段的数据表。
ipInfo = matchInfo.group(0)
ipRange = re.split(r'\.',ipInfo)
print(ipRange)
sql = "select * from classroom where ipAddress = '%s'" %(ipRange[2])

##上面那个是对比数据库中有没有这IP地址段。

try:
  mysql.execute(sql)
  result = mysql.fetchall()
  if(result):
    print(result)
  else:
    print("error,404 not found")
  

except:
  print("error")

if(not result):
  print("bye bye!!")
  sys.exit

##然后就没有下文了。！！！请自由发挥。


