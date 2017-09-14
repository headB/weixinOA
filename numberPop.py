num = [2,3,4,5]

for x in num:
  for y in num:
      for z in num:
        if(z!=y and  z!=x and x!=y):
           print(x,y,z)

