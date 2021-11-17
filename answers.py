# answer function
# выполняет действия и возвращает ответ для клиента
import time  # задержка на калибровку

from GSAemulator import sys_print


def answer(task, gsa):
    task = task[1:-1].split(' ')
    task_txt = ' '.join(map(str, task))
    type = task[0]

    if type == 'IDN?':  # возврат ID прибора
        sys_print('Answering to *', task_txt, '\\n\n')
        return (f'*{gsa.name} {gsa.soft_ver}, {gsa.protoc_name} {gsa.protoc_ver}, {gsa.upd_data}\n')

    elif type == 'CONF?':  # возврат конфигурации времязадающей цепчки
        sys_print('Answering to *', task_txt, '\\n\n')
        return f'*{gsa.T}\n'

    elif type == 'CONF':  # установка конфигурации времязадающей цепочки
        gsa.T = int(task[1])
        gsa.refresh_config()
        sys_print('Answering to *', task_txt, '\\n\n')
        return '*Ok\n'

    elif type == 'CAL':  # запуск калибровочных импульсов (65535 - начать непрерывные импульсы, 0 - остановить)
        if task[1] == '65535':
            sys_print('Answering to *', task_txt, '\\n : Infinite calibration started\n')
            return '*Ok\n'
        elif task[1] == '0':
            sys_print('Answering to *', task_txt, '\\n : Infinite calibration ended\n')
            return '*Ok\n'
        else:
            sys_print('Answering to *', task_txt, '\\n\n')
            time.sleep(5)  # прибор молчит до 8 секунд
            sys_print('Calibration ended\n')
            return '*Ok\n'
    elif type == 'GAIN':
        if task[1] == 'A':
            sys_print('Answering to *', task_txt, '\\n\n')
            gsa.gainCH1 = int(task[2])
            gsa.refresh_config()
            return '*Ok\n'
        elif task[1] == 'B':
            sys_print('Answering to *', task_txt, '\\n\n')
            gsa.gainCH2 = int(task[2])
            gsa.refresh_config()
            return '*Ok\n'
        else:
            return '*ERROR Unknown channel\n'

    else:
        sys_print('Answering to *', task_txt, '\\n\n')
        return '*ERROR unknown command\n'


if __name__ == '__main__':
    import GSAemulator

    gsa = GSAemulator.GSAemulator()
    print(answer(('*IDN?\n'), gsa))
    print(answer(('*CONF 3\n'), gsa))
    print(answer(('*CONF?\n'), gsa))
    print(answer(('*GAIN A 4\n'), gsa))
    print(answer(('*GAIN B 5\n'), gsa))
    print(answer(('*CAL 10 10 10 10\n'), gsa))

# config
# 6 T(5bit) : 0b11
# 7 gainCH1(8bit) : 0b100
# 8 gainCH2(8bit) : 0b101

# CML
# *ShapingAmplifierAndGSA v1, RadistASCII v0, 16.10.2021\n
# *Ok\n
# *3\n
# *Ok\n
# *Ok\n
# *Ok\n
