#img server

import os
import socket


ip = "172.16.104.61"
port = 5566

def imgserve():
    filename,addr = so.recvfrom(1000)
    print "filename: ",filename
    try:
        file_ob = open(filename,"r")
        file_content = file_ob.read()
        so.sendto(file_content,addr)
        print "file sent successfully"
    except IOError:
        so.sendto("no file",addr)
        print "file do not exist!!!\n"



so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
so.bind((ip,port))
imgserve()

