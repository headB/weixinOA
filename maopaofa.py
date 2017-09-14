import copy
import re
print("下面是冒泡法")
#num = [85,11,15,65,48,72,98,121,54,31,21]
#num2 = copy.copy(num)

def maopao(num):
 for indexx in range(len(num)):
  for index in range(len(num)-indexx-1):
      tmp1 = int(num[index])
      tmp2 = int(num[index+1])
      if tmp1>tmp2:
         num[index+1] = tmp1
         num[index] = tmp2
      else:
         num[index] = tmp1
         num[index+1] = tmp2
 print(num)


#初始化一个待处理的数组状态
status=False
while(not status):
  num = input("请输入一组数字序列，以逗号为隔开:")
  result = re.search("^(\d+,)+\d+$",num)
  if(result):
    print("有结果:")
    status=True
  else:
    print("你输入的格式有误:请重新输入:")

numArray = num.split(',')

maopao(numArray)

