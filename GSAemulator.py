# parameters of the GSA
import datetime
import sys


def get_config(fileobj):
    return (fileobj.readline().split(' : ')[1][:-1])  # построчно берем конфигурации из файла


def sys_print(*data):
    sys.stdout.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {"".join(map(str, data))}')
    return 'printed'


class GSAemulator:
    def __init__(self):  # инициализируемся сохраненными в файле данными
        config = open('config', 'r')
        self.name = get_config(config)
        self.soft_ver = get_config(config)
        self.protoc_name = get_config(config)
        self.protoc_ver = get_config(config)
        self.upd_data = get_config(config)
        self.T = int(get_config(config), 2)
        self.gain = int(get_config(config), 2)
        config.close()

    def refresh_config(self):  # обновляем данные в файле по параметрам переданного элемента
        config = open('config', 'w')
        config.write(f'1 name : {self.name}\n')
        config.write(f'2 soft_ver : {self.soft_ver}\n')
        config.write(f'3 protoc_name : {self.protoc_name}\n')
        config.write(f'4 protoc_ver : {self.protoc_ver}\n')
        config.write(f'5 upd_data : {self.upd_data}\n')
        config.write(f'6 T(5bit) : {bin(self.T)}\n')
        config.write(f'7 gain(8bit) : {bin(self.gain)}\n')
        config.close()
