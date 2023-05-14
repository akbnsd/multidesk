from socket import *


# sock class for network interfacing 
# socket is a wrapper class around socket for quick configuration


class sock:

    # multiple sockets to seperate data flow
    tcp, udp = socket(), socket()
    localPort = int()
    remAddr = (str, int)


    def __init__(self, port):
        self.localPort = port
        self.tcp = socket(AF_INET, SOCK_STREAM)
        self.udp = socket(AF_INET, SOCK_DGRAM )

        self.tcp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.tcp.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
        self.udp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.udp.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)

        self.tcp.bind(('', port))
        self.udp.bind(('', port))


    def listen(self):
        self.tcp.listen()


    def connect(self, addr):
        self.raw.connect(addr)
    
    
    def accept(self) -> sock:
        addr = self.tcp.accept()
        sck = sock()
        sck.tcp = addr[0]
        sck.remAddr = addr[1]
        sck.port = self.port
        return sck


    def send(self, string : str) :
        self.tcp.send(string)
    
    
    def send(self, string: str, adr):
        self.udp.sendto(bytes(string, 'utf-8') , adr)


    def recv(self) -> str:
        return self.tcp.recv()
    
    def recvFrom(self):
        bytearray(100)
        return self.udp.recvfrom()


    def __del__(self):
        self.tcp.close()
        self.udp.close()


