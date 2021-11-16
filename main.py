# main entrance point
import socket

import GSAemulator
import answers
from GSAemulator import sys_print

if __name__ == '__main__':
    serv_addr = ('127.0.0.1', 10001)  # адрес входа

    gsa = GSAemulator.GSAemulator()

    sock = socket.socket()
    sock.bind(serv_addr)
    sock.listen(1)
    sys_print(f'AMP+GSA starts on {serv_addr}\n')

    while True:  # прием запросов к серверу
        connection, client_address = sock.accept()
        try:
            sys_print('Connected with ', client_address, '\n')
            while True:  # работа с принятным клиентом
                data = connection.recv(32).decode('utf-8')  # прием до 32 бит
                sys_print('\n')
                sys_print('Received ', data.replace("\n", "\\n"), '\n')
                if data:
                    # print('Answering\n')
                    answer = answers.answer(data, gsa)  # выполнение запроса
                    connection.send(answer.encode('utf-8'))  # отправка ответа
                    sys_print('Answered ', answer.replace('\n', '\\n'), '\n')
                else:
                    sys_print('No data from:', client_address, '\n')
                    break  # прекращаем общение с клиентом, если он отключился

        finally:
            sys_print(f'Close connection with {client_address}\n')
            connection.close()  # всегда закрываем соединение (и при явной ошибке, и при break - отключении клиента)
