#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Файл с механикой персонажей, здесь задаются их параметры и
# функции взаимодействия с окном
# В будущем это будет лишь фрагментом общей программы
import time
from random import *
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class Potion:  # зелье

    def __init__(self, parameter, points, price):
        self.parameter = parameter
        self.points = points
        self.price = price  # Цена предмета, вводится при создании


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
        self.print_info()

    def print_info(self):  # функция, выводящая всю инфу по персонажу
        self.win[0].setText('Здоровье: {}'.format(self.health))
        self.win[1].setText('Урон: {}'.format(self.damage))
        self.win[2].setText('Защита: {}'.format(self.protection + self.out_protec))
        self.win[3].setText('Увертливость: {}'.format(self.evasion + self.out_evas))

    def defend(self):  # функция обороны

        self.out_protec = self.protection * 0.5  # увеличиваем в полтора раза выдаваемую защиту
        self.out_evas = self.evasion * 0.2  # увеличиваем в 1.2 раза выдаваемое уклонение
        return '{} встал в защитную стойку.\n'.format(self.name)

    def attack(self):  # функция атаки

        a = self.rival.set_damage(self.damage)  # наносим сопернику урон
        return '{} атаковал соперника.\n{}'.format(self.name, a)

    def defeated(self):
        return '{} получает ранение и падает без сознания на окровавленные пески Арены...'.format(self.name)

    def set_damage(self, att):  # функция получения урона

        the_ans = 'Шанс попадания {}%\n'.format(100 - self.evasion)  # выводимое в лог сообщение
        chance_to_evade = randint(1, 100)  # число, шанс попадания
        if chance_to_evade > self.evasion:  # если шанс попадания не больше уклонения
            # (т.е. выпало случайное число на кубике)
            critism_of_damage = randint(7, 10) / 10  # коэффициент уменьшения брони
            damage = att - ((
                                        self.protection + self.out_protec) * critism_of_damage)  # формула, высчитывающая нанесенный урон
            damage += att * 0.2
            if damage < 0:
                damage = 0
            self.health -= damage  # формула по вычету здоровья
            if self.health < 0:
                self.health = 0
            # Обновляем сообщение для лога
            the_ans += 'Удар нанес урона {}\n'.format(damage)
        # если шанс попадания входит в диапазон [0, evasion] (Промах)
        else:
            the_ans += 'Промах\n'
        return the_ans


