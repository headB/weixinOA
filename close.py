import types
print('测试闭包')

def test(num=0):
    print('--1--')
    tmp=1


    def test1(num2):

        print('--2--')
        #xx = tmp+num+num2
        return  tmp+num+num2
        #print(tmp)
        #print(num+num2,sep='',end='---++---\n')


    return test1

ret = test(100)
#print('----3----')

print(ret(200)+ret(300))
#print(ret(300))


##等于300
##测试连续变化带入数值到闭包




##测试迭代器??测试生成器??测试快速循环。
#我的第一个列表生成式。
c= [ x*x+1 for x in range(1,8)]
#print(c)
print(type(c))

d = ([ x*x+1 for x in range(1,8)])
print(d)
print(type(d))

##我的第一个迭代器。
f = ( x*x+1 for x in range(1,8))
print(type(f))

##上面的执行结果。<class 'list'>
#<class 'list'>
#<class 'generator'>

##python的第二种创建生成器的方法  关键字 yield ???
def createNum():
    a = 0
    for x in range(5,10):
        print('hello world!')
        a = a+x
        yield a
        #返回A值.
        print('hello hell')

z=createNum()


#print(next(z))
for x in z:
    print(x)
    print('++++')

##循环了结果发现，在yield这个关键字分两段，前面和yield是一段结果，然后后面又一段执行结果。

class cat:

    def __init__(self):
        self.name = 'kuManMao'

    def name(self):
        print("I am a little cat!")

def eat(self):
    print("I am eating!!%s" %(self.name))

tom = cat()

##测试使用types.MethodType这个函数。

tom.eat = types.MethodType(eat,tom)

tom.eat()



