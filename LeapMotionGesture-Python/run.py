###  AUTHOR:IVO STINGHEN ( gamefico@gmail.com)
### Read model from disk and run a RealTime Communication with unity
import time
import socket
import pickle
import sklearn
from sklearn import tree
import time,os
if __name__== "__main__":

    host, port = "localhost", 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ############# LOAD MODEL  ##############
    classifier = pickle.load(open('model.sav', 'rb'))
    print("model loaded!")
    #########################################################

    try:
        sock.connect((host, port))
        print("sock connected!")
        while (1):
            inputReceived = sock.recv(1024).decode("utf-8")
            line = inputReceived
            line = line.rstrip('\n')
            mylist = [float(x) for x in line.split(',')]
            print(mylist)
            result = classifier.predict([mylist])
            result = result[0]
            sock.sendall(result.encode("utf-8"))
            time.sleep(.02)


    finally:
        sock.close()