class UiMainWindow(QWidget):

    def __init__(self, hero):
        super().__init__()
        self.turn = 'player'
        # Третье (второе) значение у этих предметов - их цена, расставляй ее там
        self.Items = [Weapon('Меч', 20, 40), Weapon('Боевой топор', 40, 80),
                      Weapon('Боевой молот', 70, 140), Armor('Кираса', 30, 0, 45),
                      Armor('Кольчуга', 60, -30, 90), Armor('Латы', 100, -50, 180)]

        self.ITEMS = {'sword_button': self.Items[0],
                      'axe_button': self.Items[1],
                      'hammer_button': self.Items[2],
                      'cuirass': self.Items[3],
                      'mail_button': self.Items[4],
                      'plate_armor': self.Items[5]}

        self.Rivals = [Person('Шарль Убийца', 80, 15, 40, 60, 40),
                       Person('Харальд', 140, 35, 50, 0, 40),
                       Person("Ураг гро-Шуб", 120, 25, 60, 30, 60),
                       Person('Малакат', 90, 10, 70, 60, 120)]

        self.RIVALS = {'assasin': self.Rivals[0],
                       'barbarian': self.Rivals[1],
                       'orc': self.Rivals[2],
                       'wizard': self.Rivals[3]}

        self.player = hero  # Задаем героя
        self.rival = ''
        self.setObjectName("RPG game")
        self.shop_list = []
        self.main_list = []
        self.fight_list = []
        self.setMinimumSize(QtCore.QSize(971, 716))
        self.setMaximumSize(QtCore.QSize(971, 716))
        self.main_create()
        self.gold = 250  # Количество золота

    def main_create(self):

        self.resize(971, 716)

        centralwidget = QWidget(self)
        centralwidget.setObjectName("centralwidget")

        # Надпись "Характеристики"
        self.label_13 = QLabel(centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.label_13.setObjectName("label_13")

        self.damage = QLabel(centralwidget)
        self.damage.setGeometry(QtCore.QRect(170, 40, 141, 21))
        self.damage.setObjectName("damage")

        self.protection = QLabel(centralwidget)
        self.protection.setGeometry(QtCore.QRect(170, 100, 141, 21))
        self.protection.setObjectName("protection")

        pushButton = QPushButton(centralwidget)
        pushButton.setGeometry(QtCore.QRect(780, 10, 181, 71))
        pushButton.setStyleSheet("background: rgb(34, 168, 19)\n""")
        pushButton.setObjectName("pushButton")
        pushButton.pressed.connect(self.shop_open)

        self.evasion_lab = QLabel(centralwidget)
        self.evasion_lab.setGeometry(QtCore.QRect(170, 70, 141, 21))
        self.evasion_lab.setObjectName("evasion_lab")

        self.hp = QLabel(centralwidget)
        self.hp.setGeometry(QtCore.QRect(170, 10, 141, 21))
        self.hp.setObjectName("hp")

        label_6 = QLabel(centralwidget)
        label_6.setGeometry(QtCore.QRect(250, 180, 231, 300))
        label_6.setObjectName("label_6")
        label_5 = QLabel(centralwidget)
        label_5.setGeometry(QtCore.QRect(10, 180, 231, 300))
        label_5.setObjectName("label_5")
        label_2 = QLabel(centralwidget)
        label_2.setGeometry(QtCore.QRect(490, 180, 231, 300))
        label_2.setObjectName("label_2")
        label_4 = QLabel(centralwidget)
        label_4.setGeometry(QtCore.QRect(730, 180, 231, 300))
        label_4.setObjectName("label_4")
        label = QLabel(centralwidget)
        label.setGeometry(QtCore.QRect(10, 490, 181, 131))
        label.setObjectName("label")
        label_3 = QLabel(centralwidget)
        label_3.setGeometry(QtCore.QRect(250, 490, 151, 131))
        label_3.setObjectName("label_3")
        label_7 = QLabel(centralwidget)
        label_7.setGeometry(QtCore.QRect(490, 490, 151, 131))
        label_7.setObjectName("label_7")
        label_8 = QLabel(centralwidget)
        label_8.setGeometry(QtCore.QRect(730, 490, 111, 131))
        label_8.setObjectName("label_8")

        self.assasin = QPushButton(centralwidget)
        self.assasin.setGeometry(QtCore.QRect(10, 630, 231, 41))
        self.assasin.setObjectName("self.assasin")

        self.barbarian = QPushButton(centralwidget)
        self.barbarian.setGeometry(QtCore.QRect(250, 630, 231, 41))
        self.barbarian.setObjectName("self.barbarian")

        self.orc = QPushButton(centralwidget)
        self.orc.setGeometry(QtCore.QRect(490, 630, 231, 41))
        self.orc.setObjectName("self.orc")

        self.wizard = QPushButton(centralwidget)
        self.wizard.setGeometry(QtCore.QRect(730, 630, 231, 41))
        self.wizard.setObjectName("self.wizard")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_13.setText(_translate("MainWindow", "Ваши характеристики:"))
        pushButton.setText(_translate("MainWindow", "Магазин"))

        self.hp.setText("Здоровье: {}".format(self.player.health))  # Здоровье
        self.damage.setText("Атака: {}".format(self.player.damage))  # Атака героря
        self.protection.setText("Защита: {}".format(self.player.protection))  # Защита
        self.evasion_lab.setText("Увертливость: {}".format(self.player.evasion))  # Уворот
        self.Person_Main = [self.hp, self.damage, self.protection, self.evasion_lab]

        label_6.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                 "<img src=\"barbarian1.jpg\"/></p></body></html>"))
        label_5.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                 "<img src=\"magomed.png\"/></p></body></html>"))
        label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"ork.png\"/></p></body></html>"))
        label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"mag.jpg\"/></p></body></html>"))
        label.setText(_translate("MainWindow", "Шарль Убийца\n"
                                               "Ловкий и увертливый убийца\n"
                                               "\n"
                                               "Характкристики:\n"
                                               "Здоровье : 80\n"
                                               "Атака: 40\n"
                                               "Защита: 15\n"
                                               "Увертливость: 40"))
        label_3.setText(_translate("MainWindow", "Харальд\n"
                                                 "Суровый и сильный воин\n"
                                                 "\n"
                                                 "Характкристики:\n"
                                                 "Здоровье : 140\n"
                                                 "Атака: 50\n"
                                                 "Защита: 35\n"
                                                 "Увертливость: 0"))
        label_7.setText(_translate("MainWindow", "Ураг гро-шуб\n"
                                                 "Прям мега крутой чувак\n"
                                                 "\n"
                                                 "Характкристики:\n"
                                                 "Здоровье : 120\n"
                                                 "Атака: 60\n"
                                                 "Защита: 25\n"
                                                 "Увертливость: 30"))
        label_8.setText(_translate("MainWindow", "Малакат\n"
                                                 "АА Какой чувак\n"
                                                 "\n"
                                                 "Характкристики:\n"
                                                 "Здоровье : 90\n"
                                                 "Атака: 70\n"
                                                 "Защита: 10\n"
                                                 "Увертливость: 40"))

        self.assasin.setText(_translate("MainWindow", "В бой"))
        self.barbarian.setText(_translate("MainWindow", "В бой"))
        self.orc.setText(_translate("MainWindow", "В бой"))
        self.wizard.setText(_translate("MainWindow", "В бой"))

        self.assasin.pressed.connect(self.fight_open)
        self.barbarian.pressed.connect(self.fight_open)
        self.orc.pressed.connect(self.fight_open)
        self.wizard.pressed.connect(self.fight_open)

        # Магазин
        label_31 = QLabel(self)
        label_31.setGeometry(QtCore.QRect(620, 70, 62, 16))
        label_31.setObjectName("label_31")

        label_117 = QLabel(self)
        label_117.setGeometry(QtCore.QRect(700, 120, 61, 28))
        label_117.setObjectName("label_17")

        label_119 = QLabel(self)
        label_119.setGeometry(QtCore.QRect(700, 210, 71, 28))
        label_119.setObjectName("label_19")

        label_116 = QLabel(self)
        label_116.setGeometry(QtCore.QRect(700, 165, 111, 31))
        label_116.setObjectName("label_16")

        self.potion_agility = QPushButton(self)
        self.potion_agility.setGeometry(QtCore.QRect(830, 110, 61, 91))
        self.potion_agility.setObjectName("self.potion_agility")

        label_118 = QLabel(self)
        label_118.setGeometry(QtCore.QRect(700, 267, 71, 31))
        label_118.setObjectName("label_18")

        self.berserker = QPushButton(self)
        self.berserker.setGeometry(QtCore.QRect(830, 210, 61, 91))
        self.berserker.setObjectName("self.berserker")

        self.stone_skin = QPushButton(self)
        self.stone_skin.setGeometry(QtCore.QRect(830, 310, 61, 91))
        self.stone_skin.setObjectName("self.stone_skin")

        label_211 = QLabel(self)
        label_211.setGeometry(QtCore.QRect(700, 370, 111, 31))
        label_211.setObjectName("label_21")

        label_210 = QLabel(self)
        label_210.setGeometry(QtCore.QRect(700, 310, 91, 41))
        label_210.setObjectName("label_20")

        label_312 = QLabel(self)
        label_312.setGeometry(QtCore.QRect(620, 110, 61, 91))
        label_312.setObjectName("label_32")

        label_313 = QLabel(self)
        label_313.setGeometry(QtCore.QRect(620, 210, 61, 91))
        label_313.setObjectName("label_33")

        label_314 = QLabel(self)
        label_314.setGeometry(QtCore.QRect(620, 310, 61, 91))
        label_314.setObjectName("label_34")

        label01 = QLabel(self)
        label01.setGeometry(QtCore.QRect(10, 70, 61, 16))
        label01.setObjectName("label")

        label_216 = QLabel(self)
        label_216.setGeometry(QtCore.QRect(10, 110, 61, 91))
        label_216.setObjectName("label_26")

        label_217 = QLabel(self)
        label_217.setGeometry(QtCore.QRect(10, 210, 61, 91))
        label_217.setObjectName("label_27")

        label_61 = QLabel(self)
        label_61.setGeometry(QtCore.QRect(90, 220, 41, 16))
        label_61.setObjectName("label_6")

        label_41 = QLabel(self)
        label_41.setGeometry(QtCore.QRect(90, 110, 48, 16))
        label_41.setObjectName("label_4")

        label_51 = QLabel(self)
        label_51.setGeometry(QtCore.QRect(90, 130, 71, 21))
        label_51.setObjectName("label_5")

        label_71 = QLabel(self)
        label_71.setGeometry(QtCore.QRect(90, 240, 108, 32))
        label_71.setObjectName("label_7")

        self.sword_button = QPushButton(self)
        self.sword_button.setGeometry(QtCore.QRect(210, 110, 61, 91))
        self.sword_button.setObjectName("self.sword_button")

        label_218 = QLabel(self)
        label_218.setGeometry(QtCore.QRect(10, 320, 91, 91))
        label_218.setObjectName("label_28")

        label_81 = QLabel(self)
        label_81.setGeometry(QtCore.QRect(90, 320, 91, 31))
        label_81.setObjectName("label_8")

        label_91 = QLabel(self)
        label_91.setGeometry(QtCore.QRect(90, 340, 121, 31))
        label_91.setObjectName("label_9")

        self.axe_button = QPushButton(self)
        self.axe_button.setGeometry(QtCore.QRect(210, 210, 61, 91))
        self.axe_button.setObjectName("self.axe_button")

        self.hammer_button = QPushButton(self)
        self.hammer_button.setGeometry(QtCore.QRect(210, 320, 61, 91))
        self.hammer_button.setObjectName("self.hammer_button")

        label_21 = QLabel(self)
        label_21.setGeometry(QtCore.QRect(360, 70, 83, 16))
        label_21.setObjectName("label_2")

        label_110 = QLabel(self)
        label_110.setGeometry(QtCore.QRect(390, 110, 41, 16))
        label_110.setObjectName("label_10")

        label_112 = QLabel(self)
        label_112.setGeometry(QtCore.QRect(390, 220, 61, 16))
        label_112.setObjectName("label_12")

        label_114 = QLabel(self)
        label_114.setGeometry(QtCore.QRect(390, 332, 124, 20))
        label_114.setObjectName("label_14")

        label_111 = QLabel(self)
        label_111.setGeometry(QtCore.QRect(390, 130, 81, 21))
        label_111.setObjectName("label_11")

        label_113 = QLabel(self)
        label_113.setGeometry(QtCore.QRect(390, 240, 111, 32))
        label_113.setObjectName("label_13")

        label_115 = QLabel(self)
        label_115.setGeometry(QtCore.QRect(390, 352, 111, 31))
        label_115.setObjectName("label_15")

        label_212 = QLabel(self)
        label_212.setGeometry(QtCore.QRect(310, 110, 71, 91))
        label_212.setObjectName("label_22")

        label_213 = QLabel(self)
        label_213.setGeometry(QtCore.QRect(310, 210, 71, 91))
        label_213.setObjectName("label_23")

        label_214 = QLabel(self)
        label_214.setGeometry(QtCore.QRect(310, 320, 61, 81))
        label_214.setObjectName("label_24")

        self.mail_button = QPushButton(self)
        self.mail_button.setGeometry(QtCore.QRect(520, 210, 61, 91))
        self.mail_button.setObjectName("self.mail_button")

        self.plate_armor = QPushButton(self)
        self.plate_armor.setGeometry(QtCore.QRect(520, 310, 61, 91))
        self.plate_armor.setObjectName("self.plate_armor")

        self.cuirass = QPushButton(self)
        self.cuirass.setGeometry(QtCore.QRect(520, 110, 61, 91))
        self.cuirass.setObjectName("self.cuirass")

        pushButton_71 = QPushButton(self)
        pushButton_71.setGeometry(QtCore.QRect(355, 10, 211, 31))
        pushButton_71.setStyleSheet("background: rgb(34, 168, 19)\n""")
        pushButton_71.setObjectName("pushButton_7")
        pushButton_71.pressed.connect(self.main_open)

        self.gold_label = QLabel(self)
        self.gold_label.setGeometry(100, 22, 100, 16)
        self.gold_label.setObjectName("gold_label")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate

        label_31.setText("Зелья:")
        label01.setText(_translate("Form", "Оружие:"))

        label_312.setText(_translate("Form", "<html><head/><body><p><img src=\"lovkost.png\"/></p></body></html>"))
        label_313.setText(_translate("Form", "<html><head/><body><p><img src=\"berserk.png\"/></p></body></html>"))
        label_314.setText(_translate("Form", "<html><head/><body><p><img src=\"poition1.jpg\"/></p></body></html>"))

        label_216.setText(_translate("Form", "<html><head/><body><p><img src=\"sword.png\"/></p></body></html>"))
        label_217.setText(_translate("Form", "<html><head/><body><p><img src=\"axe.jpg\"/></p></body></html>"))
        label_218.setText(_translate("Form", "<html><head/><body><p><img src=\"hammer.jpg\"/></p></body></html>"))

        # НАДПИСИ С НАЗВАНИЯМИ И ХАРАКТЕРИСТИКАМИ ПРЕДМЕТОВ
        label_41.setText(_translate("Form", "Меч"))
        label_51.setText(_translate("Form", "урон: +20"))
        label_61.setText(_translate("Form", "Топор"))
        label_71.setText(_translate("Form", "урон: +40"))
        label_81.setText("Боевой молот")
        label_91.setText("урон: +70")

        label_117.setText("Зелье\nловкости")
        label_119.setText("Зелье\nберсеркера")
        label_210.setText(_translate("Form", "Зелье\nстальной кожи"))
        label_116.setText(_translate("Form", "увертливость: +30"))
        label_118.setText(_translate("Form", "атака: +30"))
        label_211.setText(_translate("Form", "защита: +30"))

        label_21.setText(_translate("Form", "Броня:"))
        label_110.setText(_translate("Form", "Кираса"))
        label_112.setText(_translate("Form", "Кольчуга"))
        label_114.setText(_translate("Form", "Латы"))
        label_111.setText(_translate("Form", "защита: +30"))
        label_113.setText("защита: +60\nувертливость: -20")
        label_115.setText("защита: +100\nувертливость: -50")

        # КНОПКИ ПОКУПКИ ПРЕДМЕТОВ
        self.sword_button.setText("Купить")
        self.sword_button.pressed.connect(self.buy_item)
        self.axe_button.setText("Купить")
        self.axe_button.pressed.connect(self.buy_item)
        self.hammer_button.setText("Купить")
        self.hammer_button.pressed.connect(self.buy_item)

        self.cuirass.setText("Купить")
        self.cuirass.pressed.connect(self.buy_item)
        self.mail_button.setText("Купить")
        self.mail_button.pressed.connect(self.buy_item)
        self.plate_armor.setText("Купить")
        self.plate_armor.pressed.connect(self.buy_item)

        self.potion_agility.setText("Купить")
        # self.potion_agility.pressed.connect(self.buy_item)
        self.berserker.setText("Купить")
        # self.berserker.pressed.connect(self.buy_item)
        self.stone_skin.setText("Купить")
        # self.stone_skin.pressed.connect(self.buy_item)

        label_212.setText(_translate("Form", "<html><head/><body><p><img src=\"cuirass.jpg\"/></p></body></html>"))
        label_213.setText(_translate("Form", "<html><head/><body><p><img src=\"chain.jpg\"/></p></body></html>"))
        label_214.setText(_translate("Form", "<html><head/><body><p><img src=\"armor.png\"/></p></body></html>"))

        pushButton_71.setText(_translate("Form", "Назад"))

        self.shop_list = [label_31, label_117, label_119, label_116, self.potion_agility, label_118,
                          self.berserker, self.stone_skin, label_211, label_210, label_312, label_313,
                          label_314, label01, label_216, label_217, label_61, label_41,
                          label_51, label_71, self.sword_button, label_218, label_81, label_91,
                          self.axe_button, self.hammer_button, label_21, label_110, label_112,
                          label_114, label_111, label_113, label_115, label_212, label_213,
                          label_214, self.mail_button, self.plate_armor, self.cuirass, pushButton_71,
                          self.gold_label]

        # self.setLayout(self.grid)
        self.main_list = [self.label_13, self.damage, self.protection, pushButton, self.evasion_lab,
                          self.hp, label_6, label_5, label_2, label_4, label,
                          label_3, label_7, label_8, self.assasin, self.barbarian, self.orc,
                          self.wizard]
        for i in self.shop_list:
            i.hide()

        self.BUTTONS = {self.Items[0]: self.sword_button,
                        self.Items[1]: self.axe_button,
                        self.Items[2]: self.hammer_button,
                        self.Items[3]: self.cuirass,
                        self.Items[4]: self.mail_button,
                        self.Items[5]: self.plate_armor}

        # Бой

        progressBars = QProgressBar(self)
        progressBars.setGeometry(QtCore.QRect(40, 80, 171, 23))
        progressBars.setProperty("value", 24)
        progressBars.setObjectName("progressBar")

        self.enemy_hp = QLabel(self)
        self.enemy_hp.setGeometry(QtCore.QRect(70, 60, 121, 16))
        self.enemy_hp.setObjectName("self.enemy_hp")

        self.textBrowsers = QTextBrowser(self)
        self.textBrowsers.setGeometry(QtCore.QRect(270, 90, 372, 301))
        self.textBrowsers.setObjectName("textBrowser")

        label_3s = QLabel(self)
        label_3s.setGeometry(QtCore.QRect(60, 140, 55, 16))
        label_3s.setObjectName("label_3")

        self.enemy_evasion = QLabel(self)
        self.enemy_evasion.setGeometry(QtCore.QRect(60, 260, 151, 16))
        self.enemy_evasion.setObjectName("self.enemy_evasion")

        self.enemy_protect = QLabel(self)
        self.enemy_protect.setGeometry(QtCore.QRect(60, 160, 101, 16))
        self.enemy_protect.setObjectName("self.enemy_protect")

        label_6s = QLabel(self)
        label_6s.setGeometry(QtCore.QRect(60, 280, 41, 16))
        label_6s.setObjectName("label_6")

        progressBar_2s = QProgressBar(self)
        progressBar_2s.setGeometry(QtCore.QRect(720, 80, 171, 23))
        progressBar_2s.setProperty("value", 24)
        progressBar_2s.setObjectName("progressBar_2")

        self.player_hp = QLabel(self)
        self.player_hp.setGeometry(QtCore.QRect(750, 60, 121, 16))
        self.player_hp.setObjectName("self.player_hp")

        label_12s = QLabel(self)
        label_12s.setGeometry(QtCore.QRect(60, 200, 55, 16))
        label_12s.setObjectName("label_12")

        self.enemy_damage = QLabel(self)
        self.enemy_damage.setGeometry(QtCore.QRect(60, 211, 101, 16))
        self.enemy_damage.setObjectName("self.enemy_damage")

        self.player_protect = QLabel(self)
        self.player_protect.setGeometry(QtCore.QRect(760, 160, 101, 16))
        self.player_protect.setObjectName("self.player_protect")

        label_9s = QLabel(self)
        label_9s.setGeometry(QtCore.QRect(760, 140, 55, 16))
        label_9s.setObjectName("label_9")

        self.player_damage = QLabel(self)
        self.player_damage.setGeometry(QtCore.QRect(760, 211, 151, 16))
        self.player_damage.setObjectName("self.player_damage")

        label_10s = QLabel(self)
        label_10s.setGeometry(QtCore.QRect(760, 280, 51, 16))
        label_10s.setObjectName("label_10")

        self.player_evasion = QLabel(self)
        self.player_evasion.setGeometry(QtCore.QRect(760, 260, 151, 16))
        self.player_evasion.setObjectName("self.player_evasion")

        label_15s = QLabel(self)
        label_15s.setGeometry(QtCore.QRect(760, 200, 55, 16))
        label_15s.setObjectName("label_15")

        self.attack_button = QPushButton(self)
        self.attack_button.setGeometry(QtCore.QRect(270, 390, 171, 51))
        self.attack_button.setObjectName("self.attack_button")

        self.defend_button = QPushButton(self)
        self.defend_button.setGeometry(QtCore.QRect(472, 390, 171, 51))
        self.defend_button.setObjectName("self.defend_button")

        self.leave = QPushButton(self)
        self.leave.setGeometry(QtCore.QRect(350, 20, 201, 51))
        self.leave.setStyleSheet("background: rgb(34, 168, 19)\n")
        self.leave.setObjectName("pushButton_7")
        self.leave.pressed.connect(self.main_open)
        self.leave.pressed.connect(self.escape)

        label_16s = QLabel(self)
        label_16s.setGeometry(QtCore.QRect(780, 20, 21, 16))
        label_16s.setObjectName("label_16")

        self.enemy_name = QLabel(self)
        self.enemy_name.setGeometry(QtCore.QRect(80, 20, 95, 16))
        self.enemy_name.setObjectName("self.enemy_name")

        _translates = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translates("Form", "Form"))

        # Характеристики врага
        self.enemy_hp.setText(_translates("Form", "Здоровье: {}"))  # label_2s
        self.enemy_damage.setText(_translates("Form", "Урон: {}"))  # label_13s
        self.enemy_protect.setText(_translates("Form", "Защита: {}"))  # label_5s
        self.enemy_evasion.setText(_translates("Form", "Увертливость: {}"))  # label_4s

        # Характеристики игрока
        self.player_hp.setText(_translates("Form", "Здоровье: {}"))  # label_7s
        self.player_protect.setText(_translates("Form", "Защита: {}"))  # label_8s
        self.player_damage.setText(_translates("Form", "Урон: {}"))  # label_14
        self.player_evasion.setText(_translates("Form", "Увертливость: {}"))  # label_11

        # надписи для игрока
        self.player_fight = [self.player_hp, self.player_damage, self.player_protect, self.player_evasion]

        # надписи для врага
        self.enemy_fight = [self.enemy_hp, self.enemy_damage, self.enemy_protect, self.enemy_evasion]

        self.attack_button.setText(_translate("Form", "Атаковать"))
        self.defend_button.setText(_translate("Form", "Защищаться"))
        self.attack_button.pressed.connect(self.attack)
        self.defend_button.pressed.connect(self.defend)

        self.leave.setText(_translate("Form", "Покинуть бой"))
        label_16s.setText(_translate("Form", "Вы"))
        self.enemy_name.setText(_translate("Form", "Ловкач"))

        self.fight_list = [self.enemy_hp, label_3s, self.enemy_evasion, self.enemy_protect,
                           label_6s, self.textBrowsers, self.player_hp, self.player_protect, label_9s,
                           label_10s, self.player_evasion, label_12s, self.enemy_damage,
                           self.player_damage, label_15s, progressBar_2s, progressBars,
                           self.defend_button, self.attack_button, self.leave,
                           self.enemy_name, label_16s]

        for i in self.fight_list:
            i.hide()

    # ФУНКЦИЯ ПОКУПКИ ПРЕДМЕТА
    def buy_item(self):
        a = self.sender().objectName().split('.')[1]  # Вытаскиваем название кнопки
        item = self.ITEMS[a]

        if self.gold >= item.get_price():
            self.sender().setText('Надеть')
            self.sender().disconnect()
            self.sender().pressed.connect(self.equip)
            self.gold -= item.get_price()

    def shop_open(self):
        self.player.set_win(self.Person_Main)
        for i in self.main_list:
            i.hide()
        for i in self.shop_list:
            i.show()
        self.gold_label.setText("Ваше золото: {}".format(self.gold))
        self.setWindowTitle("Магазин")

    def fight_open(self):  # НАЧАЛО БОЯ
        self.player.set_win(self.player_fight)
        self.player.print_info()
        self.turn = 'player'

        for i in self.fight_list:
            i.show()
        for i in self.main_list:
            i.hide()

        a = self.sender().objectName().split('.')[1]  # Вытаскиваем название кнопки
        self.rival = self.RIVALS[a]  # Достаем соперника из списка боссов
        self.rival.set_win(
            self.enemy_fight)  # Устанавливаем для врага список элементов-надписей, которые он будет изменять
        self.rival.print_info()  # Выводим информацию о характеристиках врагов
        self.rival.set_rival(self.player)  # Устанавливаем врагу в качестве соперника игрока
        self.player.set_rival(self.rival)  # Добавляем герою врага (чтобы было кого бить)
        self.enemy_name.setText(self.rival.name)  # Имя врага

        self.textBrowsers.append('''{} готов к сражению.
Бой начался\nВаш ход первый.\n'''.format(self.rival.name))

        self.setWindowTitle("Бой")

    def attack(self):
        if self.turn == 'player':
            self.textBrowsers.append(self.player.attack())
            self.player.print_info()
            self.rival.print_info()
            if self.rival.health == 0:
                self.textBrowsers.append(self.rival.defeated())
                self.textBrowsers.append('Вы выиграли бой!')
                self.player.money += self.rival.money
                self.attack_button.hide()
                self.defend_button.hide()
            else:
                self.turn = 'enemy'
                self.rival.end_defend()
                self.enemy_turn()

    def defend(self):
        if self.turn == 'player':
            self.textBrowsers.append(self.player.defend())
            self.player.print_info()
            self.turn = 'enemy'
            self.rival.end_defend()
            self.enemy_turn()

    def enemy_turn(self):
        self.textBrowsers.append(self.rival.attack())
        self.player.print_info()
        if self.player.health == 0:
            self.textBrowsers.append(self.player.defeated())
            self.textBrowsers.append('Вы проиграли бой.')
            self.attack_button.hide()
            self.defend_button.hide()
        else:
            self.turn = 'player'
        self.player.end_defend()

    def escape(self):
        self.textBrowsers.setPlainText('')
        self.player.end_defend()
        self.rival.end_defend()
        self.player.return_defaults()
        self.rival.return_defaults()

    def equip(self):
        a = self.sender().objectName().split('.')[1]  # Вытаскиваем название кнопки
        item = self.ITEMS[a]  # объект одеваемого предмета

        if item.i_type == 'weapon':
            if self.player.equip_weapon not in self.Items:
                self.sender().setText('Снять')
                self.player.set_new_weapon(item)
            elif self.player.equip_weapon == item:
                self.sender().setText('Надеть')
                self.player.set_new_weapon(Weapon('Кулаки', 0, 0))
            else:
                self.sender().setText('Снять')
                self.BUTTONS[self.player.equip_weapon].setText('Надеть')
                self.player.set_new_weapon(item)

        elif item.i_type == 'armor':
            if self.player.equip_armor not in self.Items:
                self.sender().setText('Снять')
                self.player.set_new_armor(item)
            elif self.player.equip_armor == item:
                self.sender().setText('Надеть')
                self.player.set_new_armor(Armor('', 0, 0, 0))
            else:
                self.sender().setText('Снять')
                self.BUTTONS[self.player.equip_armor].setText('Надеть')
                self.player.set_new_armor(item)

    def main_open(self):
        self.player.set_win(self.Person_Main)
        for i in self.main_list:
            i.show()
        for i in self.shop_list:
            i.hide()
        for i in self.fight_list:
            i.hide()

    def get_player(self):  # Функция, возвращающая игрока, чтобы изменять его данные
        return self.player


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UiMainWindow(Person('Гюнтер', 100, 0, 0, 10, 50))
    window.get_player().set_win(window)
    window.show()
    sys.exit(app.exec())
