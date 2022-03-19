import socket
import sys
import time

# -*- coding: utf-8 -*-

address = (sys.argv[1], int(sys.argv[2]))
var = int(sys.argv[3])
totalUseTime=0.0
while var > 0:
  startTime=time.time()
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(address)
  s.send('a'.encode())
  data = s.recv(512)
  endTime=time.time()
  useTime=(endTime-startTime)*1000
  var-=1
  totalUseTime+=useTime
avgUseTime=totalUseTime/int(sys.argv[3])/2
print ("Average rtt:",avgUseTime,"ms")
s.close()
