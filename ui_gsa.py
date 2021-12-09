import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import ui_design  # Это наш конвертированный файл дизайна
import AMP_GSA
import datetime


class ExampleApp(QtWidgets.QMainWindow, ui_design.Ui_win):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        # блок "usb-eternet"
        self.amp = AMP_GSA.AMP_GSA()
        self.ether_client = None
        self.ether_con_btn.clicked.connect(self.ether_con)
        self.get_name_btn_ether.clicked.connect(self.make_get_name)

        # блок "постоянная времени"
        self.time_const_slider.valueChanged.connect(self.set_time_const_spin_box)
        self.time_const_spin_box.valueChanged.connect(self.set_time_const_slider)
        self.setconf_btn.clicked.connect(self.set_conf)
        self.time_const_spin_box.setValue(float(self.amp.conf))
        self.getconf_btn.clicked.connect(self.get_conf)

        # блок "коэффициент усиления"
        self.setgain_slider.valueChanged.connect(self.set_setgain_spin)
        self.setgain_spin.valueChanged.connect(self.set_setgain_slider)
        self.setgain_slider_2.valueChanged.connect(self.set_setgain_spin_2)
        self.setgain_spin_2.valueChanged.connect(self.set_setgain_slider_2)
        self.setgain_btn.clicked.connect(self.set_gain_A)
        self.setgain_btn_2.clicked.connect(self.set_gain_B)
        self.setgain_spin.setValue(float(self.amp.gainCH1))
        self.setgain_spin_2.setValue(float(self.amp.gainCH2))

        # блок "калибровка (гса)"
        self.set_num_pulses_slider.valueChanged.connect(self.set_set_num_pulses_spin)
        self.set_num_pulses_spin.valueChanged.connect(self.set_set_num_pulses_slider)
        self.set_amp_pulses_slider.valueChanged.connect(self.set_set_amp_pulses_spin)
        self.set_amp_pulses_spin.valueChanged.connect(self.set_set_amp_pulses_slider)
        self.set_time_pulse_slider.valueChanged.connect(self.set_set_time_pulse_spin)
        self.set_time_pulse_spin.valueChanged.connect(self.set_set_time_pulse_slider)
        self.set_pause_slider.valueChanged.connect(self.set_set_pause_spin)
        self.set_pause_spin.valueChanged.connect(self.set_set_pause_slider)
        self.start_call.clicked.connect(self.make_start_call)
        self.set_num_pulses_spin.setValue(float(self.amp.num_pulses))
        self.set_amp_pulses_spin.setValue(float(self.amp.amp_pulses))
        self.set_time_pulse_spin.setValue(float(self.amp.width_pulses))
        self.set_pause_spin.setValue(float(self.amp.width_pause))

    # блок "usb-eterne"
    def ether_con(self):
        if len(self.ip_field.text()) & len(self.port_field.text()) != 0:
            try:
                self.ether_client = AMP_GSA.Client((str(self.ip_field.text()), int(self.port_field.text())))
                self.cml_box.append(time_print(f'CONNECTED TO ({self.ip_field.text()}, {self.port_field.text()})'))
            except ConnectionRefusedError:
                self.ether_client = None
                self.cml_box.append(time_print(f'CAN\'T CONNECT TO ({self.ip_field.text()}, {self.port_field.text()})'))


    def make_get_name(self):
        if self.ether_client is not None:
            self.cml_box.append(time_print(f'ASKED {self.amp.get_name()}'))
            name = self.ether_client.ask(self.amp.get_name())
            self.amp.name = name[1:-1]
            self.amp.refresh_conf()
            self.cml_box.append(time_print(f'RECEIVED {name}'))

    # блок "постоянная времени"
    def set_time_const_spin_box(self):
        self.time_const_spin_box.setValue(self.time_const_slider.value())
        self.amp.conf = str(int(self.time_const_slider.value()))
        self.amp.refresh_conf()

    def set_time_const_slider(self):
        self.time_const_slider.setValue(self.time_const_spin_box.value())
        self.amp.conf = str(int(self.time_const_spin_box.value()))
        self.amp.refresh_conf()

    def set_conf(self):
        if self.ether_client is not None:
            self.cml_box.append(time_print(f'ASKED {self.amp.set_conf(self.amp.conf)}'))
            self.cml_box.append(time_print(f'RECEIVED {self.ether_client.ask(self.amp.set_conf(self.amp.conf))}'))

    def get_conf(self):
        if self.ether_client is not None:
            self.cml_box.append(time_print(f'ASKED {self.amp.get_conf()}'))
            conf = self.ether_client.ask(self.amp.get_conf())
            self.amp.conf = conf[1:-1]
            self.amp.refresh_conf()
            self.time_const_spin_box.setValue(float(self.amp.conf))
            self.cml_box.append(time_print(f'RECEIVED {conf}'))

    # блок "коэффициент усиления"
    def set_setgain_slider(self):
        self.setgain_slider.setValue(self.setgain_spin.value())
        self.amp.gainCH1 = str(int(self.setgain_spin.value()))
        self.amp.refresh_conf()

    def set_setgain_spin(self):
        self.setgain_spin.setValue(self.setgain_slider.value())
        self.amp.gainCH1 = str(int(self.setgain_spin.value()))
        self.amp.refresh_conf()

    def set_setgain_slider_2(self):
        self.setgain_slider_2.setValue(self.setgain_spin_2.value())
        self.amp.gainCH2 = str(int(self.setgain_spin_2.value()))
        self.amp.refresh_conf()

    def set_setgain_spin_2(self):
        self.setgain_spin_2.setValue(self.setgain_slider_2.value())
        self.amp.gainCH2 = str(int(self.setgain_spin_2.value()))
        self.amp.refresh_conf()

    def set_gain_A(self):
        if self.ether_client is not None:
            self.cml_box.append(time_print(f'ASKED {self.amp.set_gainCH1(self.amp.gainCH1)}'))
            self.cml_box.append(time_print(f'RECEIVED {self.ether_client.ask(self.amp.set_gainCH1(self.amp.gainCH1))}'))

    def set_gain_B(self):
        if self.ether_client is not None:
            self.cml_box.append(time_print(f'ASKED {self.amp.set_gainCH2(self.amp.gainCH2)}'))
            self.cml_box.append(time_print(f'RECEIVED {self.ether_client.ask(self.amp.set_gainCH2(self.amp.gainCH2))}'))

    # блок "калибровка (гса)"
    def set_set_num_pulses_spin(self):
        self.set_num_pulses_spin.setValue(self.set_num_pulses_slider.value())
        self.amp.num_pulses = str(int(self.set_num_pulses_spin.value()))
        self.amp.refresh_conf()

    def set_set_num_pulses_slider(self):
        self.set_num_pulses_slider.setValue(self.set_num_pulses_spin.value())
        self.amp.num_pulses = str(int(self.set_num_pulses_spin.value()))
        self.amp.refresh_conf()

    def set_set_amp_pulses_spin(self):
        self.set_amp_pulses_spin.setValue(self.set_amp_pulses_slider.value())
        self.amp.amp_pulses = str(int(self.set_amp_pulses_spin.value()))
        self.amp.refresh_conf()

    def set_set_amp_pulses_slider(self):
        self.set_amp_pulses_slider.setValue(self.set_amp_pulses_spin.value())
        self.amp.amp_pulses = str(int(self.set_amp_pulses_spin.value()))
        self.amp.refresh_conf()

    def set_set_time_pulse_spin(self):
        self.set_time_pulse_spin.setValue(self.set_time_pulse_slider.value())
        self.amp.width_pulses = str(int(self.set_time_pulse_spin.value()))
        self.amp.refresh_conf()

    def set_set_time_pulse_slider(self):
        self.set_time_pulse_slider.setValue(self.set_time_pulse_spin.value())
        self.amp.width_pulses = str(int(self.set_time_pulse_spin.value()))
        self.amp.refresh_conf()

    def set_set_pause_spin(self):
        self.set_pause_spin.setValue(self.set_pause_slider.value())
        self.amp.width_pause = str(int(self.set_pause_spin.value()))
        self.amp.refresh_conf()

    def set_set_pause_slider(self):
        self.set_pause_slider.setValue(self.set_pause_spin.value())
        self.amp.width_pause = str(int(self.set_pause_spin.value()))
        self.amp.refresh_conf()

    def make_start_call(self):
        if self.ether_client is not None:
            a, b, c, d = self.amp.num_pulses, self.amp.amp_pulses, self.amp.width_pulses, self.amp.width_pause
            self.cml_box.append(time_print(f'ASKED {self.amp.make_call(a, b, c, d)}'))
            self.cml_box.append(time_print(f'RECEIVED {self.ether_client.ask(self.amp.make_call(a, b, c, d))}'))


def time_print(data):
    data = data.replace('\n', '\\n')
    return f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {data}'


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем

    main()  # то запускаем функцию main()
