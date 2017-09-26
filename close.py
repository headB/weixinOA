print('测试闭包')

def test(num):
    print('--1--')

    def test1(num2):
        print('--2--')
        print(num+num2)

    return test1

#ret = test(100)
#print('----3----')

#ret(200)

##等于300



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


print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))





