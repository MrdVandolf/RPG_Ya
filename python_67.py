from PyQt5 import QtCore
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton,
                             QHBoxLayout)


class UiMainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("RPG game")
        self.shop_list = []
        self.main_list = []
        self.main_create()

    def main_create(self):
        for i in self.shop_list:
            i.hide()
        for j in self.main_list:
            j.show()
        self.resize(971, 716)
        centralwidget = QWidget(self)
        centralwidget.setObjectName("centralwidget")
        label_13 = QLabel(centralwidget)
        label_13.setGeometry(QtCore.QRect(10, 50, 141, 31))
        label_13.setObjectName("label_13")
        label_10 = QLabel(centralwidget)
        label_10.setGeometry(QtCore.QRect(170, 40, 141, 21))
        label_10.setObjectName("label_10")
        label_11 = QLabel(centralwidget)
        label_11.setGeometry(QtCore.QRect(170, 100, 141, 21))
        label_11.setObjectName("label_11")
        pushButton = QPushButton(centralwidget)
        pushButton.setGeometry(QtCore.QRect(780, 10, 181, 71))
        pushButton.setStyleSheet("background: rgb(34, 168, 19)\n"
                                 "")
        pushButton.setObjectName("pushButton")
        pushButton.pressed.connect(self.shop_create)
        label_12 = QLabel(centralwidget)
        label_12.setGeometry(QtCore.QRect(170, 70, 141, 21))
        label_12.setObjectName("label_12")
        label_9 = QLabel(centralwidget)
        label_9.setGeometry(QtCore.QRect(170, 10, 141, 21))
        label_9.setObjectName("label_9")
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
        label_13.setText(_translate("MainWindow", "Ваши характеристики:"))
        label_10.setText(_translate("MainWindow", "Атака: 30"))
        label_11.setText(_translate("MainWindow", "Защита: 40"))
        pushButton.setText(_translate("MainWindow", "Магазин"))
        label_12.setText(_translate("MainWindow", "Увертливость: 10"))
        label_9.setText(_translate("MainWindow", "Здоровье: 100"))
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
        self.main_list = [label_13, label_10, label_11, pushButton, label_12, label_9, label_6, label_5,
                          label_2, label_4, label, label_3, label_7, label_8, pushButton_3, pushButton_4,
                          pushButton_5, pushButton_6]

    def shop_create(self):
        for i in self.main_list:
            i.hide()
        self.resize(902, 450)
        label_3 = QLabel(self)
        label_3.setGeometry(QtCore.QRect(620, 70, 62, 16))
        label_3.setObjectName("label_3")
        label_17 = QLabel(self)
        label_17.setGeometry(QtCore.QRect(700, 120, 61, 28))
        label_17.setObjectName("label_17")
        label_19 = QLabel(self)
        label_19.setGeometry(QtCore.QRect(700, 210, 71, 28))
        label_19.setObjectName("label_19")
        label_16 = QLabel(self)
        label_16.setGeometry(QtCore.QRect(700, 165, 111, 31))
        label_16.setObjectName("label_16")
        pushButton_12 = QPushButton(self)
        pushButton_12.setGeometry(QtCore.QRect(830, 110, 61, 91))
        pushButton_12.setObjectName("pushButton_12")
        label_18 = QLabel(self)
        label_18.setGeometry(QtCore.QRect(700, 267, 71, 31))
        label_18.setObjectName("label_18")
        pushButton_11 = QPushButton(self)
        pushButton_11.setGeometry(QtCore.QRect(830, 210, 61, 91))
        pushButton_11.setObjectName("pushButton_11")
        pushButton_10 = QPushButton(self)
        pushButton_10.setGeometry(QtCore.QRect(830, 310, 61, 91))
        pushButton_10.setObjectName("pushButton_10")
        label_21 = QLabel(self)
        label_21.setGeometry(QtCore.QRect(700, 370, 111, 31))
        label_21.setObjectName("label_21")
        label_20 = QLabel(self)
        label_20.setGeometry(QtCore.QRect(700, 310, 91, 41))
        label_20.setObjectName("label_20")
        label_32 = QLabel(self)
        label_32.setGeometry(QtCore.QRect(620, 110, 61, 91))
        label_32.setObjectName("label_32")
        label_33 = QLabel(self)
        label_33.setGeometry(QtCore.QRect(620, 210, 61, 91))
        label_33.setObjectName("label_33")
        label_34 = QLabel(self)
        label_34.setGeometry(QtCore.QRect(620, 310, 61, 91))
        label_34.setObjectName("label_34")
        label = QLabel(self)
        label.setGeometry(QtCore.QRect(10, 70, 61, 16))
        label.setObjectName("label")
        label_26 = QLabel(self)
        label_26.setGeometry(QtCore.QRect(10, 110, 61, 91))
        label_26.setObjectName("label_26")
        label_27 = QLabel(self)
        label_27.setGeometry(QtCore.QRect(10, 210, 61, 91))
        label_27.setObjectName("label_27")
        label_6 = QLabel(self)
        label_6.setGeometry(QtCore.QRect(90, 220, 41, 16))
        label_6.setObjectName("label_6")
        label_4 = QLabel(self)
        label_4.setGeometry(QtCore.QRect(90, 110, 48, 16))
        label_4.setObjectName("label_4")
        label_5 = QLabel(self)
        label_5.setGeometry(QtCore.QRect(90, 180, 71, 21))
        label_5.setObjectName("label_5")
        label_7 = QLabel(self)
        label_7.setGeometry(QtCore.QRect(90, 260, 108, 32))
        label_7.setObjectName("label_7")
        pushButton = QPushButton(self)
        pushButton.setGeometry(QtCore.QRect(210, 110, 61, 91))
        pushButton.setObjectName("pushButton")
        label_28 = QLabel(self)
        label_28.setGeometry(QtCore.QRect(10, 320, 61, 91))
        label_28.setObjectName("label_28")
        label_8 = QLabel(self)
        label_8.setGeometry(QtCore.QRect(90, 320, 61, 31))
        label_8.setObjectName("label_8")
        label_9 = QLabel(self)
        label_9.setGeometry(QtCore.QRect(90, 370, 121, 31))
        label_9.setObjectName("label_9")
        pushButton_3 = QPushButton(self)
        pushButton_3.setGeometry(QtCore.QRect(210, 210, 61, 91))
        pushButton_3.setObjectName("pushButton_3")
        pushButton_4 = QPushButton(self)
        pushButton_4.setGeometry(QtCore.QRect(210, 320, 61, 91))
        pushButton_4.setObjectName("pushButton_4")
        label_2 = QLabel(self)
        label_2.setGeometry(QtCore.QRect(360, 70, 83, 16))
        label_2.setObjectName("label_2")
        label_10 = QLabel(self)
        label_10.setGeometry(QtCore.QRect(400, 110, 41, 16))
        label_10.setObjectName("label_10")
        label_12 = QLabel(self)
        label_12.setGeometry(QtCore.QRect(400, 220, 61, 16))
        label_12.setObjectName("label_12")
        label_14 = QLabel(self)
        label_14.setGeometry(QtCore.QRect(390, 332, 124, 20))
        label_14.setObjectName("label_14")
        label_11 = QLabel(self)
        label_11.setGeometry(QtCore.QRect(400, 180, 81, 21))
        label_11.setObjectName("label_11")
        label_13 = QLabel(self)
        label_13.setGeometry(QtCore.QRect(400, 270, 111, 32))
        label_13.setObjectName("label_13")
        label_15 = QLabel(self)
        label_15.setGeometry(QtCore.QRect(390, 371, 111, 31))
        label_15.setObjectName("label_15")
        label_22 = QLabel(self)
        label_22.setGeometry(QtCore.QRect(310, 110, 71, 91))
        label_22.setObjectName("label_22")
        label_23 = QLabel(self)
        label_23.setGeometry(QtCore.QRect(310, 210, 71, 91))
        label_23.setObjectName("label_23")
        label_24 = QLabel(self)
        label_24.setGeometry(QtCore.QRect(310, 320, 61, 81))
        label_24.setObjectName("label_24")
        pushButton_2 = QPushButton(self)
        pushButton_2.setGeometry(QtCore.QRect(520, 210, 61, 91))
        pushButton_2.setObjectName("pushButton_2")
        pushButton_5 = QPushButton(self)
        pushButton_5.setGeometry(QtCore.QRect(520, 310, 61, 91))
        pushButton_5.setObjectName("pushButton_5")
        pushButton_6 = QPushButton(self)
        pushButton_6.setGeometry(QtCore.QRect(520, 110, 61, 91))
        pushButton_6.setObjectName("pushButton_6")
        pushButton_7 = QPushButton(self)
        pushButton_7.setGeometry(QtCore.QRect(355, 10, 211, 31))
        pushButton_7.setStyleSheet("background: rgb(34, 168, 19)\n"
                                   "")
        pushButton_7.setObjectName("pushButton_7")
        pushButton_7.pressed.connect(self.main_create)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        label_3.setText(_translate("Form", "Зелья:"))
        label_17.setText(_translate("Form", "Зелье\n"
                                            "ловкости"))
        label_19.setText(_translate("Form", "Зелье\n"
                                            "берсеркера"))
        label_16.setText(_translate("Form", "увертливость: +30"))
        pushButton_12.setText(_translate("Form", "Купить"))
        label_18.setText(_translate("Form", "атака: +30"))
        pushButton_11.setText(_translate("Form", "Купить"))
        pushButton_10.setText(_translate("Form", "Купить"))
        label_21.setText(_translate("Form", "защита: +30"))
        label_20.setText(_translate("Form", "Зелье\n"
                                            "стальной кожи"))
        label_32.setText(_translate("Form", "<html><head/><body><p><img src=\"lovkost.png\"/></p></body></html>"))
        label_33.setText(_translate("Form", "<html><head/><body><p><img src=\"berserk.png\"/></p></body></html>"))
        label_34.setText(_translate("Form", "<html><head/><body><p><img src=\"poition1.jpg\"/></p></body></html>"))
        label.setText(_translate("Form", "Оружие:"))
        label_26.setText(_translate("Form", "<html><head/><body><p><img src=\"sword.png\"/></p></body></html>"))
        label_27.setText(_translate("Form", "<html><head/><body><p><img src=\"axe.jpg\"/></p></body></html>"))
        label_6.setText(_translate("Form", "Топор"))
        label_4.setText(_translate("Form", "Меч"))
        label_5.setText(_translate("Form", "урон: +20"))
        label_7.setText(_translate("Form", "урон: +40\n"
                                           "увертливость: -10"))
        pushButton.setText(_translate("Form", "Купить"))
        label_28.setText(_translate("Form", "<html><head/><body><p><img src=\"hammer.jpg\"/></p></body></html>"))
        label_8.setText(_translate("Form", "Боевой\n"
                                           "молот"))
        label_9.setText(_translate("Form", "урон: +70\n"
                                           "увертливость: -40"))
        pushButton_3.setText(_translate("Form", "Купить"))
        pushButton_4.setText(_translate("Form", "Купить"))
        label_2.setText(_translate("Form", "Броня:"))
        label_10.setText(_translate("Form", "Кираса"))
        label_12.setText(_translate("Form", "Кольчуга"))
        label_14.setText(_translate("Form", "Латы"))
        label_11.setText(_translate("Form", "защита: +30"))
        label_13.setText(_translate("Form", "защита: +60\n"
                                            "увертливость: -20"))
        label_15.setText(_translate("Form", "защита: +100\n"
                                            "увертливость: -50"))
        label_22.setText(_translate("Form", "<html><head/><body><p><img src=\"cuirass.jpg\"/></p></body></html>"))
        label_23.setText(_translate("Form", "<html><head/><body><p><img src=\"chain.jpg\"/></p></body></html>"))
        label_24.setText(_translate("Form", "<html><head/><body><p><img src=\"armor.png\"/></p></body></html>"))
        pushButton_2.setText(_translate("Form", "Купить"))
        pushButton_5.setText(_translate("Form", "Купить"))
        pushButton_6.setText(_translate("Form", "Купить"))
        pushButton_7.setText(_translate("Form", "Назад"))
        self.shop_list = [label_3, label_17, label_19, label_16, pushButton_12, label_18, pushButton_11, pushButton_10,
                          label_21, label_20, label_32, label_33, label_34, label, label_26, label_27, label_6, label_4,
                          label_5, label_7, pushButton, label_28, label_8, label_9, pushButton_3, pushButton_4, label_2,
                          label_10, label_12, label_14, label_11, label_13, label_15, label_22, label_23, label_24,
                          pushButton_2, pushButton_5, pushButton_6, pushButton_7]
        for i in self.shop_list:
            i.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UiMainWindow()
    window.show()
    sys.exit(app.exec())
