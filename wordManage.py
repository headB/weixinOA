name = []
x = 1
while x>0:
  print ("\n\n")
  print ("+++++++++++++++++++++")
  print ("1是添加名字")
  print ("2是显示当前所有名字")
  print ("3是删除某个名字")
  print ("+++++++++++++++++++++")
  print ("\n\n") 
  

  indexs = input("请输入选择你需要的服务:")
  if indexs.isdigit():
    pass
  # print("你输入的内容为数字:"+indexs)
  else:
    print("你输入了不是数字的选项，请你输入数字:")
    continue
  index = int(indexs) 
  if index==1:
    names = input("请添加姓名:")
    name.append(names)
    names = []

  elif index==2:
    print("========")
    print(name)
    print("========")

  elif index==3:
   removes = input("请输入删除的名字,直接输入名字就可以了:")
   #remove=int(removes)  //this is just for a test
   for x1 in name:
     if removes==x1:
        name.remove(removes)
