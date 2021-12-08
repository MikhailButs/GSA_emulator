import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import ui_design  # Это наш конвертированный файл дизайна
import AMP_GSA

class ExampleApp(QtWidgets.QMainWindow, ui_design.Ui_win):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        # блок "usb-eternet"
        self.amp = None
        self.ether_con_btn.clicked.connect(self.ether_con)

        # блок "постоянная времени"
        self.time_const_slider.valueChanged.connect(self.set_time_const_spin_box)
        self.time_const_spin_box.valueChanged.connect(self.set_time_const_slider)
        self.setconf_btn.clicked.connect(self.set_conf)

        # блок "коэффициент усиления"
        self.setgain_slider.valueChanged.connect(self.set_setgain_spin)
        self.setgain_spin.valueChanged.connect(self.set_setgain_slider)
        self.setgain_slider_2.valueChanged.connect(self.set_setgain_spin_2)
        self.setgain_spin_2.valueChanged.connect(self.set_setgain_slider_2)
        self.setgain_btn.clicked.connect(self.set_gain_A)
        self.setgain_btn_2.clicked.connect(self.set_gain_B)

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

        # блок "eternet"
        self.get_name_btn_ether.clicked.connect(self.make_get_name)

    # блок "usb-eterne"
    def ether_con(self):
        if len(self.ip_field.text()) & len(self.port_field.text()) != 0:
            self.cml_box.append('CONNECTION')
            self.amp = AMP_GSA.AMP_GSA((str(self.ip_field.text()), int(self.port_field.text())))


    # блок "постоянная времени"
    def set_time_const_spin_box(self):
        self.time_const_spin_box.setValue(self.time_const_slider.value())

    def set_time_const_slider(self):
        self.time_const_slider.setValue(self.time_const_spin_box.value())

    def set_conf(self):
        self.cml_box.append('CONF')

    # блок "коэффициент усиления"
    def set_setgain_slider(self):
        self.setgain_slider.setValue(self.setgain_spin.value())

    def set_setgain_spin(self):
        self.setgain_spin.setValue(self.setgain_slider.value())

    def set_setgain_slider_2(self):
        self.setgain_slider_2.setValue(self.setgain_spin_2.value())

    def set_setgain_spin_2(self):
        self.setgain_spin_2.setValue(self.setgain_slider_2.value())

    def set_gain_A(self):
        self.cml_box.append('GAIN A')

    def set_gain_B(self):
        self.cml_box.append('GAIN B')

    # блок "калибровка (гса)"
    def set_set_num_pulses_spin(self):
        self.set_num_pulses_spin.setValue(self.set_num_pulses_slider.value())

    def set_set_num_pulses_slider(self):
        self.set_num_pulses_slider.setValue(self.set_num_pulses_spin.value())

    def set_set_amp_pulses_spin(self):
        self.set_amp_pulses_spin.setValue(self.set_amp_pulses_slider.value())

    def set_set_amp_pulses_slider(self):
        self.set_amp_pulses_slider.setValue(self.set_amp_pulses_spin.value())

    def set_set_time_pulse_spin(self):
        self.set_time_pulse_spin.setValue(self.set_time_pulse_slider.value())

    def set_set_time_pulse_slider(self):
        self.set_time_pulse_slider.setValue(self.set_time_pulse_spin.value())

    def set_set_pause_spin(self):
        self.set_pause_spin.setValue(self.set_pause_slider.value())

    def set_set_pause_slider(self):
        self.set_pause_slider.setValue(self.set_pause_spin.value())

    def make_start_call(self):
        if self.amp != None:
            self.amp.make_call()

    # блок "eternet"
    def make_get_name(self):
        self.cml_box.append('CONF?')

    # вывод в cml

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
