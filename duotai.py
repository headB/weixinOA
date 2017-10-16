class F1:
    def show(self):
        print("this is print F1")

class S1(F1):
    def show(self):
        print("this is print S1")

class S2(F1):
    def show(self):
        print("this is print S2")

class testClass:
    def show(self):
        print('this is kuManXuan test')

def funcC(x):
    x.show()

s1 = S1()
funcC(s1)

