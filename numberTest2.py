for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print("%d 等于 %d * %d" %(num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
       print(num, '是一个质数')
#   if num%i != 0:
#      print("这个数是素数的啦!")

def autoScript(input=''):
 str = '''
 #!/usr/bin/expect
 set timeout 15
 spawn ssh admin@192.168.113.254
 
 expect {
 "(yes/no)?" {send "yes\\r"}
 "Password:" {send "kumanxuan@gzit\\r"}
 }
 %s
 
 #expect eof
 interact
 '''
 return str
respond = """
反正这里输入一些特定的语句，用来生成脚本的，其实我也不懂python能不能直接执行shell语句。
"""
print(autoScript() %(respond))

a= [100]
def test(num):
  num=num+num
  print(num)


test(a)

print(a)
