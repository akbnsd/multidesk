import json
from socket import *
from types import SimpleNamespace
import pickle


# sock class for network interfacing 
# socket is a wrapper class around socket for quick configuration

delim = b"\n\n\n\n\n"

class sock:

    # multiple sockets to seperate data flow
    tcp, udp = socket(), socket()
    localPort = int()
    remAddr = (str, int)


    def __init__(self, port):
        self.localPort = port
        self.tcp = socket(AF_INET, SOCK_STREAM)
        self.udp = socket(AF_INET, SOCK_DGRAM )

        self.udp.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.tcp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.tcp.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
        self.udp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.udp.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)

        self.tcp.bind(('', port))
        self.udp.bind(('', port))
        self.buffer = b""

    def listen(self):
        self.tcp.listen()


    def connect(self, addr):
        self.tcp.connect(addr)
        child = sock(self.localPort)
        var = child.tcp
        child.tcp = self.tcp
        self.tcp = var
        
        return child

    
    def accept(self):
        addr = self.tcp.accept()
        sck = sock(self.localPort)
        sck.tcp = addr[0]
        sck.remAddr = addr[1]
        return sck
    
    def send(self, string: str, adr=None):
        if adr == None:
            self.tcp.send(bytes(string, 'utf-8'))
        else:
            self.udp.sendto(bytes(string, 'utf-8') , adr)


    def sendJ(self, obj, adr=None):
        if adr == None:
            self.tcp.sendall(pickle.dumps(obj) + delim)
        else:
            self.udp.sendall(pickle.dumps(obj), adr)


    def recv(self) -> str:
        return self.tcp.recv()
    
    def recvFrom(self, bufsize=1024):
        return self.udp.recvfrom(bufsize)

    def recvJ(self, bufsize=1024):
        bit = self.tcp.recv(bufsize)
        if len(self.buffer) > 1000000:
            # self.buffer = self.buffer.split(delim,1)[1]
            pass
        self.buffer += bit
        try:
            data, self.buffer = self.buffer.split(delim, 1)
            data = pickle.loads(data)
            return data

        except pickle.UnpicklingError:
            return None

    def recvJFrom(self):
        try:
            info = self.recvFrom()
            return [ pickle.loads(info[0]), info[1]]
        except:
            return [None, None]

    def __del__(self):
        self.tcp.close()
        self.udp.close()


