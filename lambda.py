##测试匿名函数和多态
def funcT(x,y,opt):
    print(x)
    print(y)
    print(opt(x,y))

def funcX():
    print("test the @")

funcT(4,5,lambda x,y:x+y)

print(funcT.__name__)

def demo(func):
    def wrapper():
        func()
        ##这里是可以添加新功能的！！
        def testFunction():
            print("I am a new function!!")
        testFunction()

    return wrapper

funcX = demo(funcX)

print(funcX.__name__)

funcX()

@demo
def printMyName():
    print("I am kumanxuan!!")


printMyName()