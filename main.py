# main entrance point
import socket

import AMP_GSA

if __name__ == '__main__':
    address = ('127.0.0.1', 10001)
    sock = socket.socket()
    sock.connect(address)

    gsa = AMP_GSA.AMP_GSA()
