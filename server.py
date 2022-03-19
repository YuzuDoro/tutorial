import socket
import sys
import time
# -*- coding: utf-8 -*-
ISOTIMEFORMAT='%Y-%m-%d %X'
address = ('0.0.0.0', int(sys.argv[1]))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)
var = 1
while var == 1 :
  ss, addr = s.accept()
  ss.send('a'.encode())
  ra = ss.recv(512)
ss.close()
s.close()

