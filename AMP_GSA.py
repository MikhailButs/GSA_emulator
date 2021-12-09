# Класс принимает из главной программы сокет и по нему выполняет действия с усилителем
import socket


class AMP_GSA:
    def __init__(self, conffilename='conf'):
        configfile = open(conffilename, 'r')
        lines = configfile.readlines()
        conf_dict = {i[:i.index(' ')]: i[i.index(' ') + 1:-1] for i in lines}
        self.gainCH1 = conf_dict.setdefault('gainCH1(8bit)', '0')
        self.gainCH2 = conf_dict.setdefault('gainCH2(8bit)', '0')
        self.conf = conf_dict.setdefault('T(5bit)', '0')
        self.num_pulses = conf_dict.setdefault('num_pulses(16bit)', '0')
        self.amp_pulses = conf_dict.setdefault('amp_pulses(16bit)', '0')
        self.width_pulses = conf_dict.setdefault('width_pulses(8bit)', '0')
        self.width_pause = conf_dict.setdefault('width_pause(8bit)', '0')
        self.name = conf_dict.setdefault('name', 'name')

    def get_name(self):
        return '*IDN?\n'

    def get_conf(self):
        return '*CONF?\n'

    def set_conf(self, conf):
        return f'*CONF {conf}\n'

    def set_gainCH1(self, gainCH1):
        return f'*GAIN A {gainCH1}\n'

    def set_gainCH2(self, gainCH2):
        return f'*GAIN B {gainCH2}\n'

    def make_call(self, num, amp, impulse, pause):
        return f'*CAL {num} {amp} {impulse} {pause}\n'

    def refresh_conf(self, conffilename='conf'):
        conffilename = open(conffilename, 'w')
        conffilename.write(f'name {self.name}\n')
        conffilename.write(f'T(5bit) {self.conf}\n')
        conffilename.write(f'gainCH1(8bit) {self.gainCH1}\n')
        conffilename.write(f'gainCH2(8bit) {self.gainCH2}\n')
        conffilename.write(f'num_pulses(16bit) {self.num_pulses}\n')
        conffilename.write(f'amp_pulses(16bit) {self.amp_pulses}\n')
        conffilename.write(f'width_pulses(8bit) {self.width_pulses}\n')
        conffilename.write(f'width_pause(8bit) {self.width_pause}\n')
        conffilename.close()


class Client:
    def __init__(self, address=('127.0.0.1', 10001)):
        self.address = address
        self.sock = socket.socket()
        self.sock.connect(address)

    def ask(self, quest):
        self.sock.send(f'{quest}'.encode('utf-8'))
        return self.sock.recv(1024).decode('utf-8')

    def __del__(self):
        self.sock.close()


if __name__ == '__main__':
    client = Client()

'''' 
    def sys_print(*data):
    sys.stdout.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {"".join(map(str, data))}')
    return 'printed'
'''
