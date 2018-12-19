#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Файл с механикой персонажей, здесь задаются их параметры и 
# функции взаимодействия с окном
# В будущем это будет лишь фрагментом общей программы


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
    
    def __init__(self, name):  # конструктор
        
        self.name = name  # имя перса
        self.health = 100  # дефолтное здоровье
        self.protection = 0  # дефолтная броня
        self.damage = 0  # дефолтный урон (кулаками)
        self.real_evasion = 10  # считаемый уворот
        self.evasion = 10  # выводимый уворот
        self.equip_armor = Armor('', 0, 0) # дефолтная броня, надетая на перса
        self.equip_weapon = Weapon('Кулаки', 0)  # дефолтное оружие, надетое на перса
        
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
        else:
            self.evasion = self.real_evasion
            # Уклонение для расчета в бою будет браться из self.evasion
            # self.real_evasion нужен только для случаев, когда штраф брони больше уклонения игрока
        
    def set_new_weapon(self, new_weap):  # функция по одеванию нового оружия
        
        if self.equip_weapon != '':  # Если есть какое-то другое оружие в руках, то
            self.unset_weapon(self.equip_weapon)  # снимаем старое оружие
        self.equip_weapon = new_weap  # устанавливаем новое оружие
        self.damage += new_weap.damage  # добавляем урон оружия
        
    def print_info(self):  # функция, выводящая всю инфу по персонажу
        # АХТУНГ!!
        # ФУНКЦИЯ ТРЕБУЕТ ДОРАБОТКИ: РЕТЁРНИТЬ МАССИВ ДАННЫХ ДЛЯ ОБРАБОТКИ ОКНОМ
        # АХТУНГ!!
        return '''{}\nЗдоровье: {}\nЗащита: {}\nУклонение: {}
Броня: {}\nУрон: {}\nОружие: {}'''.format(self.name, self.health, self.protection,
                                          self.evasion, self.equip_armor.name,
                                          self.damage, self.equip_weapon.name)
 
 
hero = Person('Гюнтер')
hero.set_new_armor(Armor('Латы', 100, -100))
hero.set_new_armor(Armor('Кольчуга', 70, -50))
hero.set_new_weapon(Weapon('Меч', 20))
print(hero.print_info())

        