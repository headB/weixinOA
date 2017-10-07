from  socket import *

myFirstSocket = socket(AF_INET,SOCK_DGRAM)

myFirstSocket.sendto("",('127.0.0.1:2425',2425))

