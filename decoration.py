##测试装饰器

def addI(before):
    def wrapper():
     return "<i>"+before()+"</i>"
    return wrapper

def addB(before):
    def wrapper():
     return "<b>"+before()+"</b>"
    return wrapper

def addBr(before):
    def wrapper():
     return "<br>"+before()
    return wrapper


@addBr
@addB
@addI
def printX():
    return "my name is kumanxuan"

print(printX())