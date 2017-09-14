print("下面演示的关于打印输出三角形的~！！！")

#first to define the length of triangle

def triangle(leng):
 space = ' '
 d = leng - 1
 for x in range(leng):
  if(x==0):
   print((leng-x)*space+"*"+(x-1)*space)
  elif(x<d):
   print((leng-x)*space+"*"+(x-1)*space+"*"+(x-1)*space+"*")
  else:
   print((leng-x)*space+(x)*2*"*"+"*")
#  print(space*x)

hight = int(input("请输入你需要定制的三角形高度:"))

triangle(hight)

def test(a=33):
  print(a)

test()
