#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Файл с механикой персонажей, здесь задаются их параметры и 
# функции взаимодействия с окном
# В будущем это будет лишь фрагментом общей программы
import random
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Armor():  # класс брони
    
    def __init__(self, name, protection, evasion):  # конструктор
        
        self.name = name  # название
        self.protection = protection  # Защита этой броней
        self.evasion = evasion  # Штраф/бонус к уклонению
    
    def name(self):  # функция, возвращающая название предмета
        
        return self.name
        
        
class Weapon():  # класс оружия
    
    def __init__(self, name, damage):  # конструктор
        
        self.name = name  # название
        self.damage = damage  # Урон этого оружия
        
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
        self.equip_armor = Armor('', 0, 0) # дефолтная броня, надетая на перса
        self.equip_weapon = Weapon('Кулаки', 0)  # дефолтное оружие, надетое на перса
        self.rival = ''  # Соперник
        
    def unset_armor(self, armor):  # Функция по сниманию брони
        self.equip_armor = ''  # Удаляем броню
        self.protection -= armor.protection  # Удаляем защиту брони
        self.real_evasion -= armor.evasion  # Удаляем штраф/бонус к уклонению от брони
        self.evasion = self.real_evasion
        
    def unset_weapon(self, weapon):  # Функция по сниманию оружия
        self.equip_weapon = ''  # Удаляем броню
        self.damage -= weapon.damage  # Удаляем защиту брони
        
    def set_new_armor(self, new_arm):  # функция по одеванию новой броньки на персонажа
        
        if self.equip_armor != '':  # Если есть какая-то другая броня, то
            self.unset_armor(self.equip_armor)  # снимаем старую броню
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
        
    def set_new_weapon(self, new_weap):  # функция по одеванию нового оружия
        
        if self.equip_weapon != '':  # Если есть какое-то другое оружие в руках, то
            self.unset_weapon(self.equip_weapon)  # снимаем старое оружие
        self.equip_weapon = new_weap  # устанавливаем новое оружие
        self.damage = new_weap.damage  # добавляем урон оружия
        
    def set_rival(self, rival):  # функция по добавлению соперника
        
        self.rival = rival
        
    def print_info(self):  # функция, выводящая всю инфу по персонажу
        # АХТУНГ!!
        # ФУНКЦИЯ ТРЕБУЕТ ДОРАБОТКИ: РЕТЁРНИТЬ МАССИВ ДАННЫХ ДЛЯ ОБРАБОТКИ ОКНОМ
        # АХТУНГ!!
        return '''{}\nЗдоровье: {}\nЗащита: {}\nУклонение: {}
Броня: {}\nУрон: {}\nОружие: {}'''.format(self.name, self.health, self.protection,
                                          self.evasion, self.equip_armor.name,
                                          self.damage, self.equip_weapon.name)
    
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
            
            
class Ui_MainWindow(QWidget):  # GUI

    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(1041, 725)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 1021, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)  # Создание кнопки магазина
        self.pushButton.setStyleSheet("background: rgb(34, 168, 19)\n"  # Изменение цвета кнопки магазина
                                      "")
        self.pushButton.setObjectName("pushButton")  # Название кнопки магазина
        self.verticalLayout.addWidget(self.pushButton)  # Добавление кнопки магазин в верхний элемент лэйаута
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)  # Кнопка "В бой" для орка
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)  # Кнопка "В бой" для мага
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)  # Кнопка "В бой" для варвара
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)  # Кнопка "В бой" для ловкача
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 26))
        self.menubar.setObjectName("menubar")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Магазин"))
        self.pushButton_4.setText(_translate("MainWindow", "В бой"))
        self.pushButton_5.setText(_translate("MainWindow", "В бой"))
        self.label_3.setText(_translate("MainWindow", "Варвар\nЕщё более крутой чувак"))
        self.label_8.setText(_translate("MainWindow", "Маг\nАА Какой чувак"))
        self.label.setText(_translate("MainWindow", "Ловкач\nКрутой чувак"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                      "<img src=\"ork.png\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                      "<img src=\"barbarian.jpg\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                      "<img src=\"mag.jpg\"/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Орк\nПрям мега крутой чувак"))
        self.pushButton_3.setText(_translate("MainWindow", "В бой"))
        self.pushButton_2.setText(_translate("MainWindow", "В бой"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                      "<img src=\"magomed.png\"/></p></body></html>"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
                                                                                                         
 
 
hero = Person('Гюнтер', 100, 0, 0, 10)
hero.set_new_armor(Armor('Латы', 100, -100))
hero.set_new_armor(Armor('Кольчуга', 70, -50))
hero.set_new_weapon(Weapon('Меч', 20))
print(hero.print_info())

        