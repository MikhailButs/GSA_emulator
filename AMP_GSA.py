class AMP_GSA:
    def __init__(self, sock):
        self.gainCH1 = None
        self.gainCH2 = None
        self.conf = None
        self.sock = sock

    def get_name(self):
        self.sock.send('*IDN?\n'.encode('utf-8'))
        return self.sock.recv(1024).decode('utf-8')[1:-1]

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
