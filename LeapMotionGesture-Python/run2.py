###  AUTHOR:IVO STINGHEN ( gamefico@gmail.com)
### Read model from disk and run a RealTime Communication with unity
import Orange
import numpy as np
import pandas as pd
import time,os
import socket
import pickle

host, port = "127.0.0.1", 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

############# LOAD MODEL  ##############
model = pickle.load(open('model.pkcls', 'rb'))
#classifier = pickle.load(open('save.pkcls', 'rb'))
print("model loaded!")
#########################################################

try:

    sock.connect((host, port))
    print("socket connected!")
    while (1):

        #recebe input
        inputReceived = sock.recv(1024).decode("utf-8")
        line = inputReceived
        line = line.rstrip('\n')
        mylist = [float(x) for x in line.split(',')]
        print(mylist)
        result = model(mylist)
        r2 = [model.domain.class_var.str_val(i) for i in result]  # convert to value names (strings)
        r = r2[0]
        print(r)
        sock.sendall(r.encode("utf-8"))
        # print(result)
        time.sleep(.02)


finally:
    sock.close()
