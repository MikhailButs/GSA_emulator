# answer function in GSAemulatorclass
# выполняет действия и возвращает ответ для клиента
import datetime
import sys
import time  # задержка на калибровку


def sys_print(*data):
    sys.stdout.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {"".join(map(str, data))}')
    return 'printed'


def answer(gsa, task):
    task = task[1:-1].split(' ')
    task_txt = ' '.join(map(str, task))
    type = task[0]

    sys_print('Answering to *', task_txt, '\\n\n')

    # if type == 'IDN?':  # возврат ID прибора
    # sys_print('Answering to *', task_txt, '\\n\n')
    # return (f'*{gsa.name} {gsa.soft_ver}, {gsa.protoc_name} {gsa.protoc_ver}, {gsa.upd_data}\n')

    # elif type == 'CONF?':  # возврат конфигурации времязадающей цепчки
    # sys_print('Answering to *', task_txt, '\\n\n')
    # answer = gsa.prot[type]
    # return f'*{gsa.conf_dict[answer]}\n'

    if type == 'CONF':  # установка конфигурации времязадающей цепочки
        gsa.T = int(task[1])
        gsa.refresh_config()
        # sys_print('Answering to *', task_txt, '\\n\n')
        # return '*Ok\n'

    elif type == 'CAL':  # запуск калибровочных импульсов (65535 - начать непрерывные импульсы, 0 - остановить)
        if task[1] == '65535':
            sys_print('Infinite calibration started\n')
            # return '*Ok\n'
        elif task[1] == '0':
            sys_print('Infinite calibration ended\n')
            # return '*Ok\n'
        else:
            # sys_print('Answering to *', task_txt, '\\n\n')
            time.sleep(5)  # прибор молчит до 8 секунд
            sys_print('Calibration ended\n')
            # return '*Ok\n'
    elif type == 'GAIN':
        if task[1] == 'A':
            # sys_print('Answering to *', task_txt, '\\n\n')
            gsa.gainCH1 = int(task[2])
            gsa.refresh_config()
            # return '*Ok\n'
        elif task[1] == 'B':
            # sys_print('Answering to *', task_txt, '\\n\n')
            gsa.gainCH2 = int(task[2])
            gsa.refresh_config()
            # return '*Ok\n'
        # else:
        # return '*ERROR Unknown channel\n'

    # else:
    # sys_print('Answering to *', task_txt, '\\n\n')
    #    return '*ERROR unknown command\n'

    # формируем отвер по протоколу
    answer_prot = gsa.prot[type]
    answer_prot = answer_prot.split(',')
    answer_gsa = ''
    for i in answer_prot:
        answer_gsa += gsa.conf_dict[i] + ' '
    answer_gsa = answer_gsa[:-1]
    return f'*{answer_gsa}\n'

if __name__ == '__main__':
    import GSAemulator

    gsa = GSAemulator.GSAemulator('config', 'protocol')
    # print(gsa.answer(gsa, ('*IDN?\n')))
    # print(answer(('*CONF 3\n'), gsa))
    # print(answer(('*CONF?\n'), gsa))
    # print(answer(('*GAIN A 4\n'), gsa))
    # print(answer(('*GAIN B 5\n'), gsa))
    #print(answer(('*CAL 10 10 10 10\n'), gsa))

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
