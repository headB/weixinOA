import time,threading

def printTest():
    print("我要并发打印！！")


if __name__=="__main__":
    for x in range(5):
        t = threading.Thread(target=printTest)
        t.start()

