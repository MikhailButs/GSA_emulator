from socket import socket,AF_INET, SOCK_STREAM
from threading import Thread
import sys

class server:
    def __init__(self, host='localhost', port=10001, timeout=1):
        self.state = 'init'
        self.addr = (host, port)
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind(self.addr)
        self.sock.listen(1)
        self.sock.settimeout(1)

        self.state = 'idle'

        self.rearm_auto = False
        self.listener = None
        self.rearmer = Thread(target=self.rearm, daemon=True)
        self.rearmer.start()


        self.client_sock = None
        self.client_addr = None
        self.client_timeout = timeout

        self.data = None

        # Callbacks
        self.on_connection = None
        self.on_connection_lost = None
        self.on_new_data = None
        self.on_timeout = None

    def __del__(self):
        print('deleting')
        self.close()

    def close(self):
        if self.state == 'closed':
            return
        if self.state == 'connected':
            self.client_sock.send(b'')

        self.state = 'closing'

        if self.listener:
            while self.listener.is_alive():
                pass
            self.listener = None

        self.rearm_auto = False
        if self.rearmer:
            while self.rearmer.is_alive():
                pass
            self.rearmer = None

        self.data = None
        self.on_connection = None
        self.on_connection_lost = None
        self.on_new_data = None

        if self.client_sock:
            self.client_sock.close()
            self.client_sock = None
            self.client_addr = None

        if self.sock:
            self.sock.close()
            self.sock = None

        self.state = 'closed'

    def rearm(self):
        while self.state != 'closing':
            if self.rearm_auto and self.state == 'idle':
                self.listen()

    def listen(self):
        if self.state == 'idle':
            self.state = 'listening'
            self.listener = Thread(target=self.accept, daemon=True)
            self.listener.start()

    def accept(self):
        while self.state == 'listening':
            try:
                self.client_sock, self.client_addr = self.sock.accept()
            except:
                pass
            else:
                self.client_sock.settimeout(self.client_timeout)
                self.reply()

    def reply(self):
        self.state = 'connected'
        if self.on_connection:
            self.on_connection(self)

        while self.state == 'connected':
            try:
                self.data = self.client_sock.recv(1024)
                if len(self.data) == 0:
                    if self.on_connection_lost:
                        self.on_connection_lost(self)
                    self.client_sock = None
                    self.client_addr = None
                    self.data = None
                    self.state = 'idle'
                    self. listener = None

                elif self.on_new_data:
                    self.on_new_data(self)
            except OSError as msg:
                if self.on_timeout:
                    self.on_timeout(self, msg)


def connected(obj):
    sys.stdout.write('\nconnected\n')
    sys.stdout.write('>')
    sys.stdout.flush()

def lost(obj):
    sys.stdout.write('lost\n')
    sys.stdout.write('>')
    sys.stdout.flush()

def newdata(obj):
    sys.stdout.write(obj.data.decode())
    sys.stdout.write('>')
    sys.stdout.flush()

def ontimeout(obj, msg):
    pass
    # sys.stdout.write(format(msg)+'\n')
    # sys.stdout.write('>')
    # sys.stdout.flush()


class Cli:
    def __init__(self):
        self.commands = ['',]

    def prompt(self, ps1='srv>'):
        sys.stdout.write(ps1)
        sys.stdout.flush()
        cmd = sys.stdin.readline()
        if len(cmd)>1:
            self.commands.append(cmd)


if __name__ == "__main__":

    host = 'localhost'
    port = 10001
    timeout = 1

    if len(sys.argv)>1:
        host = sys.argv[1]

    if len(sys.argv)>2:
        port = sys.argv[2]

    if len(sys.argv)>2:
        timeout = sys.argv[3]
    srv = server(host=host, port=port, timeout=1)

    srv.on_connection = connected
    srv.on_connection_lost = lost
    srv.on_new_data = newdata
    srv.on_timeout = ontimeout

    srv.rearm_auto = True
    addr = srv.sock.getsockname()
    sys.stdout.write('Srv at '+addr[0]+':'+format(addr[1])+' started\n')

    stdin_fileno = sys.stdin

    # Keeps reading from stdin and quits only if the word 'exit' is there
    # This loop, by default does not terminate, since stdin is open
    sys.stdout.write('>')
    sys.stdout.flush()
    for line in stdin_fileno:
        # Remove trailing newline characters using strip()
        if 'exit' == line.strip():
            print('Found exit. Terminating the program')
            exit(0)
        else:
            sys.stdout.write('>')
            sys.stdout.flush()

    # cli = Cli()
    # while cli.commands[-1][:-1].lower() != 'exit':
    #     cli.prompt()