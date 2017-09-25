print("测试python里面的property用法")

class score:
    def __init__(self):
        self.__num = 0
        print("默认分数是0分")

    @property
    def scoreX(self,score):

        #做了一个简单的判断，只能接收int
        if not type(score)==int:
            print("error value")
            exit()
        self.__num = score
        print("success to set score")
    @scoreX.setter
    def score2(self):
        return self.__num

 #   num = property(getScore,setScore)

tom = score()
#tom.setScore(60)
#print(tom.getScore())
tom.num = 80
print(tom.num)

##针对上面的代码，针对修饰器的知识认知，然后修改了一下个别函数的名字，然后证明可以用。

##自己定义一个修饰器。

def weapon(functionName):
  def warpTest():
    functionName()
    value= 'this is run a weapon function!!'
    print(value)
  return warpTest
 #    print(name)
 #   print(ammo)
 #   print(who)

#weapon()

##哈哈哈，一看我自己就知道是新手啦，写修饰器的时候，居然后面写了括号
@weapon
def ak():
    print('I am kumanxuan')


ak()



##OK，自己成功定义了一个修饰器函数。

#设置一个函数，来尝试设置值和获取值。
#修饰器是和闭包结合??

##尝试设置一个连续闭包。

def test1(num1):
    def test2(num2):
        def test3(num3):
            return num1+num2+num3
        return test3
    return test2


#xx = test1(100)

#c = xx(200)

#print(c(300))

##答案是600
##测试成功。！！！

##采用新的方式去尝试运行函数试试（闭包）
#OK!成功。
xx = test1(100)(200)(300)
print(xx)