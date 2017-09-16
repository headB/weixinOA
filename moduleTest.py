import pythonMysql
from pythonMysql import testMysql
from classTest import *
from xuanPrint import *
#from xuanPrint import package2
#import xuanPrint
print("这个是测试模块导入的")

#pythonMysql.testMysql()


class VarX:


 def __init__(self):
   self.name=''
   self.__nickName = 'beetle'

 def __printX(self):
    name = 'kumanxuan6666666666'
    print(self.__nickName)
    print(name)

 def test1Print(self):
     __string = 'lizhixuan'
     print(__string)

 def testPrint(self):
    num = 24
    self.name = 'kumanxuan'
    self.__printX()
    return self.name

 def test2Print(x):
    name = 'kumanjin'
    return name

 def __str__(self):
    return "你就是最棒棒了我！！"

class bigCat(VarX):
 def testPrint(self):
     print("this is bigCat speak!!")
     super().testPrint()
#testMysql()

print("我现在正在用window10的系统，pycharm工具来编写代码的！！")

test = VarX()
val = test.testPrint()

package2.printWorld.cat()

printTest.xuanxuan()

#package2.printWorld.cat()


#print(val)

#print(test.test2Print())

#print(test)

#print(test.name)

#tom = cat()

#jack = classTest.dog()

#tom.play()

#bigTom = bigCat()

#bigTom.testPrint()

#xuanPrint.printTestInit()

#sendMsg.sendMsg()

#jack.shout()




