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


class UiMainWindow(QWidget):

    def __init__(self, hero):
        super().__init__()
        self.turn = 'player'
        self.action_points = 2
        # Третье (второе) значение у этих предметов - их цена, расставляй ее там
        self.Items = [Weapon('Меч', 20, 30), Weapon('Боевой топор', 40, 50),
                      Weapon('Боевой молот', 70, 80), Armor('Кираса', 30, 0, 20),
                      Armor('Кольчуга', 60, -30, 55), Armor('Латы', 100, -50, 100),
                      Potion('evasion', 30, 30), Potion('damage', 30, 30),
                      Potion('protect', 30, 30)]

        self.ITEMS = {'sword_button': self.Items[0],
                      'axe_button': self.Items[1],
                      'hammer_button': self.Items[2],
                      'cuirass': self.Items[3],
                      'mail_button': self.Items[4],
                      'plate_armor': self.Items[5],
                      'potion_agility': self.Items[6],
                      'berserker': self.Items[7],
                      'stone_skin': self.Items[8]}

        self.Rivals = [Person('Шарль Убийца', 80, 5, 40, 50, 40),
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
        self.main_create()

    def main_create(self):
        
        self.move(100, 100)

        centralwidget = QWidget(self)
        centralwidget.setObjectName("centralwidget")
        self.grid = QGridLayout(self)

        # Надпись "Характеристики"
        self.label_13 = QLabel(centralwidget)
        self.label_13.setObjectName("label_13")

        self.damage = QLabel(centralwidget)
        self.damage.setObjectName("damage")

        self.protection = QLabel(centralwidget)
        self.protection.setObjectName("protection")

        pushButton = QPushButton(centralwidget)
        pushButton.setStyleSheet("background: rgb(34, 168, 19)\n""")
        pushButton.setObjectName("pushButton")
        pushButton.pressed.connect(self.shop_open)

        self.evasion_lab = QLabel(centralwidget)
        self.evasion_lab.setObjectName("evasion_lab")

        self.hp = QLabel(centralwidget)
        self.hp.setObjectName("hp")

        label_6 = QLabel(centralwidget)
        label_6.setObjectName("label_6")
        
        label_5 = QLabel(centralwidget)
        label_5.setObjectName("label_5")
        
        label_2 = QLabel(centralwidget)
        label_2.setObjectName("label_2")
        
        label_4 = QLabel(centralwidget)
        label_4.setObjectName("label_4")
        
        label = QLabel(centralwidget)
        label.setObjectName("label")
        
        label_3 = QLabel(centralwidget)
        label_3.setObjectName("label_3")
        
        label_7 = QLabel(centralwidget)
        label_7.setObjectName("label_7")
        
        label_8 = QLabel(centralwidget)
        label_8.setObjectName("label_8")

        self.assasin = QPushButton(centralwidget)
        self.assasin.setObjectName("self.assasin")

        self.barbarian = QPushButton(centralwidget)
        self.barbarian.setObjectName("self.barbarian")

        self.orc = QPushButton(centralwidget)
        self.orc.setObjectName("self.orc")

        self.wizard = QPushButton(centralwidget)
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
        
        label.setText(_translate("MainWindow", "{}\n"
                                   "Ловкий и увертливый убийцв\n\n"
                                   "Характкристики:\n"
                                   "Здоровье : {}\n"
                                   "Атака: {}\n"
                                   "Защита: {}\n"
                                   "Увертливость: {}".format(self.Rivals[0].name,
                                   self.Rivals[0].health, self.Rivals[0].damage,
                                   self.Rivals[0].protection, self.Rivals[0].evasion)))
        
        label_3.setText(_translate("MainWindow", "{}\n"
                                   "Жестокий и сильный воин\n\n"
                                   "Характкристики:\n"
                                   "Здоровье : {}\n"
                                   "Атака: {}\n"
                                   "Защита: {}\n"
                                   "Увертливость: {}".format(self.Rivals[1].name,
                                   self.Rivals[1].health, self.Rivals[1].damage,
                                   self.Rivals[1].protection, self.Rivals[1].evasion)))
        
        label_7.setText(_translate("MainWindow", "{}\n"
                                   "Великий ветеран Арены\n\n"
                                   "Характкристики:\n"
                                   "Здоровье : {}\n"
                                   "Атака: {}\n"
                                   "Защита: {}\n"
                                   "Увертливость: {}".format(self.Rivals[2].name,
                                   self.Rivals[2].health, self.Rivals[2].damage,
                                   self.Rivals[2].protection, self.Rivals[2].evasion)))
        
        label_8.setText(_translate("MainWindow", "{}\n"
                                   "Вечный Чемпион Арены\n\n"
                                   "Характкристики:\n"
                                   "Здоровье : {}\n"
                                   "Атака: {}\n"
                                   "Защита: {}\n"
                                   "Увертливость: {}".format(self.Rivals[3].name,
                                   self.Rivals[3].health, self.Rivals[3].damage,
                                   self.Rivals[3].protection, self.Rivals[3].evasion)))
        

        self.assasin.setText(_translate("MainWindow", "В бой"))
        self.barbarian.setText(_translate("MainWindow", "В бой"))
        self.orc.setText(_translate("MainWindow", "В бой"))
        self.wizard.setText(_translate("MainWindow", "В бой"))

        self.assasin.pressed.connect(self.fight_open)
        self.barbarian.pressed.connect(self.fight_open)
        self.orc.pressed.connect(self.fight_open)
        self.wizard.pressed.connect(self.fight_open)
        
        self.grid.addWidget(self.label_13, 0, 0, 1, 1)
        self.grid.addWidget(self.damage, 1, 1, 1, 1)
        self.grid.addWidget(self.protection, 2, 1, 1, 1)
        self.grid.addWidget(self.hp, 0, 1, 1, 1)
        self.grid.addWidget(self.evasion_lab, 3, 1, 1, 1)
        self.grid.addWidget(pushButton, 0, 3, 1, 1)
        self.grid.addWidget(label_6, 4, 1, 1, 1)
        self.grid.addWidget(label_5, 4, 0, 1, 1)
        self.grid.addWidget(label_2, 4, 2, 1, 1)
        self.grid.addWidget(label_4, 4, 3, 1, 1)
        self.grid.addWidget(label, 5, 0, 1, 1)
        self.grid.addWidget(label_3, 5, 1, 1, 1)
        self.grid.addWidget(label_7, 5, 2, 1, 1)
        self.grid.addWidget(label_8, 5, 3, 1, 1)
        self.grid.addWidget(self.assasin, 6, 0, 1, 1)
        self.grid.addWidget(self.barbarian, 6, 1, 1, 1)
        self.grid.addWidget(self.orc, 6, 2, 1, 1)
        self.grid.addWidget(self.wizard, 6, 3, 1, 1)

        # Магазин
        label_31 = QLabel(self)
        label_31.setObjectName("label_31")

        label_117 = QLabel(self)
        label_117.setObjectName("label_17")

        label_119 = QLabel(self)
        label_119.setObjectName("label_19")

        label_116 = QLabel(self)
        label_116.setObjectName("label_16")

        self.potion_agility = QPushButton(self)
        self.potion_agility.setObjectName("self.potion_agility")

        label_118 = QLabel(self)
        label_118.setObjectName("label_18")

        self.berserker = QPushButton(self)
        self.berserker.setObjectName("self.berserker")

        self.stone_skin = QPushButton(self)
        self.stone_skin.setObjectName("self.stone_skin")

        label_211 = QLabel(self)
        label_211.setObjectName("label_21")

        label_210 = QLabel(self)
        label_210.setObjectName("label_20")

        label_312 = QLabel(self)
        label_312.setObjectName("label_32")

        label_313 = QLabel(self)
        label_313.setObjectName("label_33")

        label_314 = QLabel(self)
        label_314.setObjectName("label_34")

        label01 = QLabel(self)
        label01.setObjectName("label")

        label_216 = QLabel(self)
        label_216.setObjectName("label_26")

        label_217 = QLabel(self)
        label_217.setObjectName("label_27")

        label_61 = QLabel(self)
        label_61.setObjectName("label_6")

        label_41 = QLabel(self)
        label_41.setObjectName("label_4")

        label_51 = QLabel(self)
        label_51.setObjectName("label_5")

        label_71 = QLabel(self)
        label_71.setObjectName("label_7")

        self.sword_button = QPushButton(self)
        self.sword_button.setObjectName("self.sword_button")

        label_218 = QLabel(self)
        label_218.setObjectName("label_28")

        label_81 = QLabel(self)
        label_81.setObjectName("label_8")

        label_91 = QLabel(self)
        label_91.setObjectName("label_9")

        self.axe_button = QPushButton(self)
        self.axe_button.setObjectName("self.axe_button")

        self.hammer_button = QPushButton(self)
        self.hammer_button.setObjectName("self.hammer_button")

        label_21 = QLabel(self)
        label_21.setObjectName("label_2")

        label_110 = QLabel(self)
        label_110.setObjectName("label_10")

        label_112 = QLabel(self)
        label_112.setObjectName("label_12")

        label_114 = QLabel(self)
        label_114.setObjectName("label_14")

        label_111 = QLabel(self)
        label_111.setObjectName("label_11")

        label_113 = QLabel(self)
        label_113.setObjectName("label_13")

        label_115 = QLabel(self)
        label_115.setObjectName("label_15")

        label_212 = QLabel(self)
        label_212.setObjectName("label_22")

        label_213 = QLabel(self)
        label_213.setObjectName("label_23")

        label_214 = QLabel(self)
        label_214.setObjectName("label_24")

        self.mail_button = QPushButton(self)
        self.mail_button.setObjectName("self.mail_button")

        self.plate_armor = QPushButton(self)
        self.plate_armor.setObjectName("self.plate_armor")
        
        self.gold_label = QLabel(self)
        self.gold_label.setObjectName("gold_label")        

        self.cuirass = QPushButton(self)
        self.cuirass.setObjectName("self.cuirass")

        pushButton_71 = QPushButton(self)
        pushButton_71.setStyleSheet("background: rgb(34, 168, 19)\n""")
        pushButton_71.setObjectName("pushButton_7")
        pushButton_71.pressed.connect(self.main_open)

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
        label_51.setText(_translate("Form", "Урон: +{}\nЦена: {} золотых".format(self.Items[0].damage,
                                                                                 self.Items[0].get_price())))
        label_61.setText(_translate("Form", "Топор"))
        label_71.setText(_translate("Form", "Урон: +{}\nЦена: {} золотых".format(self.Items[1].damage,
                                                                                 self.Items[1].get_price())))
        label_81.setText("Боевой молот")
        label_91.setText("Урон: +{}\nЦена: {} золотых".format(self.Items[2].damage,
                                                              self.Items[2].get_price()))

        label_117.setText("Зелье\nловкости")
        label_119.setText("Зелье\nберсеркера")
        label_210.setText(_translate("Form", "Зелье\nстальной кожи"))
        label_116.setText(_translate("Form", "Увертливость: +{}\nЦена: {} золотых".format(self.Items[6].points,
                                                                                          self.Items[6].get_price())))
        label_118.setText(_translate("Form", "Атака: +{}\nЦена: {} золотых".format(self.Items[7].points,
                                                                                   self.Items[7].get_price())))
        label_211.setText(_translate("Form", "Защита: +{}\nЦена: {} золотых".format(self.Items[8].points,
                                                                                    self.Items[8].get_price())))

        label_21.setText(_translate("Form", "Броня:"))
        label_110.setText(_translate("Form", "Кираса"))
        label_112.setText(_translate("Form", "Кольчуга"))
        label_114.setText(_translate("Form", "Латы"))
        label_111.setText(_translate("Form", "Защита: +{}\nЦена: {} золотых".format(self.Items[3].protection,
                                                                                    self.Items[3].get_price())))
        label_113.setText("Защита: +{}\nУвертливость: {}\nЦена: {} золотых".format(self.Items[4].protection,
                                                                                   self.Items[4].evasion,
                                                                                   self.Items[4].get_price()))
        label_115.setText("Защита: +{}\nУвертливость: {}\nЦена: {} золотых".format(self.Items[5].protection,
                                                                                   self.Items[5].evasion,
                                                                                   self.Items[5].get_price()))

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
        self.potion_agility.pressed.connect(self.buy_item)
        self.berserker.setText("Купить")
        self.berserker.pressed.connect(self.buy_item)
        self.stone_skin.setText("Купить")
        self.stone_skin.pressed.connect(self.buy_item)

        label_212.setText(_translate("Form", "<html><head/><body><p><img src=\"cuirass.jpg\"/></p></body></html>"))
        label_213.setText(_translate("Form", "<html><head/><body><p><img src=\"chain.jpg\"/></p></body></html>"))
        label_214.setText(_translate("Form", "<html><head/><body><p><img src=\"armor.png\"/></p></body></html>"))

        pushButton_71.setText(_translate("Form", "Назад"))
        self.gold_label.setText('Ваше золото: {}'.format(self.player.money))

        self.shop_list = [label_31, label_117, label_119, label_116, self.potion_agility, label_118,
                          self.berserker, self.stone_skin, label_211, label_210, label_312, label_313,
                          label_314, label01, label_216, label_217, label_61, label_41,
                          label_51, label_71, self.sword_button, label_218, label_81, label_91,
                          self.axe_button, self.hammer_button, label_21, label_110, label_112,
                          label_114, label_111, label_113, label_115, label_212, label_213,
                          label_214, self.mail_button, self.plate_armor, self.cuirass, pushButton_71,
                          self.gold_label]

        self.main_list = [self.label_13, self.damage, self.protection, pushButton, self.evasion_lab,
                          self.hp, label_6, label_5, label_2, label_4, label,
                          label_3, label_7, label_8, self.assasin, self.barbarian, self.orc,
                          self.wizard]
        
        self.grid.addWidget(self.gold_label, 0, 4, 1, 1)
        self.grid.addWidget(pushButton_71, 0, 5, 1, 1)
        self.grid.addWidget(label01, 1, 0, 1, 1)
        
        # ОРУЖИЕ
        self.grid.addWidget(label_216, 3, 0, 1, 1)  # Картинка
        self.grid.addWidget(label_41, 2, 1, 1, 1)  # Название 
        self.grid.addWidget(label_51, 3, 1, 1, 1)  
        self.grid.addWidget(self.sword_button, 3, 2)
        
        self.grid.addWidget(label_217, 5, 0, 1, 1)  # Картинка
        self.grid.addWidget(label_61, 4, 1, 1, 1)  # Название 
        self.grid.addWidget(label_71, 5, 1, 1, 1)  # Бонусы   
        self.grid.addWidget(self.axe_button, 5, 2)
        
        self.grid.addWidget(label_218, 7, 0, 1, 1)  # Картинка
        self.grid.addWidget(label_81, 6, 1, 1, 1)  # Название 
        self.grid.addWidget(label_91, 7, 1, 1, 1)  # Бонусы
        self.grid.addWidget(self.hammer_button, 7, 2)  # Кнопка "Купить"
        
        # БРОНЯ
        self.grid.addWidget(label_21, 1, 3, 1, 1)
        
        self.grid.addWidget(label_212, 3, 3, 1, 1)  # Картинка
        self.grid.addWidget(label_110, 2, 4, 1, 1)  # Название 
        self.grid.addWidget(label_111, 3, 4, 1, 1)  # Бонусы
        self.grid.addWidget(self.cuirass, 3, 5)
        
        self.grid.addWidget(label_213, 5, 3, 1, 1)  # Картинка
        self.grid.addWidget(label_112, 4, 4, 1, 1)  # Название 
        self.grid.addWidget(label_113, 5, 4, 1, 1)  # Бонусы
        self.grid.addWidget(self.mail_button, 5, 5)  # Кнопка "Купить"
        
        self.grid.addWidget(label_214, 7, 3, 1, 1)  # Картинка
        self.grid.addWidget(label_114, 6, 4, 1, 1)  # Название 
        self.grid.addWidget(label_115, 7, 4, 1, 1)  # Бонусы
        self.grid.addWidget(self.plate_armor, 7, 5)  # Кнопка "Купить"
        
        # ЗЕЛЬЯ
        self.grid.addWidget(label_31, 1, 6, 1, 1)
        
        self.grid.addWidget(label_312, 3, 6, 1, 1)  # Картинка
        self.grid.addWidget(label_117, 2, 7, 1, 1)  # Название 
        self.grid.addWidget(label_116, 3, 7, 1, 1)  # Бонусы
        self.grid.addWidget(self.potion_agility, 3, 8)  # Кнопка "Купить"
        
        self.grid.addWidget(label_313, 5, 6, 1, 1)  # Картинка
        self.grid.addWidget(label_119, 4, 7, 1, 1)  # Название 
        self.grid.addWidget(label_118, 5, 7, 1, 1)  # Бонусы
        self.grid.addWidget(self.berserker, 5, 8)  # Кнопка "Купить"
        
        self.grid.addWidget(label_314, 7, 6, 1, 1)  # Картинка
        self.grid.addWidget(label_210, 6, 7, 1, 1)  # Название 
        self.grid.addWidget(label_211, 7, 7, 1, 1)  # Бонусы
        self.grid.addWidget(self.stone_skin, 7, 8)  # Кнопка "Купить"
    
        for i in self.shop_list:
            i.hide()

        self.BUTTONS = {self.Items[0]: self.sword_button,
                        self.Items[1]: self.axe_button,
                        self.Items[2]: self.hammer_button,
                        self.Items[3]: self.cuirass,
                        self.Items[4]: self.mail_button,
                        self.Items[5]: self.plate_armor}

        # Бой

        self.enemy_bar = QProgressBar(self)
        self.enemy_bar.setProperty("value", 100)
        self.enemy_bar.setMinimum(0)
        self.enemy_bar.setObjectName("self.enemy_bar")

        self.enemy_hp = QLabel(self)
        self.enemy_hp.setObjectName("self.enemy_hp")

        self.textBrowsers = QTextBrowser(self)
        self.textBrowsers.setObjectName("textBrowser")

        self.enemy_evasion = QLabel(self)
        self.enemy_evasion.setObjectName("self.enemy_evasion")

        self.enemy_protect = QLabel(self)
        self.enemy_protect.setObjectName("self.enemy_protect")

        self.player_bar = QProgressBar(self)
        self.player_bar.setProperty("value", 90)
        self.player_bar.setMinimum(0)
        self.player_bar.setObjectName("self.player_bar")

        self.player_hp = QLabel(self)
        self.player_hp.setObjectName("self.player_hp")

        self.enemy_damage = QLabel(self)
        self.enemy_damage.setObjectName("self.enemy_damage")

        self.player_protect = QLabel(self)
        self.player_protect.setObjectName("self.player_protect")

        self.player_damage = QLabel(self)
        self.player_damage.setObjectName("self.player_damage")

        self.player_evasion = QLabel(self)
        self.player_evasion.setObjectName("self.player_evasion")

        self.attack_button = QPushButton(self)
        self.attack_button.setObjectName("self.attack_button")

        self.defend_button = QPushButton(self)
        self.defend_button.setObjectName("self.defend_button")

        self.leave = QPushButton(self)
        self.leave.setStyleSheet("background: rgb(34, 168, 19)\n")
        self.leave.setObjectName("pushButton_7")
        self.leave.pressed.connect(self.main_open)
        self.leave.pressed.connect(self.escape)

        label_16s = QLabel(self)
        label_16s.setObjectName("label_16")

        self.enemy_name = QLabel(self)
        self.enemy_name.setObjectName("self.enemy_name")

        # Характеристики врага
        self.enemy_hp.setText(_translate("Form", "Здоровье: {}"))  # label_2s
        self.enemy_damage.setText(_translate("Form", "Урон: {}"))  # label_13s
        self.enemy_protect.setText(_translate("Form", "Защита: {}"))  # label_5s
        self.enemy_evasion.setText(_translate("Form", "Увертливость: {}"))  # label_4s

        # Характеристики игрока
        self.player_hp.setText(_translate("Form", "Здоровье: {}"))  # label_7s
        self.player_protect.setText(_translate("Form", "Защита: {}"))  # label_8s
        self.player_damage.setText(_translate("Form", "Урон: {}"))  # label_14
        self.player_evasion.setText(_translate("Form", "Увертливость: {}"))  # label_11

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

        self.fight_list = [self.enemy_hp, self.enemy_evasion, self.enemy_protect,
                           self.textBrowsers, self.player_hp, self.player_protect,
                           self.player_evasion, self.enemy_damage,
                           self.player_damage, self.player_bar, self.enemy_bar,
                           self.defend_button, self.attack_button, self.leave,
                           self.enemy_name, label_16s]
        
        self.grid.addWidget(self.enemy_name, 0, 0, 1, 1)
        self.grid.addWidget(self.enemy_bar, 2, 0, 1, 1)
        self.grid.addWidget(self.enemy_hp, 1, 0, 1, 1)
        self.grid.addWidget(self.enemy_damage, 3, 0, 1, 1)
        self.grid.addWidget(self.enemy_protect, 4, 0, 1, 1)
        self.grid.addWidget(self.enemy_evasion, 5, 0, 1, 1)
        self.grid.addWidget(self.leave, 0, 2, 1, 1)
        self.grid.addWidget(self.textBrowsers, 1, 1, 5, 3)
        self.grid.addWidget(label_16s, 0, 4, 1, 1)
        self.grid.addWidget(self.defend_button, 6, 3, 1, 1)
        self.grid.addWidget(self.attack_button, 6, 1, 1, 1)
        self.grid.addWidget(self.player_hp, 1, 4, 1, 1)
        self.grid.addWidget(self.player_bar, 2, 4, 1, 1)
        self.grid.addWidget(self.player_damage, 3, 4, 1, 1)
        self.grid.addWidget(self.player_protect, 4, 4, 1, 1)
        self.grid.addWidget(self.player_evasion, 5, 4, 1, 1)

        for i in self.fight_list:
            i.hide()
            
        self.setLayout(self.grid)

    # ФУНКЦИЯ ПОКУПКИ ПРЕДМЕТА
    def buy_item(self):
        a = self.sender().objectName().split('.')[1]  # Вытаскиваем название кнопки
        item = self.ITEMS[a]
        if self.player.money >= item.get_price():
            
            if not item.i_type == 'potion':
                self.sender().setText('Надеть')
            
            else:
                self.sender().setText('Выпить')            

            self.sender().disconnect()
            self.sender().pressed.connect(self.equip)
            self.player.money -= item.get_price()
            self.gold_label.setText('Ваше золото: {}'.format(self.player.money))

    def shop_open(self):
        self.player.set_win(self.Person_Main)
        self.gold_label.setText('Ваше золото: {}'.format(self.player.money))
        for i in self.main_list:
            i.hide()
        for i in self.shop_list:
            i.show()
        self.setWindowTitle("Магазин")

    def fight_open(self):  # НАЧАЛО БОЯ
        
        self.player.set_win(self.player_fight)
        self.player.print_info()
        self.turn = 'player'
        self.action_points = 2
        
        for i in self.main_list:
            i.hide()        
        for i in self.fight_list:
            i.show()
    
        a = self.sender().objectName().split('.')[1]  # Вытаскиваем название кнопки
        self.rival = self.RIVALS[a]  # Достаем соперника из списка боссов
        self.rival.set_win(self.enemy_fight)  # Устанавливаем для врага список элементов-надписей, которые он будет изменять
        self.rival.print_info()  # Выводим информацию о характеристиках врагов
        self.rival.set_rival(self.player)  # Устанавливаем врагу в качестве соперника игрока
        self.player.set_rival(self.rival)  # Добавляем герою врага (чтобы было кого бить)
        self.enemy_name.setText(self.rival.name)  # Имя врага
        
        self.enemy_bar.setMaximum(self.rival.health)
        self.enemy_bar.setValue(self.rival.health)
        
        self.player_bar.setMaximum(self.player.health)
        self.player_bar.setValue(self.player.health)

        self.textBrowsers.append('''{} готов к сражению.
Бой начался\nВаш ход первый.\n'''.format(self.rival.name))
        
        self.setWindowTitle("Бой")
        
    def attack(self):
        if self.turn == 'player':
            self.action_points -= 1
            self.textBrowsers.append(self.player.attack())
            self.textBrowsers.append('Ваши очки действия: {}\n'.format(self.action_points))
            self.enemy_bar.setValue(self.rival.health)
            self.player.print_info()
            self.rival.print_info()
            if self.rival.health == 0:
                self.textBrowsers.append(self.rival.defeated())
                self.textBrowsers.append('Вы выиграли бой!')
                self.player.money += self.rival.money
                self.attack_button.hide()
                self.defend_button.hide()
            else:
                if self.action_points < 1:
                    self.action_points = 2
                    self.turn = 'enemy'
                    self.rival.end_defend()
                    self.enemy_turn()
            
    def defend(self):
        if self.turn == 'player':
            self.textBrowsers.append(self.player.defend())
            self.textBrowsers.append('Ваши очки действия: {}\n'.format(0))
            self.player.print_info()
            self.action_points = 2
            self.turn = 'enemy'
            self.rival.end_defend()
            self.enemy_turn()
            
    def enemy_turn(self):
        self.action_points -= 1
        self.textBrowsers.append(self.rival.attack())
        self.textBrowsers.append('Очки действий вашего соперника: {}\n'.format(self.action_points))
        self.player_bar.setValue(self.player.health)
        self.player.print_info()
        if self.player.health == 0:
            self.textBrowsers.append(self.player.defeated())
            self.textBrowsers.append('Вы проиграли бой.')
            self.attack_button.hide()
            self.defend_button.hide()
        else:
            if self.action_points < 1:
                self.action_points = 2
                self.turn = 'player'
                self.player.end_defend()                
            else:
                self.enemy_turn()
                
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
                
        elif item.i_type == 'potion':
            self.player.drink(item)    
            self.sender().disconnect()
            self.sender().pressed.connect(self.buy_item)
            self.sender().setText('Купить')

    def main_open(self): 
        self.player.set_win(self.Person_Main)
        self.player.print_info()
        self.resize(500, 500)
        for i in self.shop_list:
            i.hide()
        for i in self.fight_list:
            i.hide()
        for i in self.main_list:
            i.show()            

    def get_player(self):  # Функция, возвращающая игрока, чтобы изменять его данные
        return self.player


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UiMainWindow(Person('Гюнтер', 100, 0, 0, 10, 50))
    window.get_player().set_win(window)
    window.show()
    sys.exit(app.exec())