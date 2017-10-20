from multiprocessing import Pool
import urllib.request
import xuanPrint.package2
import xuanPrint

##定义进程池
##定义好数量
pa = Pool(3)

xuanPrint.sendMsg.sendMsg()
newClass = xuanPrint.package2.printWorld.dog()

newClass.testMod()

def pachong():
    pass
    #res = urllib.request.urlopen("www.baidu.com")

##程序必写的这句话

def main():
    pass

if __name__ == "__main__":
    pass