# Класс принимает из главной программы сокет и по нему выполняет действия с усилителем
import socket


class AMP_GSA:
    def __init__(self, address):
        self.gainCH1 = None
        self.gainCH2 = None
        self.conf = None
        self.client = Client(address)

    def get_name(self):
        return self.client.ask('IDN?')

    def get_conf(self):
        return self.client.ask('CONF?')

    def set_conf(self, conf):
        return self.client.ask(f'CONF {conf}')

    def set_gainCH1(self, gainCH1):
        return self.client.ask(f'GAIN A {gainCH1}')

    def set_gainCH2(self, gainCH2):
        return self.client.ask(f'GAIN B {gainCH2}')

    def make_call(self, num, amp, impulse, pause):
        return self.client.ask(f'CAL {num} {amp} {impulse} {pause}')


class Client:
    def __init__(self, address):
        self.address = address
        self.sock = socket.socket()
        self.sock.connect(address)

    def ask(self, quest):
        self.sock.send(f'*{quest}\n'.encode('utf-8'))
        return self.sock.recv(1024).decode('utf-8')[1:-1]

    def __del__(self):
        self.sock.close()
