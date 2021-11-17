# main entrance point
import socket
import time

import AMP_GSA

if __name__ == '__main__':
    address = ('127.0.0.1', 10001)
    sock = socket.socket()
    sock.connect(address)

    gsa = AMP_GSA.AMP_GSA(sock)
    print('asked: NAME')
    print(gsa.get_name())
    time.sleep(5)

    print('asked: CONF?')
    print(gsa.get_conf())
    time.sleep(5)

    print('set : CONF')
    print(gsa.set_conf(9))
    time.sleep(5)

    print('set : GAIN CH1')
    print(gsa.set_gainCH1(10))
    time.sleep(5)

    print('set : GAIN CH2')
    print(gsa.set_gainCH2(11))
    time.sleep(5)

    print('make : CAL')
    print(gsa.make_call(10, 10, 10, 10))

    print('close connection')
    time.sleep(10)

    sock.close()
