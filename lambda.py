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

#print(funcX.__name__)

funcX()

@demo
def printMyName():
    print("I am kumanxuan!!")


printMyName()

def testReturn():
    def test2():
        def tt():
            print('cccc')
        str="I am kumanxuan2222222222!!"
        #return tt
        #差点忘记了，就是如果这里使用了return的话，后面的代码就不执行的啦。！！
        #哎呀，没记性啊。~！
        tt()
    return test2


strs = testReturn()

strs()

##OK，顺便验证了，真的是，在python里面，也是一切皆为对象。
print(testReturn)

#print(testReturn())

#print(testReturn())

