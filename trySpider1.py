from multiprocessing import Pool
import urllib.request
##定义进程池
##定义好数量
pa = Pool(3)

def pachong():
    res = urllib.request.urlopen("www.baidu.com")

##程序必写的这句话

def main():
    pass

if __name__ == "__main__":
    pass