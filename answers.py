# answer function
# выполняет действия и возвращает ответ для клиента
import time  # задержка на калибровку

from GSAemulator import sys_print


def answer(data, gsa):
    data = data[1:-1].split(' ')
    data_txt = ' '.join(map(str, data))
    type = data[0]

    if type == 'IDN?':  # возврат ID прибора
        sys_print('Answering to *', data_txt, '\\n\n')
        return (f'*{gsa.name} {gsa.soft_ver}, {gsa.protoc_name} {gsa.protoc_ver}, {gsa.upd_data}\n')

    elif type == 'CONF?':  # возврат конфигурации времязадающей цепчки
        sys_print('Answering to *', data_txt, '\\n\n')
        return f'*{gsa.T}\n'

    elif type == 'CONF':  # установка конфигурации времязадающей цепочки
        gsa.T = int(data[1])
        gsa.refresh_config()
        sys_print('Answering to *', data_txt, '\\n\n')
        return '*Ok\n'

    elif type == 'CAL':  # запуск калибровочных импульсов (65535 - начать непрерывные импульсы, 0 - остановить)
        if data[1] == '65535':
            sys_print('Answering to *', data_txt, '\\n : Infinite calibration started\n')
            return '*Ok\n'
        elif data[1] == '0':
            sys_print('Answering to *', data_txt, '\\n : Infinite calibration ended\n')
            return '*Ok\n'
        else:
            sys_print('Answering to *', data_txt, '\\n\n')
            time.sleep(5)  # прибор молчит до 8 секунд
            sys_print('Calibration ended\n')
            return '*Ok\n'

    else:
        sys_print('Answering to *', data_txt, '\\n\n')
        return 'ERROR unknown command'


if __name__ == '__main__':
    pass
