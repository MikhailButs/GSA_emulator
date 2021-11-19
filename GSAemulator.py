# parameters of the GSA
import answers


# def get_config(fileobj):
#    return (fileobj.readline().split(' : ')[1][:-1])  # построчно берем конфигурации из файла

# def sys_print(*data):
#    sys.stdout.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {"".join(map(str, data))}')
#    return 'printed'


class GSAemulator:
    def __init__(self, conffilename, protofilename):
        # инициализируемся сохраненными в файле данными
        configfile = open(conffilename, 'r')
        lines = configfile.readlines()
        conf_dict = {i.split(' ')[0]: i.split(' ')[1][:-1] for i in lines}
        self.name = conf_dict.setdefault('name')
        self.soft_ver = conf_dict.setdefault('soft_ver')
        self.protoc_name = conf_dict.setdefault('protoc_name')
        self.protoc_ver = conf_dict.setdefault('protoc_ver')
        self.upd_data = conf_dict.setdefault('upd_data')
        self.T = int(conf_dict.setdefault('T(5bit)', '0'))
        self.gainCH1 = int(conf_dict.setdefault('gainCH1(8bit)', '0'))
        self.gainCH2 = int(conf_dict.setdefault('gainCH2(8bit)', '0'))
        self.conf_dict = conf_dict
        configfile.close()

        # загружаем прококол общения
        # смотрим, где команды пользователя, а где прибора
        protocfile = open(protofilename, 'r')
        head = protocfile.readline().split(' ')
        if head[0] == 'USER':
            user = 0
            amp = 1
        else:
            user = 1
            amp = 0
        lines = protocfile.readlines()
        prot_dict = {i.split(' ')[user]: i.split(' ')[amp][:-1] for i in lines}
        self.prot = prot_dict

    def refresh_config(self):  # обновляем данные в файле конфигурации по параметрам переданного элемента
        configfile = open('config', 'w')
        configfile.write(f'name {self.name}\n')
        configfile.write(f'soft_ver {self.soft_ver}\n')
        configfile.write(f'protoc_name {self.protoc_name}\n')
        configfile.write(f'protoc_ver {self.protoc_ver}\n')
        configfile.write(f'upd_data {self.upd_data}\n')
        configfile.write(f'T(5bit) {self.T}\n')
        configfile.write(f'gainCH1(8bit) {self.gainCH1}\n')
        configfile.write(f'gainCH2(8bit) {self.gainCH2}\n')
        configfile.write(f'Ok {self.conf_dict["Ok"]}\n')
        configfile.close()

    def answer(self, data):
        return answers.answer(self, data)

if __name__ == '__main__':
    gsa = GSAemulator('config', 'protocol')
    print(gsa.conf_dict)
