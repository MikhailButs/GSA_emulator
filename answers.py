# answer function in GSAemulatorclass
# выполняет действия и возвращает ответ для клиента
import datetime
import sys
import time  # задержка на калибровку


def sys_print(*data):
    sys.stdout.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {"".join(map(str, data))}')
    return 'printed'


def answer(gsa, task):
    gsa.refresh_config()
    task = task[1:-1].split(' ')
    task_txt = ' '.join(map(str, task))
    type = task[0]

    sys_print('Answering to *', task_txt, '\\n\n')

    if type == 'CONF':  # установка конфигурации времязадающей цепочки
        gsa.T = int(task[1])

    elif type == 'CAL':  # запуск калибровочных импульсов (65535 - начать непрерывные импульсы, 0 - остановить)
        if task[1] == '65535':
            sys_print('Infinite calibration started\n')
        elif task[1] == '0':
            sys_print('Infinite calibration ended\n')
        else:
            time.sleep(5)  # прибор молчит до 8 секунд
            sys_print('Calibration ended\n')
    elif type == 'GAIN':
        if task[1] == 'A':
            gsa.gainCH1 = int(task[2])
        elif task[1] == 'B':
            # sys_print('Answering to *', task_txt, '\\n\n')
            gsa.gainCH2 = int(task[2])

    gsa.refresh_config()  # сохраняемся

    # формируем ответ по протоколу
    answer_prot = gsa.prot[type]
    answer_prot = answer_prot.split(',')
    answer_gsa = ''
    for i in answer_prot:
        if gsa.conf_dict.get(i) == None:
            answer_gsa += gsa.prot[type] + ' '  # если поля нет в конфигурации, значит это "дежурный" отет (типа Ок)
        else:
            answer_gsa += gsa.conf_dict[i] + ' '  # если поле есть в конфигурации, возвращаем значение
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
# 6 T(5bit) : 3
# 7 gainCH1(8bit) : 4
# 8 gainCH2(8bit) : 5

# CML
# *ShapingAmplifierAndGSA v1, RadistASCII v0, 16.10.2021\n
# *Ok\n
# *3\n
# *Ok\n
# *Ok\n
# *Ok\n
