# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\karakurt\Documents\GitHub\Project\settingscustomer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(54, 100, 139);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 271, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 18pt \"Montserrat SemiBold\";")
        self.label.setObjectName("label")
        self.la_name = QtWidgets.QLabel(self.centralwidget)
        self.la_name.setGeometry(QtCore.QRect(50, 130, 141, 41))
        self.la_name.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Montserrat SemiBold\";")
        self.la_name.setObjectName("la_name")
        self.la_password = QtWidgets.QLabel(self.centralwidget)
        self.la_password.setGeometry(QtCore.QRect(50, 200, 171, 41))
        self.la_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Montserrat SemiBold\";")
        self.la_password.setObjectName("la_password")
        self.li_name = QtWidgets.QLineEdit(self.centralwidget)
        self.li_name.setGeometry(QtCore.QRect(310, 131, 291, 51))
        self.li_name.setStyleSheet("font: 63 14pt \"Montserrat SemiBold\";\n"
"color: rgb(255, 255, 255);")
        self.li_name.setObjectName("li_name")
        self.li_password = QtWidgets.QLineEdit(self.centralwidget)
        self.li_password.setGeometry(QtCore.QRect(310, 200, 291, 51))
        self.li_password.setStyleSheet("font: 63 14pt \"Montserrat SemiBold\";\n"
"color: rgb(255, 255, 255);")
        self.li_password.setObjectName("li_password")
        self.la_confpass = QtWidgets.QLabel(self.centralwidget)
        self.la_confpass.setGeometry(QtCore.QRect(50, 280, 221, 41))
        self.la_confpass.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Montserrat SemiBold\";")
        self.la_confpass.setObjectName("la_confpass")
        self.li_confpass = QtWidgets.QLineEdit(self.centralwidget)
        self.li_confpass.setGeometry(QtCore.QRect(310, 270, 291, 51))
        self.li_confpass.setStyleSheet("font: 63 14pt \"Montserrat SemiBold\";\n"
"color: rgb(255, 255, 255);")
        self.li_confpass.setObjectName("li_confpass")
        self.B_exit = QtWidgets.QPushButton(self.centralwidget)
        self.B_exit.setGeometry(QtCore.QRect(640, 490, 101, 41))
        self.B_exit.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 63 14pt \"Montserrat SemiBold\";\n"
"border-radius: 20;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.B_exit.setCheckable(False)
        self.B_exit.setObjectName("B_exit")
        self.B_back = QtWidgets.QPushButton(self.centralwidget)
        self.B_back.setGeometry(QtCore.QRect(640, 440, 101, 41))
        self.B_back.setStyleSheet("background-color: rgb(240, 240, 119);\n"
"color: rgb(54, 100, 139);\n"
"font: 63 14pt ;Montserrat SemiBold;\n"
"border-radius: 20;")
        self.B_back.setCheckable(False)
        self.B_back.setObjectName("B_back")
        self.la_error = QtWidgets.QLabel(self.centralwidget)
        self.la_error.setGeometry(QtCore.QRect(250, 350, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.la_error.setFont(font)
        self.la_error.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Montserrat SemiBold\";")
        self.la_error.setObjectName("la_error")
        self.B_save = QtWidgets.QPushButton(self.centralwidget)
        self.B_save.setGeometry(QtCore.QRect(650, 280, 101, 41))
        self.B_save.setStyleSheet("background-color: rgb(50, 173, 58);\n"
"font: 63 14pt ;Montserrat SemiBold;\n"
"border-radius: 20;\n"
"color: rgb(255, 255, 255);")
        self.B_save.setCheckable(False)
        self.B_save.setObjectName("B_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CHANGE SETTINGS"))
        self.la_name.setText(_translate("MainWindow", "New E-mail"))
        self.la_password.setText(_translate("MainWindow", "New Password"))
        self.la_confpass.setText(_translate("MainWindow", "Confirm Password"))
        self.B_exit.setText(_translate("MainWindow", "EXIT"))
        self.B_back.setText(_translate("MainWindow", "BACK"))
        self.la_error.setText(_translate("MainWindow", "Please enter 7 characters for new password"))
        self.B_save.setText(_translate("MainWindow", "SAVE"))
