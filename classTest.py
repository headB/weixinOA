##crate a new class
__all__ = ['cat']
class cat:

  print('现在就是假如我不创建一个对象，不实例，直接写语句，看看会有什么结果。！！')

  def eat(p):
    print("我正在吃")

  def sleep(p):
    print("我正在睡觉，请不要打扰我啦。！！")

  def play(self):
    print("我正在和小伙伴玩，不用烦我啦。！！%s" %(132))

class dog:
  def shout(self):
     print("wang!wang!wang!")
     print("I am single dog!!miao miao %s")

def printTestX():
    print("this is classTest of one function")
##create a new instance

#tom = cat()
#jack = dog()

#tom.eat()
#tom.sleep()
#tom.play()

##这个是测试用type创建类，然后再创建一个实例。

##成功创建了一个元类，嗯嗯，不错。！！
def printWorld(x):
    print('hello world - XD - X2')

printX = type("printX2",(),{"num":printWorld})

test2 = printX()

test2.num()

##利用元类去定义类，不过增加了继承，

def print2(x):
    print('this is the send function to print')

test3 = type('xx',(printX,),{'cc':print2})

test4 = test3()

test4.cc()

test4.num()