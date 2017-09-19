print("测试python里面的property用法")

class score:
    def __init__(self):
        self.__num = 0
        print("默认分数是0分")

    @property
    def score(self,score):

        #做了一个简单的判断，只能接收int
        if not type(score)==int:
            print("error value")
            exit()
        self.__num = score
        print("success to set score")
    @score.setter
    def score(self):
        return self.__num

 #   num = property(getScore,setScore)

tom = score()
#tom.setScore(60)
#print(tom.getScore())
tom.num = 80
print(tom.num)


