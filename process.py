from multiprocessing import Process
import time

y='kumanxuan'

def test():
    for i in range(2):
        global y
        y+="cc1"
        print(y)
        print('--test--')
        time.sleep(1)


if __name__ == "__main__":
    for x in range(2):
        test1 = Process(target=test)
        test1.start()
    time.sleep(4)
    print("hello!!")
    print(y)



