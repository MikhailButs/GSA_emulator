# parameters of the GSA
import datetime
import sys


# def get_config(fileobj):
#    return (fileobj.readline().split(' : ')[1][:-1])  # построчно берем конфигурации из файла

def sys_print(*data):
    sys.stdout.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {"".join(map(str, data))}')
    return 'printed'


class GSAemulator:
    def __init__(self, conffilename):  # инициализируемся сохраненными в файле данными
        configfile = open(conffilename, 'r')
        lines = configfile.readlines()
        conf_dict = {i.split(' ')[0]: i.split(' ')[1][:-1] for i in lines}
        self.name = conf_dict.setdefault('name')
        self.soft_ver = conf_dict.setdefault('soft_ver')
        self.protoc_name = conf_dict.setdefault('protoc_name')
        self.protoc_ver = conf_dict.setdefault('protoc_ver')
        self.upd_data = conf_dict.setdefault('upd_data')
        self.T = int(conf_dict.setdefault('T(5bit', '0'), 2)
        self.gainCH1 = int(conf_dict.setdefault('gainCH1(8bit)', '0'), 2)
        self.gainCH2 = int(conf_dict.setdefault('gainCH2(8bit)', '0'), 2)
        configfile.close()

    def refresh_config(self):  # обновляем данные в файле по параметрам переданного элемента
        config = open('config', 'w')
        config.write(f'name : {self.name}\n')
        config.write(f'soft_ver : {self.soft_ver}\n')
        config.write(f'protoc_name : {self.protoc_name}\n')
        config.write(f'protoc_ver : {self.protoc_ver}\n')
        config.write(f'upd_data : {self.upd_data}\n')
        config.write(f'T(5bit) : {bin(self.T)}\n')
        config.write(f'gainCH1(8bit) : {bin(self.gainCH1)}\n')
        config.write(f'gainCH2(8bit) : {bin(self.gainCH2)}\n')
        config.close()


if __name__ == '__main__':
    gsa = GSAemulator('config')
