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


class Person:  # класс персонажа

    # В конструкторе задаются начальное здоровье, защита, урон без оружия и уклонение
    def __init__(self, name, health, protection, damage, evasion, money):  # конструктор

        # Изменяемые в бою переменные, которые используются в расчетах при обороне/ударе
        self.out_protec = 0  # Защита (при обороне увеличивается)
        self.out_evas = 0  # Уклонение (при обороне увеличивается)

        self.defaults = [health, protection, damage, evasion]

        # Постоянные (или полупостоянные) переменные, которые служат основой характерист персонажа
        self.name = name  # имя перса
        self.health = health  # дефолтное здоровье
        self.protection = protection  # дефолтная броня
        self.damage = damage  # дефолтный урон (кулаками)
        self.real_evasion = evasion  # считаемый уворот
        self.evasion = evasion  # выводимый уворот
        self.equip_armor = Armor('', 0, 0, 0)  # дефолтная броня, надетая на перса
        self.equip_weapon = Weapon('Кулаки', 3, 0)  # дефолтное оружие, надетое на перса
        self.rival = ''  # Соперник
        self.win = ''  # Список, в котором выводится вся инфа персонажа
        self.potion_effects = {'evasion': 0, 'damage': 0, 'protect': 0}  # Эффекты от зелий

        self.money = money  # Золото игрока (запас денег игрока)

    def set_win(self, win):  # Функция, в которой устанавливается класс, для вывода в нем инфы персонажа
        self.win = win

    def unset_armor(self):  # Функция по сниманию брони
        self.protection -= self.equip_armor.protection  # Удаляем защиту брони
        self.real_evasion -= self.equip_armor.evasion  # Удаляем штраф/бонус к уклонению от брони
        self.evasion = self.real_evasion
        self.equip_armor = ''  # Удаляем броню
        self.defaults[1] = self.protection
        self.defaults[3] = self.evasion
        if self.win != '':
            self.print_info()  # Обновляем информацию в окне

    def unset_weapon(self):  # Функция по сниманию оружия
        self.damage -= self.equip_weapon.damage  # Удаляем атаку старого оружия
        self.equip_weapon = ''  # Удаляем броню
        self.defaults[2] = self.damage
        if self.win != '':
            self.print_info()  # Обновляем информацию в окне

    def set_new_armor(self, new_arm):  # функция по одеванию новой броньки на персонажа
        if self.equip_armor != '':  # Если есть какая-то другая броня, то
            self.unset_armor()  # снимаем старую броню
        self.equip_armor = new_arm  # Устанавливаем новую броню
        self.protection += new_arm.protection  # Добавляем к себе ее защиту
        self.real_evasion += new_arm.evasion  # Добавляем к себе ее штраф/бонус к уклонению
        if self.real_evasion < 0:  # предотвращаем отрицательное уклонение
            self.evasion = 0  # если уклонение получилось меньше 0, то устанавливаем его на 0
        elif self.real_evasion > 90:  # предотвращено максимальное уклонение (иначе это имба
            self.evasion = 100
        else:
            self.evasion = self.real_evasion
            # Уклонение для расчета в бою будет браться из self.evasion
            # self.real_evasion нужен только для случаев, когда штраф брони больше уклонения игрока
        self.defaults[1] = self.protection
        self.defaults[3] = self.evasion
        if self.win != '':
            self.print_info()  # Обновляем информацию в окне

    def set_new_weapon(self, new_weap):  # функция по одеванию нового оружия
        if self.equip_weapon != '':  # Если есть какое-то другое оружие в руках, то
            self.unset_weapon()  # снимаем старое оружие
        self.equip_weapon = new_weap  # устанавливаем новое оружие
        self.damage = new_weap.damage  # добавляем урон оружия
        self.defaults[2] = self.damage
        if self.win != '':
            self.print_info()  # Обновляем информацию в окне

    def set_rival(self, rival):  # функция по добавлению соперника
        self.rival = rival

    def end_defend(self):
        self.out_evas = 0
        self.out_protec = 0
        self.print_info()

    def return_defaults(self):
        self.health = self.defaults[0]
        self.damage = self.defaults[2]
        self.protection = self.defaults[1]
        self.evasion = self.defaults[3]
        for i in self.potion_effects.keys():
            self.potion_effects[i] = 0
        self.print_info()

    def drink(self, potion):  # функция для выпивания зелий
        self.potion_effects[potion.get_bonus()[0]] += potion.get_bonus()[1]
        print(self.potion_effects)

    def print_info(self):  # функция, выводящая всю инфу по персонажу
        self.win[0].setText('Здоровье: {}'.format(self.health))
        self.win[1].setText('Урон: {}'.format(self.damage + self.potion_effects['damage']))
        self.win[2].setText('Защита: {}'.format(self.protection + self.out_protec + self.potion_effects['protect']))
        self.win[3].setText('Увертливость: {}'.format(self.evasion + self.out_evas + self.potion_effects['evasion']))

    def defend(self):  # функция обороны

        self.out_protec = self.protection  # увеличиваем в два раза выдаваемую защиту
        self.out_evas = self.evasion * 0.2  # увеличиваем в 1.2 раза выдаваемое уклонение
        return '{} встал в защитную стойку.'.format(self.name)

    def attack(self):  # функция атаки

        a = self.rival.set_damage(self.damage + self.potion_effects['damage'])  # наносим сопернику урон
        return '{} атаковал соперника.\n{}'.format(self.name, a)

    def defeated(self):
        return '{} получает ранение и падает без сознания на окровавленные пески Арены...'.format(self.name)

    def set_damage(self, att):  # функция получения урона

        current_protec = self.protection + self.out_protec + self.potion_effects['protect']
        current_evasion = self.evasion + self.out_evas + self.potion_effects['evasion']

        the_ans = 'Шанс попадания {}%\n'.format(100 - current_evasion)  # выводимое в лог сообщение
        chance_to_evade = randint(1, 100)  # число, шанс попадания
        if chance_to_evade > current_evasion:  # если шанс попадания не больше уклонения
            # (т.е. выпало случайное число на кубике)
            critism_of_damage = randint(8, 10) / 10  # коэффициент уменьшения брони
            damage = att - (current_protec * critism_of_damage)  # формула, высчитывающая нанесенный урон
            if damage < 0:
                damage = att * 0.25
            self.health -= damage  # формула по вычету здоровья
            if self.health < 0:
                self.health = 0
            # Обновляем сообщение для лога
            the_ans += 'Удар нанес урона {}'.format(int(damage))
        # если шанс попадания входит в диапазон [0, evasion] (Промах)
        else:
            the_ans += 'Промах'
        return the_ans

