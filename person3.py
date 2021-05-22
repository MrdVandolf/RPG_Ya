#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Файл с механикой персонажей, здесь задаются их параметры и
# функции взаимодействия с окном
# В будущем это будет лишь фрагментом общей программы
from random import *
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class Dialog(QWidget):

    def __init__(self, num, change, state, change2):

        super().__init__()
        self.setObjectName("Dialog")
        self.resize(190, 170)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 101, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.close())
        self.pushButton.pressed.connect(change2)
        self.pushButton.pressed.connect(change)
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.label.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        if state == 'winner':
            self.label.setText(_translate("Dialog", "Вы получили награду за бой\n"
                                                    "в размере {} золотых").format(num))
        elif state == 'champion':
            self.label.setText(_translate("Dialog", "Отныне вы - Чемпион Арены!\n"
                                                    "Ваша награда - {} золотых").format(num))
        else:
            self.label.setText(_translate("Dialog", "Вы проиграли бой, обагрив\n"
                                                    "своей кровью пески Арены.").format(num))

class Potion:  # зелье

    def __init__(self, parameter, points, price):
        self.parameter = parameter
        self.points = points
        self.i_type = 'potion'
        self.price = price  # Цена предмета, вводится при создании

    def get_price(self):
        return self.price

    def get_bonus(self):
        return self.parameter, self.points


class Armor:  # класс брони

    def __init__(self, name, protection, evasion, price):  # конструктор
        self.name = name  # название
        self.protection = protection  # Защита этой броней
        self.evasion = evasion  # Штраф/бонус к уклонению
        self.i_type = 'armor'
        self.price = price  # цена предмета

    def name(self):  # функция, возвращающая название предмета
        return self.name

    def get_price(self):
        return self.price


class Weapon:  # класс оружия

    def __init__(self, name, damage, price):  # конструктор
        self.name = name  # название
        self.damage = damage  # Урон этого оружия
        self.i_type = 'weapon'
        self.price = price  # цена

    def name(self):  # функция, возвращающая название предмета
        return self.name

    def get_price(self):
        return self.price

