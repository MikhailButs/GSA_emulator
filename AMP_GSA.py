# Класс принимает из главной программы сокет и по нему выполняет действия с усилителем
import socket


class AMP_GSA:
    def __init__(self, address):
        self.gainCH1 = None
        self.gainCH2 = None
        self.conf = None
        self.client = Client(address)

    def get_name(self):
        #self.sock.send('*IDN?\n'.encode('utf-8'))
        #return self.sock.recv(1024).decode('utf-8')[1:-1]
        return self.client.ask('IDN?')

    def get_conf(self):
        self.sock.send('*CONF?\n'.encode('utf-8'))
        return int(self.sock.recv(1024).decode('utf-8')[1:-1])

    def set_conf(self, conf):
        self.sock.send(f'*CONF {conf}\n'.encode('utf-8'))
        return self.sock.recv(1024).decode('utf-8')[1:-1]

    def set_gainCH1(self, gainCH1):
        self.sock.send(f'*GAIN A {gainCH1}\n'.encode('utf-8'))
        return self.sock.recv(1024).decode('utf-8')[1:-1]

    def set_gainCH2(self, gainCH2):
        self.sock.send(f'*GAIN B {gainCH2}\n'.encode('utf-8'))
        return self.sock.recv(1024).decode('utf-8')[1:-1]

    def make_call(self, num, amp, impulse, pause):
        self.sock.send(f'*CAL {num} {amp} {impulse} {pause}\n'.encode('utf-8'))
        return self.sock.recv(1024).decode('utf-8')[1:-1]


class Client:
    def __init__(self, address):
        self.address = address
        self.sock = socket.socket()
        self.sock.connect(address)

    def ask(self, quest):
        self.sock.send(f'*{quest}\n'.encode('utf-8'))
        return self.sock.recv(1024).decode('utf-8')[1:-1]
