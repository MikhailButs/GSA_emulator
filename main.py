# main entrance point
import socket

import GSAemulator
import answers

if __name__ == '__main__':
    serv_addr = ('127.0.0.1', 12345)  # адрес входа

    gsa = GSAemulator.GSAemulator()

    sock = socket.socket()
    sock.bind(serv_addr)
    sock.listen(1)
    print('GSA starts')

    while True:  # прием запросов к серверу
        connection, client_address = sock.accept()
        try:
            print('Connected with:', client_address)
            while True:  # работа с принятным клиентом
                data = connection.recv(32).decode('utf-8')  # прием до 32 бит
                print(f'Received: {data}')
                if data:
                    print('Wait...')
                    answer = answers.answer(data, gsa)  # выполнение запроса
                    connection.send(answer.encode('utf-8'))  # отправка ответа
                    print('Answer: ', answer)
                else:
                    print('No data from:', client_address)
                    break  # прекращаем общение с клиентом, если он отключился

        finally:
            connection.close()  # всегда закрываем соединение (и при явной ошибке, и при break - отключении клиента)
