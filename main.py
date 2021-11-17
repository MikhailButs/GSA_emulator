# main entrance point
# Тест команд класса AMP_GSA
import socket
import time

import AMP_GSA

if __name__ == '__main__':
    print('Test of AMP_GSA starts')
    address = ('127.0.0.1', 10001)
    sock = socket.socket()
    sock.connect(address)
    print(f'Connected with {address}\n')

    gsa = AMP_GSA.AMP_GSA(sock)
    print('asked: NAME')
    print('Answered ', gsa.get_name(), '\n')
    time.sleep(5)

    print('asked: CONF?')
    print('Answered ', gsa.get_conf(), '\n')
    time.sleep(5)

    print('set : CONF')
    print('Set ', gsa.set_conf(9), '\n')
    time.sleep(5)

    print('set : GAIN CH1')
    print('Set ', gsa.set_gainCH1(10), '\n')
    time.sleep(5)

    print('set : GAIN CH2')
    print('Set ', gsa.set_gainCH2(11), '\n')
    time.sleep(5)

    print('make : CAL')
    print('made ', gsa.make_call(10, 10, 10, 10), '\n')

    print('close connection')
    time.sleep(10)

    sock.close()
