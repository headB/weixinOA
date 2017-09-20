print('测试闭包')

def test(num):
    print('--1--')

    def test1(num2):
        print('--2--')
        print(num+num2)

    return test1

ret = test(100)
print('----3----')

ret(200)

##等于300
