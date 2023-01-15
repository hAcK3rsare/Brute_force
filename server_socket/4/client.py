try:
    from socket import *
    s=socket(AF_INET,SOCK_STREAM)
    host="192.168.0.180"
    port=5000
    s.connect((host,port))
    while True:
        s.send(input('phillip : ').encode('utf-8'))
        y=s.recv(2048)
        print('patrick : ',y.decode('utf-8'))
    s.close()
    
except error as e:
    print(e)
except KeyboardInterrupt:
    print('chat has finished')