from PyQt5 import QtCore
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton,
                             QHBoxLayout, QProgressBar, QTextBrowser)


class UiMainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("RPG game")
        self.shop_list = []
        self.main_list = []
        self.resize(971, 716)
        self.setMinimumSize(QtCore.QSize(971, 716))
        self.setMaximumSize(QtCore.QSize(971, 716))
        self.main_create()

    def main_create(self):

        # self.grid = QGridLayout(self)
        centralwidget = QWidget(self)
        centralwidget.setObjectName("centralwidget")

        # Надпись "Характеристики"
        self.label_13 = QLabel(centralwidget)
        # self.grid.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.label_13.setObjectName("label_13")

        label_10 = QLabel(centralwidget)
        label_10.setGeometry(QtCore.QRect(170, 40, 141, 21))
        label_10.setObjectName("label_10")

        label_11 = QLabel(centralwidget)
        label_11.setGeometry(QtCore.QRect(170, 100, 141, 21))
        label_11.setObjectName("label_11")

        pushButton = QPushButton(centralwidget)
        pushButton.setGeometry(QtCore.QRect(780, 10, 181, 71))
        pushButton.setStyleSheet("background: rgb(34, 168, 19)\n""")
        pushButton.setObjectName("pushButton")
        pushButton.pressed.connect(self.shop_open)

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
        self.label_13.setText(_translate("MainWindow", "Ваши характеристики:"))
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

        pushButton_3.pressed.connect(self.fight_open)
        pushButton_4.pressed.connect(self.fight_open)
        pushButton_5.pressed.connect(self.fight_open)
        pushButton_6.pressed.connect(self.fight_open)

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

        pushButton_112 = QPushButton(self)
        pushButton_112.setGeometry(QtCore.QRect(830, 110, 61, 91))
        pushButton_112.setObjectName("pushButton_12")

        label_118 = QLabel(self)
        label_118.setGeometry(QtCore.QRect(700, 267, 71, 31))
        label_118.setObjectName("label_18")

        pushButton_111 = QPushButton(self)
        pushButton_111.setGeometry(QtCore.QRect(830, 210, 61, 91))
        pushButton_111.setObjectName("pushButton_11")

        pushButton_110 = QPushButton(self)
        pushButton_110.setGeometry(QtCore.QRect(830, 310, 61, 91))
        pushButton_110.setObjectName("pushButton_10")

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
        label_51.setGeometry(QtCore.QRect(90, 180, 71, 21))
        label_51.setObjectName("label_5")

        label_71 = QLabel(self)
        label_71.setGeometry(QtCore.QRect(90, 260, 108, 32))
        label_71.setObjectName("label_7")

        pushButton01 = QPushButton(self)
        pushButton01.setGeometry(QtCore.QRect(210, 110, 61, 91))
        pushButton01.setObjectName("pushButton")

        label_218 = QLabel(self)
        label_218.setGeometry(QtCore.QRect(10, 320, 61, 91))
        label_218.setObjectName("label_28")

        label_81 = QLabel(self)
        label_81.setGeometry(QtCore.QRect(90, 320, 61, 31))
        label_81.setObjectName("label_8")

        label_91 = QLabel(self)
        label_91.setGeometry(QtCore.QRect(90, 370, 121, 31))
        label_91.setObjectName("label_9")

        pushButton_31 = QPushButton(self)
        pushButton_31.setGeometry(QtCore.QRect(210, 210, 61, 91))
        pushButton_31.setObjectName("pushButton_3")

        pushButton_41 = QPushButton(self)
        pushButton_41.setGeometry(QtCore.QRect(210, 320, 61, 91))
        pushButton_41.setObjectName("pushButton_4")

        label_21 = QLabel(self)
        label_21.setGeometry(QtCore.QRect(360, 70, 83, 16))
        label_21.setObjectName("label_2")

        label_110 = QLabel(self)
        label_110.setGeometry(QtCore.QRect(400, 110, 41, 16))
        label_110.setObjectName("label_10")

        label_112 = QLabel(self)
        label_112.setGeometry(QtCore.QRect(400, 220, 61, 16))
        label_112.setObjectName("label_12")

        label_114 = QLabel(self)
        label_114.setGeometry(QtCore.QRect(390, 332, 124, 20))
        label_114.setObjectName("label_14")

        label_111 = QLabel(self)
        label_111.setGeometry(QtCore.QRect(400, 180, 81, 21))
        label_111.setObjectName("label_11")

        label_113 = QLabel(self)
        label_113.setGeometry(QtCore.QRect(400, 270, 111, 32))
        label_113.setObjectName("label_13")

        label_115 = QLabel(self)
        label_115.setGeometry(QtCore.QRect(390, 371, 111, 31))
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

        pushButton_21 = QPushButton(self)
        pushButton_21.setGeometry(QtCore.QRect(520, 210, 61, 91))
        pushButton_21.setObjectName("pushButton_2")

        pushButton_51 = QPushButton(self)
        pushButton_51.setGeometry(QtCore.QRect(520, 310, 61, 91))
        pushButton_51.setObjectName("pushButton_5")

        pushButton_61 = QPushButton(self)
        pushButton_61.setGeometry(QtCore.QRect(520, 110, 61, 91))
        pushButton_61.setObjectName("pushButton_6")

        pushButton_71 = QPushButton(self)
        pushButton_71.setGeometry(QtCore.QRect(355, 10, 211, 31))
        pushButton_71.setStyleSheet("background: rgb(34, 168, 19)\n""")
        pushButton_71.setObjectName("pushButton_7")
        pushButton_71.pressed.connect(self.main_open)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        label_31.setText(_translate("Form", "Зелья:"))
        label_117.setText(_translate("Form", "Зелье\n"
                                             "ловкости"))
        label_119.setText(_translate("Form", "Зелье\n"
                                             "берсеркера"))
        label_116.setText(_translate("Form", "увертливость: +30"))
        pushButton_112.setText(_translate("Form", "Купить"))
        label_118.setText(_translate("Form", "атака: +30"))
        pushButton_111.setText(_translate("Form", "Купить"))
        pushButton_110.setText(_translate("Form", "Купить"))
        label_211.setText(_translate("Form", "защита: +30"))
        label_210.setText(_translate("Form", "Зелье\n"
                                             "стальной кожи"))
        label_312.setText(_translate("Form", "<html><head/><body><p><img src=\"lovkost.png\"/></p></body></html>"))
        label_313.setText(_translate("Form", "<html><head/><body><p><img src=\"berserk.png\"/></p></body></html>"))
        label_314.setText(_translate("Form", "<html><head/><body><p><img src=\"poition1.jpg\"/></p></body></html>"))
        label01.setText(_translate("Form", "Оружие:"))
        label_216.setText(_translate("Form", "<html><head/><body><p><img src=\"sword.png\"/></p></body></html>"))
        label_217.setText(_translate("Form", "<html><head/><body><p><img src=\"axe.jpg\"/></p></body></html>"))
        label_61.setText(_translate("Form", "Топор"))
        label_41.setText(_translate("Form", "Меч"))
        label_51.setText(_translate("Form", "урон: +20"))
        label_71.setText(_translate("Form", "урон: +40\n"
                                            "увертливость: -10"))
        pushButton01.setText(_translate("Form", "Купить"))
        label_218.setText(_translate("Form", "<html><head/><body><p><img src=\"hammer.jpg\"/></p></body></html>"))
        label_81.setText(_translate("Form", "Боевой\n"
                                            "молот"))
        label_91.setText(_translate("Form", "урон: +70\n"
                                            "увертливость: -40"))
        pushButton_31.setText(_translate("Form", "Купить"))
        pushButton_41.setText(_translate("Form", "Купить"))
        label_21.setText(_translate("Form", "Броня:"))
        label_110.setText(_translate("Form", "Кираса"))
        label_112.setText(_translate("Form", "Кольчуга"))
        label_114.setText(_translate("Form", "Латы"))
        label_111.setText(_translate("Form", "защита: +30"))
        label_113.setText(_translate("Form", "защита: +60\n"
                                             "увертливость: -20"))
        label_115.setText(_translate("Form", "защита: +100\n"
                                             "увертливость: -50"))
        label_212.setText(_translate("Form", "<html><head/><body><p><img src=\"cuirass.jpg\"/></p></body></html>"))
        label_213.setText(_translate("Form", "<html><head/><body><p><img src=\"chain.jpg\"/></p></body></html>"))
        label_214.setText(_translate("Form", "<html><head/><body><p><img src=\"armor.png\"/></p></body></html>"))
        pushButton_21.setText(_translate("Form", "Купить"))
        pushButton_51.setText(_translate("Form", "Купить"))
        pushButton_61.setText(_translate("Form", "Купить"))
        pushButton_71.setText(_translate("Form", "Назад"))

        self.shop_list = [label_31, label_117, label_119, label_116, pushButton_112, label_118,
                          pushButton_111, pushButton_110, label_211, label_210, label_312, label_313,
                          label_314, label01, label_216, label_217, label_61, label_41,
                          label_51, label_71, pushButton01, label_218, label_81, label_91,
                          pushButton_31, pushButton_41, label_21, label_110, label_112,
                          label_114, label_111, label_113, label_115, label_212, label_213,
                          label_214, pushButton_21, pushButton_51, pushButton_61, pushButton_71]

        # self.setLayout(self.grid)
        self.main_list = [self.label_13, label_10, label_11, pushButton, label_12, label_9, label_6, label_5,
                          label_2, label_4, label, label_3, label_7, label_8, pushButton_3, pushButton_4,
                          pushButton_5, pushButton_6]
        for i in self.shop_list:
            i.hide()

        labels = QLabel(self)
        labels.setGeometry(QtCore.QRect(15, 100, 221, 301))
        labels.setObjectName("label")
        progressBars = QProgressBar(self)
        progressBars.setGeometry(QtCore.QRect(20, 70, 221, 23))
        progressBars.setProperty("value", 24)
        progressBars.setObjectName("progressBar")
        label_2s = QLabel(self)
        label_2s.setGeometry(QtCore.QRect(80, 40, 121, 16))
        label_2s.setObjectName("label_2")
        textBrowsers = QTextBrowser(self)
        textBrowsers.setGeometry(QtCore.QRect(260, 100, 381, 301))
        textBrowsers.setObjectName("textBrowser")
        label_3s = QLabel(self)
        label_3s.setGeometry(QtCore.QRect(280, 50, 55, 16))
        label_3s.setObjectName("label_3")
        label_4s = QLabel(self)
        label_4s.setGeometry(QtCore.QRect(400, 50, 91, 16))
        label_4s.setObjectName("label_4")
        label_5s = QLabel(self)
        label_5s.setGeometry(QtCore.QRect(280, 70, 71, 16))
        label_5s.setObjectName("label_5")
        label_6s = QLabel(self)
        label_6s.setGeometry(QtCore.QRect(400, 70, 111, 16))
        label_6s.setObjectName("label_6")
        progressBar_2s = QProgressBar(self)
        progressBar_2s.setGeometry(QtCore.QRect(20, 550, 221, 23))
        progressBar_2s.setProperty("value", 24)
        progressBar_2s.setObjectName("progressBar_2")
        label_7s = QLabel(self)
        label_7s.setGeometry(QtCore.QRect(90, 520, 121, 16))
        label_7s.setObjectName("label_7")
        label_12s = QLabel(self)
        label_12s.setGeometry(QtCore.QRect(520, 50, 55, 16))
        label_12s.setObjectName("label_12")
        label_13s = QLabel(self)
        label_13s.setGeometry(QtCore.QRect(520, 70, 71, 16))
        label_13s.setObjectName("label_13")
        label_8s = QLabel(self)
        label_8s.setGeometry(QtCore.QRect(260, 560, 71, 16))
        label_8s.setObjectName("label_8")
        label_9s = QLabel(self)
        label_9s.setGeometry(QtCore.QRect(260, 540, 55, 16))
        label_9s.setObjectName("label_9")
        label_14s = QLabel(self)
        label_14s.setGeometry(QtCore.QRect(500, 560, 121, 16))
        label_14s.setObjectName("label_14")
        label_10s = QLabel(self)
        label_10s.setGeometry(QtCore.QRect(380, 560, 111, 16))
        label_10s.setObjectName("label_10")
        label_11s = QLabel(self)
        label_11s.setGeometry(QtCore.QRect(380, 540, 91, 16))
        label_11s.setObjectName("label_11")
        label_15s = QLabel(self)
        label_15s.setGeometry(QtCore.QRect(500, 540, 55, 16))
        label_15s.setObjectName("label_15")

        _translates = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translates("Form", "Form"))
        labels.setText(_translates("Form", "<html><head/><body><p><img src=\"magomed.png\"/></p></body></html>"))
        label_2s.setText(_translates("Form", "Здоровье: 48"))
        label_3s.setText(_translates("Form", "Броня"))
        label_4s.setText(_translates("Form", "Увертливость"))
        label_5s.setText(_translates("Form", "Кираса, 20"))
        label_6s.setText(_translates("Form", "100"))
        label_7s.setText(_translates("Form", "Здоровье: 72"))
        label_12s.setText(_translates("Form", "Оружие"))
        label_13s.setText(_translates("Form", "Кинжал, 30"))
        label_8s.setText(_translates("Form", "Латы, 100"))
        label_9s.setText(_translates("Form", "Броня"))
        label_14s.setText(_translates("Form", "Боевой молот, 120"))
        label_10s.setText(_translates("Form", "10"))
        label_11s.setText(_translates("Form", "Увертливость"))
        label_15s.setText(_translates("Form", "Оружие"))
        self.fight_list = [labels, label_2s, label_3s, label_4s, label_5s, label_6s, textBrowsers, label_7s, label_8s,
                           label_9s, label_10s, label_11s, label_12s, label_13s, label_14s, label_15s, progressBar_2s,
                           progressBars]
        for i in self.fight_list:
            i.hide()

    def shop_open(self):
        for i in self.main_list:
            i.hide()
        for i in self.shop_list:
            i.show()

    def main_open(self):
        for i in self.main_list:
            i.show()
        for i in self.shop_list:
            i.hide()

    def fight_open(self):
        for i in self.fight_list:
            i.show()
        for i in self.main_list:
            i.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UiMainWindow()
    window.show()
    sys.exit(app.exec())
