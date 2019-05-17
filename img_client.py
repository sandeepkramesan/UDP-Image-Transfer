#img client

import os
import socket

ip = "172.16.104.61"
port = 5566

def imgrecv():
    filename = raw_input("enter file name : ")
    co.sendto(filename,(ip,port))
    file_ob = open(filename,"w")
    file_content,addr = co.recvfrom(40000)
    file_ob.write(file_content)
    print "file recieved successfully!!!"

co = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
imgrecv()
