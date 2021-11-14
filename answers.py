# answer function
# выполняет действия и возвращает ответ для клиента
import time  # задержка на калибровку


def answer(data, gsa):
    data = data[1:-1].split(' ')
    type = data[0]

    if type == 'IDN?':  # возврат ID прибора
        print('GSA: answered ID')
        return (f'*{gsa.name} {gsa.soft_ver}, {gsa.protoc_name} {gsa.protoc_ver}, {gsa.upd_data}\n')

    elif type == 'CONF?':  # возврат конфигурации времязадающей цепчки
        print('GSA: answered config')
        return f'*{gsa.T}\n'

    elif type == 'CONF':  # установка конфигурации времязадающей цепочки
        gsa.T = int(data[1])
        gsa.refresh_config()
        print('GSA: configuration refreshed')
        return '*Ok\n'

    elif type == 'CAL':  # запуск калибровочных импульсов (65535 - начать непрерывные импульсы, 0 - остановить)
        if data[1] == '65535':
            print('GSA: infinite calibration started')
            return '*Ok\n'
        elif data[1] == '0':
            print('GSA: infinite calibration ended')
            return '*Ok\n'
        else:
            time.sleep(5)  # прибор молчит до 8 секунд
            print('GSA: calibration ended')
            return '*Ok\n'

    else:
        return 'GSA: unknown command'


if __name__ == '__main__':
    pass
