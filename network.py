from  socket import *

myFirstSocket = socket(AF_INET,SOCK_DGRAM)

#myFirstSocket.sendto("1:12525:kumanxuan:kumanxuan:32:my name is kumanxuan",("127.0.0.1",2425))
#修正，直接发送字符串的话，需要在前面加一个B。
##今天看了数据结构和算法。这两个在所有程序里面都很重要。
##举例，平时在php里面变成，其实就是数据结构（数组）和算法（里面的流程）。
myFirstSocket.sendto(b"1:12525:kumanxuan:kumanxuan:32:my name is kumanxuan",('127.0.0.1',2425))

