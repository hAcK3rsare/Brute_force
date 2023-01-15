from socket import *

try:
    s= socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    
    host="192.168.0.180"
    port=5000
    
    s.bind((host,port))
    s.listen(5)
    c,addr = s.accept()
    
    while True:
        x=c.recv(2048)
        print("him : ",x.decode('utf-8'))
        c.send(input('you :').encode('utf-8'))
    while True:
        s.send(input('patrick : ').encode('utf-8'))
        x=c.recv(2049)
        print('bob : ',y.decode('utf-8'))
    s.close()

except error as e:
    print(e)
except KeyboardInterrupt:
    print('chat has finished')
    