from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class UiMainWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(1119, 864)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 19, 1061, 611))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setStyleSheet("background: rgb(34, 168, 19)\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 5, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Здоровье: 100"))
        self.label_10.setText(_translate("MainWindow", "Атака: 30"))
        self.label_11.setText(_translate("MainWindow", "Защита: 40"))
        self.label_12.setText(_translate("MainWindow", "Увертливость: 10"))
        self.pushButton.setText(_translate("MainWindow", "Магазин"))
        self.label_13.setText(_translate("MainWindow", "Ваши характеристики:"))
        self.pushButton_4.setText(_translate("MainWindow", "В бой"))
        self.pushButton_5.setText(_translate("MainWindow", "В бой"))
        self.label_3.setText(_translate("MainWindow", "Варвар\n"
                                        "Ещё более крутой чувак\n"
                                        "\n"
                                        "Характкристики:\n"
                                        "Здоровье : 500\n"
                                        "Атака: 70\n"
                                        "Защита: 50\n"
                                        "Увертливость: 30"))
        self.label_8.setText(_translate("MainWindow", "Маг\n"
                                        "АА Какой чувак\n"
                                        "\n"
                                        "Характкристики:\n"
                                        "Здоровье : 1200\n"
                                        "Атака: 250\n"
                                        "Защита: 100\n"
                                        "Увертливость: 50"))
        self.label.setText(_translate("MainWindow", "Ловкач\n"
                                      "Крутой ловкий чувак\n"
                                      "\n"
                                      "Характкристики:\n"
                                      "Здоровье : 200\n"
                                      "Атака: 50\n"
                                      "Защита: 10\n"
                                      "Увертливость: 100"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                      "<img src=\"ork.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                      "<img src=\"mag.jpg\"/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Орк\n"
                                        "Прям мега крутой чувак\n"
                                        "\n"
                                        "Характкристики:\n"
                                        "Здоровье : 750\n"
                                        "Атака: 120\n"
                                        "Защита: 50\n"
                                        "Увертливость: 20"))
        self.pushButton_3.setText(_translate("MainWindow", "В бой"))
        self.pushButton_2.setText(_translate("MainWindow", "В бой"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                      "<img src=\"magomed.png\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                      "<img src=\"barbarian1.jpg\"/></p></body></html>"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UiMainWindow()
    window.show()
    sys.exit(app.exec())
