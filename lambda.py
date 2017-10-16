##测试匿名函数和多态
def funcT(x,y,opt):
    print(x)
    print(y)
    print(opt(x,y))

funcT(4,5,lambda x,y:x+y)
