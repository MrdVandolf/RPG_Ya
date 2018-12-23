#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Файл с механикой персонажей, здесь задаются их параметры и 
# функции взаимодействия с окном
# В будущем это будет лишь фрагментом общей программы
import random
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)


class Potion():  # зелье
    
    def __init__(self, parameter, points, price):
        self.parameter = parameter
        self.points = points
        self.price = price

class Armor():  # класс брони
    
    def __init__(self, name, protection, evasion, price):  # конструктор
        self.name = name  # название
        self.protection = protection  # Защита этой броней
        self.evasion = evasion  # Штраф/бонус к уклонению
        self.itype = 'armor'
        self.price = price  # цена предмета
    
    def name(self):  # функция, возвращающая название предмета
        return self.name
        
class Weapon():  # класс оружия
    
    def __init__(self, name, damage, price):  # конструктор
        self.name = name  # название
        self.damage = damage  # Урон этого оружия
        self.itype = 'weapon'
        self.price = price  # цена
        
    def name(self):  # функция, возвращающая название предмета
        return self.name    


class Person():  # класс персонажа
    
    # В конструкторе задаются начальное здоровье, защита, урон без оружия и уклонение
    def __init__(self, name, health, protection, damage, evasion):  # конструктор
        
        # Изменяемые в бою переменные, которые используются в расчетах при обороне/ударе
        self.out_protec = protection  # Защита (при обороне увеличивается)
        self.out_evas = evasion  # Уклонение (при обороне увеличивается)
        
        # Постоянные (или полупостоянные) переменные, которые служат основой характерист персонажа
        self.name = name  # имя перса
        self.health = health  # дефолтное здоровье
        self.protection = protection  # дефолтная броня
        self.damage = damage  # дефолтный урон (кулаками)
        self.real_evasion = 10  # считаемый уворот
        self.evasion = evasion  # выводимый уворот
        self.equip_armor = Armor('', 0, 0, 0) # дефолтная броня, надетая на перса
        self.equip_weapon = Weapon('Кулаки', 3, 0)  # дефолтное оружие, надетое на перса
        self.rival = ''  # Соперник
        self.win = ''  # Класс, в котором выводится вся инфа персонажа
        self.money = 130  # Золото игрока
        
    def set_win(self, win):  # Функция, в которой устанавливается класс, для вывода в нем инфы персонажа
        self.win = win
        
    def unset_armor(self):  # Функция по сниманию брони
        self.protection -= self.equip_armor.protection  # Удаляем защиту брони
        self.real_evasion -= self.equip_armor.evasion  # Удаляем штраф/бонус к уклонению от брони
        self.evasion = self.real_evasion
        self.equip_armor = ''  # Удаляем броню
        if self.win != '':
            self.print_info()  # Обновляем информацию в окне
        
    def unset_weapon(self):  # Функция по сниманию оружия
        self.damage -= self.equip_weapon.damage  # Удаляем атаку старого оружия
        self.equip_weapon = ''  # Удаляем броню
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
        elif self.real_evasion > 90: # предотвращено максимальное уклонение (иначе это имба
            self.evasion = 100
        else:
            self.evasion = self.real_evasion
            # Уклонение для расчета в бою будет браться из self.evasion
            # self.real_evasion нужен только для случаев, когда штраф брони больше уклонения игрока
        if self.win != '':
            self.print_info()  # Обновляем информацию в окне
        
    def set_new_weapon(self, new_weap):  # функция по одеванию нового оружия
        if self.equip_weapon != '':  # Если есть какое-то другое оружие в руках, то
            self.unset_weapon()  # снимаем старое оружие
        self.equip_weapon = new_weap  # устанавливаем новое оружие
        self.damage = new_weap.damage  # добавляем урон оружия
        if self.win != '':
            self.print_info()  # Обновляем информацию в окне
        
    def set_rival(self, rival):  # функция по добавлению соперника
        self.rival = rival
        
    def print_info(self):  # функция, выводящая всю инфу по персонажу
        self.win.hp.setText('Здоровье: {}'.format(self.health))
        self.win.damage.setText('Урон: {}'.format(self.damage))
        self.win.protection.setText('Защита: {}'.format(self.protection))
        self.win.evasion_lab.setText('Увертливость: {}'.format(self.evasion))
    
    def defend(self):  # функция обороны
        
        self.out_protec = self.protection * 1.5  # увеличиваем в полтора раза выдаваемую защиту
        self.out_evas = self.evasion * 1.2  # увеличиваем в 1.2 раза выдаваемое уклонение
        return '{} встал в защитную стойку.\nЕго защита увеличена в 1.5 раза, уклонение в 1.2 раза'.format(self.name)
                
    def attack(self):  # функция атаки
    
        self.rival.damage(self.attack)  # наносим сопернику урон
        return '{} атаковал соперника.'.format(self.name)
    
    def damage(self, attack):  # функция получения урона
        
        the_ans = 'Шанс попадания {}\n'.format(100 - self.out_evas)  # выводимое в лог сообщение
        chance_to_evade = randint(1, 100)  # число, шанс попадания
        if chance_to_evade > self.out_evas: # если шанс попадания не больше уклонения (т.е. выпало случайное число на кубике)
            critism_of_damage = randint(7, 10) / 10  # коэффициент уменьшения брони
            damage = attack - (self.out_protec * critism_of_damage)  # формула, высчитывающая нанесенный урон
            self.health -=  damage  # формула по вычету здоровья
            # Обновляем сообщение для лога
            the_ans += '''Выпало случайное число {} > {} (1-100) \n
Нанесено урона - {} ({} - ({} * {}))'''.format(chance_to_evade, self.out_evas, damage,
                                               attack, self.out_protec, critism_of_damage)
        # если шанс попадания входит в диапазон [0, out_evas] (Промах)
        else:
            the_ans += '''Выпало случайное число {} <= {} (1-100)\n
Промах'''.format(chance_to_evade, self.out_evas)
            
            
class UiMainWindow(QWidget):

    def __init__(self, hero):
        super().__init__()
        
        self.Items = [Weapon('Меч', 20, 40), Weapon('Боевой топор', 40, 80),
                 Weapon('Боевой молот', 70, 140), Armor('Кираса', 30, 0, 45),
                 Armor('Кольчуга', 60, -30, 90), Armor('Латы', 100, -50, 180)]
                 
        self.ITEMS = {'sword_button': self.Items[0],
                      'axe_button': self.Items[1],
                      'hammer_button': self.Items[2],
                      'cuirass': self.Items[3],
                      'mail_button': self.Items[4],
                      'plate_armor': self.Items[5]}
        
        self.player = hero  # Задаем героя    
        self.setObjectName("RPG game")
        self.shop_list = []
        self.main_list = []
        self.setMinimumSize(QtCore.QSize(971, 716))
        self.setMaximumSize(QtCore.QSize(971, 716))        
        self.main_create()

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
        label.setGeometry(QtCore.QRect(10, 490, 131, 131))
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
        pushButton_3 = QPushButton(centralwidget)
        pushButton_3.setGeometry(QtCore.QRect(10, 630, 231, 41))
        pushButton_3.setObjectName("pushButton_3")
        pushButton_4 = QPushButton(centralwidget)
        pushButton_4.setGeometry(QtCore.QRect(250, 630, 231, 41))
        pushButton_4.setObjectName("pushButton_4")
        pushButton_5 = QPushButton(centralwidget)
        pushButton_5.setGeometry(QtCore.QRect(490, 630, 231, 41))
        pushButton_5.setObjectName("pushButton_5")
        pushButton_6 = QPushButton(centralwidget)
        pushButton_6.setGeometry(QtCore.QRect(730, 630, 231, 41))
        pushButton_6.setObjectName("pushButton_6")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_13.setText(_translate("MainWindow", "Ваши характеристики:"))
        pushButton.setText(_translate("MainWindow", "Магазин"))
        
        self.damage.setText("Атака: {}".format(self.player.damage))  # label_10
        self.protection.setText("Защита: {}".format(self.player.protection))  # lab 11
        self.evasion_lab.setText("Увертливость: {}".format(self.player.evasion))  # lab 12
        self.hp.setText("Здоровье: {}".format(self.player.health))
        
        label_6.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                 "<img src=\"barbarian1.jpg\"/></p></body></html>"))
        label_5.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                 "<img src=\"magomed.png\"/></p></body></html>"))
        label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"ork.png\"/></p></body></html>"))
        label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"mag.jpg\"/></p></body></html>"))
        label.setText(_translate("MainWindow", "Ловкач\n"
                                               "Крутой ловкий чувак\n"
                                               "\n"
                                               "Характкристики:\n"
                                               "Здоровье : 200\n"
                                               "Атака: 50\n"
                                               "Защита: 10\n"
                                               "Увертливость: 100"))
        label_3.setText(_translate("MainWindow", "Варвар\n"
                                                 "Ещё более крутой чувак\n"
                                                 "\n"
                                                 "Характкристики:\n"
                                                 "Здоровье : 500\n"
                                                 "Атака: 70\n"
                                                 "Защита: 50\n"
                                                 "Увертливость: 30"))
        label_7.setText(_translate("MainWindow", "Орк\n"
                                                 "Прям мега крутой чувак\n"
                                                 "\n"
                                                 "Характкристики:\n"
                                                 "Здоровье : 750\n"
                                                 "Атака: 120\n"
                                                 "Защита: 50\n"
                                                 "Увертливость: 20"))
        label_8.setText(_translate("MainWindow", "Маг\n"
                                                 "АА Какой чувак\n"
                                                 "\n"
                                                 "Характкристики:\n"
                                                 "Здоровье : 1200\n"
                                                 "Атака: 250\n"
                                                 "Защита: 100\n"
                                                 "Увертливость: 50"))
        pushButton_3.setText(_translate("MainWindow", "В бой"))
        pushButton_4.setText(_translate("MainWindow", "В бой"))
        pushButton_5.setText(_translate("MainWindow", "В бой"))
        pushButton_6.setText(_translate("MainWindow", "В бой"))

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
        #self.potion_agility.pressed.connect(self.buy_item)
        self.berserker.setText("Купить")
        #self.berserker.pressed.connect(self.buy_item)
        self.stone_skin.setText("Купить")
        #self.stone_skin.pressed.connect(self.buy_item)
        
        
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
                          label_214, self.mail_button, self.plate_armor, self.cuirass, pushButton_71]

        # self.setLayout(self.grid)
        self.main_list = [self.label_13, self.damage, self.protection, pushButton, self.evasion_lab,
                          self.hp, label_6, label_5, label_2, label_4, label,
                          label_3, label_7, label_8, pushButton_3, pushButton_4, pushButton_5,
                          pushButton_6]
        for i in self.shop_list:
            i.hide()
            
        self.BUTTONS = {self.Items[0]: self.sword_button,
                        self.Items[1]: self.axe_button,
                        self.Items[2]: self.hammer_button,
                        self.Items[3]: self.cuirass,
                        self.Items[4]: self.mail_button,
                        self.Items[5]: self.plate_armor}
            
    def buy_item(self):
        self.sender().setText('Надеть')
        self.sender().disconnect()
        self.sender().pressed.connect(self.equip)
        
    def shop_open(self):
        for i in self.main_list:
            i.hide()
        for i in self.shop_list:
            i.show()
        self.setWindowTitle("Магазин")
        
    def equip(self):
        a = self.sender().objectName().split('.')[1]  # Вытаскиваем название кнопки
        item = self.ITEMS[a]  # объект одеваемого предмета
        
        if item.itype == 'weapon':
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
            
        elif item.itype == 'armor':
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
        for i in self.main_list:
            i.show()
        for i in self.shop_list:
            i.hide()
        
    def get_player(self):  # Функция, возвращающая игрока, чтобы изменять его данные
        return self.player


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UiMainWindow(Person('Гюнтер', 100, 0, 0, 10))
    window.get_player().set_win(window)
    window.show()
    sys.exit(app.exec())
                                                                                                         
 
 
'''hero.set_new_armor(Armor('Латы', 100, -100))
hero.set_new_armor(Armor('Кольчуга', 70, -50))
hero.set_new_weapon(Weapon('Меч', 20))
'''

        