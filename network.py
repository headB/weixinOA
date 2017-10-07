from  socket import *

myFirstSocket = socket(AF_INET,SOCK_DGRAM)

#myFirstSocket.sendto("1:12525:kumanxuan:kumanxuan:32:my name is kumanxuan",("127.0.0.1",2425))
#修正，直接发送字符串的话，需要在前面加一个B。
myFirstSocket.sendto(b"1:12525:kumanxuan:kumanxuan:32:my name is kumanxuan",('127.0.0.1',2425))

