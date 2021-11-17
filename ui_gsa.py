# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledLgwfPB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_win(object):
    def setupUi(self, win):
        if not win.objectName():
            win.setObjectName(u"win")
        win.resize(482, 603)
        win.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget = QWidget(win)
        self.centralwidget.setObjectName(u"centralwidget")
        self.get_name_btn_3 = QTabWidget(self.centralwidget)
        self.get_name_btn_3.setObjectName(u"get_name_btn_3")
        self.get_name_btn_3.setGeometry(QRect(10, 10, 461, 68))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 102, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.usbportname = QLabel(self.layoutWidget)
        self.usbportname.setObjectName(u"usbportname")

        self.horizontalLayout_3.addWidget(self.usbportname)

        self.choose_usb = QComboBox(self.layoutWidget)
        self.choose_usb.addItem("")
        self.choose_usb.addItem("")
        self.choose_usb.addItem("")
        self.choose_usb.setObjectName(u"choose_usb")

        self.horizontalLayout_3.addWidget(self.choose_usb)

        self.layoutWidget1 = QWidget(self.tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(290, 10, 161, 25))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.usb_con_btn = QPushButton(self.layoutWidget1)
        self.usb_con_btn.setObjectName(u"usb_con_btn")

        self.horizontalLayout_5.addWidget(self.usb_con_btn)

        self.get_name_btn = QPushButton(self.layoutWidget1)
        self.get_name_btn.setObjectName(u"get_name_btn")

        self.horizontalLayout_5.addWidget(self.get_name_btn)

        self.get_name_btn_3.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.splitter = QSplitter(self.tab_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 10, 441, 25))
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.usbportname_2 = QLabel(self.layoutWidget2)
        self.usbportname_2.setObjectName(u"usbportname_2")

        self.horizontalLayout_4.addWidget(self.usbportname_2)

        self.ip_field = QLineEdit(self.layoutWidget2)
        self.ip_field.setObjectName(u"ip_field")

        self.horizontalLayout_4.addWidget(self.ip_field)

        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.port_field = QLineEdit(self.layoutWidget2)
        self.port_field.setObjectName(u"port_field")

        self.horizontalLayout_4.addWidget(self.port_field)

        self.splitter.addWidget(self.layoutWidget2)
        self.layoutWidget3 = QWidget(self.splitter)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.gridLayout = QGridLayout(self.layoutWidget3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ether_con_btn = QPushButton(self.layoutWidget3)
        self.ether_con_btn.setObjectName(u"ether_con_btn")
        self.ether_con_btn.setEnabled(True)

        self.gridLayout.addWidget(self.ether_con_btn, 0, 0, 1, 1)

        self.get_name_btn_ether = QPushButton(self.layoutWidget3)
        self.get_name_btn_ether.setObjectName(u"get_name_btn_ether")

        self.gridLayout.addWidget(self.get_name_btn_ether, 0, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget3)
        self.get_name_btn_3.addTab(self.tab_2, "")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 280, 461, 171))
        self.layoutWidget4 = QWidget(self.groupBox_2)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 20, 441, 116))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.layoutWidget4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.set_num_pulses_slider = QSlider(self.layoutWidget4)
        self.set_num_pulses_slider.setObjectName(u"set_num_pulses_slider")
        self.set_num_pulses_slider.setMaximum(65535)
        self.set_num_pulses_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.set_num_pulses_slider)

        self.set_num_pulses_spin = QDoubleSpinBox(self.layoutWidget4)
        self.set_num_pulses_spin.setObjectName(u"set_num_pulses_spin")
        self.set_num_pulses_spin.setMaximum(65535.000000000000000)

        self.horizontalLayout_6.addWidget(self.set_num_pulses_spin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.set_amp_pulses_slider = QSlider(self.layoutWidget4)
        self.set_amp_pulses_slider.setObjectName(u"set_amp_pulses_slider")
        self.set_amp_pulses_slider.setMaximum(65535)
        self.set_amp_pulses_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.set_amp_pulses_slider)

        self.set_amp_pulses_spin = QDoubleSpinBox(self.layoutWidget4)
        self.set_amp_pulses_spin.setObjectName(u"set_amp_pulses_spin")
        self.set_amp_pulses_spin.setMaximum(65535.000000000000000)

        self.horizontalLayout_8.addWidget(self.set_amp_pulses_spin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.layoutWidget4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.set_time_pulse_slider = QSlider(self.layoutWidget4)
        self.set_time_pulse_slider.setObjectName(u"set_time_pulse_slider")
        self.set_time_pulse_slider.setMaximum(255)
        self.set_time_pulse_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.set_time_pulse_slider)

        self.set_time_pulse_spin = QDoubleSpinBox(self.layoutWidget4)
        self.set_time_pulse_spin.setObjectName(u"set_time_pulse_spin")
        self.set_time_pulse_spin.setMaximum(255.000000000000000)

        self.horizontalLayout_9.addWidget(self.set_time_pulse_spin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.set_pause_slider = QSlider(self.layoutWidget4)
        self.set_pause_slider.setObjectName(u"set_pause_slider")
        self.set_pause_slider.setMaximum(255)
        self.set_pause_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.set_pause_slider)

        self.set_pause_spin = QDoubleSpinBox(self.layoutWidget4)
        self.set_pause_spin.setObjectName(u"set_pause_spin")
        self.set_pause_spin.setReadOnly(False)
        self.set_pause_spin.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.set_pause_spin.setMaximum(255.000000000000000)

        self.horizontalLayout_10.addWidget(self.set_pause_spin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.start_call = QPushButton(self.groupBox_2)
        self.start_call.setObjectName(u"start_call")
        self.start_call.setGeometry(QRect(380, 140, 71, 23))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 80, 461, 91))
        self.layoutWidget5 = QWidget(self.groupBox)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 20, 441, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_const_slider = QSlider(self.layoutWidget5)
        self.time_const_slider.setObjectName(u"time_const_slider")
        self.time_const_slider.setMaximum(31)
        self.time_const_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.time_const_slider)

        self.time_const_spin_box = QDoubleSpinBox(self.layoutWidget5)
        self.time_const_spin_box.setObjectName(u"time_const_spin_box")
        self.time_const_spin_box.setMaximum(31.000000000000000)
        self.time_const_spin_box.setValue(0.000000000000000)

        self.horizontalLayout.addWidget(self.time_const_spin_box)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.getconf_btn = QPushButton(self.layoutWidget5)
        self.getconf_btn.setObjectName(u"getconf_btn")

        self.verticalLayout.addWidget(self.getconf_btn)

        self.setconf_btn = QPushButton(self.layoutWidget5)
        self.setconf_btn.setObjectName(u"setconf_btn")

        self.verticalLayout.addWidget(self.setconf_btn)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.cml_box = QTextBrowser(self.centralwidget)
        self.cml_box.setObjectName(u"cml_box")
        self.cml_box.setGeometry(QRect(10, 460, 461, 131))
        self.cml_box.setFrameShape(QFrame.StyledPanel)
        self.cml_box.setFrameShadow(QFrame.Sunken)
        self.cml_box.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 170, 461, 111))
        self.gain_coef_widget = QTabWidget(self.groupBox_3)
        self.gain_coef_widget.setObjectName(u"gain_coef_widget")
        self.gain_coef_widget.setGeometry(QRect(10, 20, 441, 81))
        self.gain_coef_widget.setTabShape(QTabWidget.Rounded)
        self.gain_coef_widget.setElideMode(Qt.ElideNone)
        self.CH1 = QWidget()
        self.CH1.setObjectName(u"CH1")
        self.widget = QWidget(self.CH1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 411, 25))
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.setgain_slider = QSlider(self.widget)
        self.setgain_slider.setObjectName(u"setgain_slider")
        self.setgain_slider.setMaximum(255)
        self.setgain_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.setgain_slider)

        self.setgain_spin = QDoubleSpinBox(self.widget)
        self.setgain_spin.setObjectName(u"setgain_spin")
        self.setgain_spin.setMaximum(255.000000000000000)

        self.horizontalLayout_7.addWidget(self.setgain_spin)

        self.setgain_btn = QPushButton(self.widget)
        self.setgain_btn.setObjectName(u"setgain_btn")

        self.horizontalLayout_7.addWidget(self.setgain_btn)

        self.gain_coef_widget.addTab(self.CH1, "")
        self.CH2 = QWidget()
        self.CH2.setObjectName(u"CH2")
        self.layoutWidget_2 = QWidget(self.CH2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 20, 411, 25))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.setgain_slider_2 = QSlider(self.layoutWidget_2)
        self.setgain_slider_2.setObjectName(u"setgain_slider_2")
        self.setgain_slider_2.setMaximum(255)
        self.setgain_slider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.setgain_slider_2)

        self.setgain_spin_2 = QDoubleSpinBox(self.layoutWidget_2)
        self.setgain_spin_2.setObjectName(u"setgain_spin_2")
        self.setgain_spin_2.setMaximum(255.000000000000000)

        self.horizontalLayout_11.addWidget(self.setgain_spin_2)

        self.setgain_btn_2 = QPushButton(self.layoutWidget_2)
        self.setgain_btn_2.setObjectName(u"setgain_btn_2")

        self.horizontalLayout_11.addWidget(self.setgain_btn_2)

        self.gain_coef_widget.addTab(self.CH2, "")
        win.setCentralWidget(self.centralwidget)

        self.retranslateUi(win)

        self.get_name_btn_3.setCurrentIndex(1)
        self.gain_coef_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(win)
    # setupUi

    def retranslateUi(self, win):
        win.setWindowTitle(QCoreApplication.translate("win", u"\u0423\u0441\u0438\u043b\u0438\u0442\u0435\u043b\u044c-\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u0435\u043b\u044c, \u0413\u0421\u0410 ", None))
        self.usbportname.setText(QCoreApplication.translate("win", u"\u041f\u043e\u0440\u0442", None))
        self.choose_usb.setItemText(0, QCoreApplication.translate("win", u"COM1", None))
        self.choose_usb.setItemText(1, QCoreApplication.translate("win", u"COM2", None))
        self.choose_usb.setItemText(2, QCoreApplication.translate("win", u"COM3", None))

        self.choose_usb.setCurrentText(QCoreApplication.translate("win", u"COM1", None))
        self.usb_con_btn.setText(QCoreApplication.translate("win", u"\u0421\u043e\u0435\u0434\u0438\u043d\u0438\u0442\u044c\u0441\u044f", None))
        self.get_name_btn.setText(QCoreApplication.translate("win", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c \u0438\u043c\u044f", None))
        self.get_name_btn_3.setTabText(self.get_name_btn_3.indexOf(self.tab), QCoreApplication.translate("win", u"USB", None))
        self.usbportname_2.setText(QCoreApplication.translate("win", u"IP-\u0430\u0434\u0440\u0435\u0441", None))
        self.ip_field.setPlaceholderText(QCoreApplication.translate("win", u"000.000.000.000", None))
        self.label.setText(QCoreApplication.translate("win", u"\u041f\u043e\u0440\u0442", None))
        self.port_field.setText("")
        self.port_field.setPlaceholderText(QCoreApplication.translate("win", u"0000...", None))
        self.ether_con_btn.setText(QCoreApplication.translate("win", u"\u0421\u043e\u0435\u0434\u0438\u043d\u0438\u0442\u044c\u0441\u044f", None))
        self.get_name_btn_ether.setText(QCoreApplication.translate("win", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c \u0438\u043c\u044f", None))
        self.get_name_btn_3.setTabText(self.get_name_btn_3.indexOf(self.tab_2), QCoreApplication.translate("win", u"Ethernet", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("win", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430 (\u0413\u0421\u0410)", None))
        self.label_2.setText(QCoreApplication.translate("win", u"\u0418\u043c\u043f\u0443\u043b\u044c\u0441\u043e\u0432 ", None))
        self.label_4.setText(QCoreApplication.translate("win", u"\u0410\u043c\u043f\u043b\u0438\u0442\u0443\u0434\u0430", None))
        self.label_5.setText(QCoreApplication.translate("win", u"\u0418\u043c\u043f\u0443\u043b\u044c\u0441     ", None))
        self.label_6.setText(QCoreApplication.translate("win", u"\u041f\u0430\u0443\u0437\u0430         ", None))
        self.start_call.setText(QCoreApplication.translate("win", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("win", u"\u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u0430\u044f \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.getconf_btn.setText(QCoreApplication.translate("win", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.setconf_btn.setText(QCoreApplication.translate("win", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("win", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0443\u0441\u0438\u043b\u0435\u043d\u0438\u044f", None))
        self.setgain_btn.setText(QCoreApplication.translate("win", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.gain_coef_widget.setTabText(self.gain_coef_widget.indexOf(self.CH1), QCoreApplication.translate("win", u"\u041a\u0430\u043d\u0430\u043b 1", None))
        self.setgain_btn_2.setText(QCoreApplication.translate("win", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.gain_coef_widget.setTabText(self.gain_coef_widget.indexOf(self.CH2), QCoreApplication.translate("win", u"\u041a\u0430\u043d\u0430\u043b 2", None))
    # retranslateUi

