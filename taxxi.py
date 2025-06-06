# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taxxi.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 543)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: green; background:white")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 60, 201, 41))
        self.comboBox.setIconSize(QtCore.QSize(40, 40))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 341, 41))
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_3.setStyleSheet("color: green; background:white;")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 170, 301, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 230, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:green; background:white")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 280, 201, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 350, 171, 51))
        self.pushButton.setObjectName("pushButton")
        self.pricelabel = QtWidgets.QLabel(self.centralwidget)
        self.pricelabel.setGeometry(QtCore.QRect(70, 340, 55, 16))
        self.pricelabel.setObjectName("pricelabel")
        self.timelabel = QtWidgets.QLabel(self.centralwidget)
        self.timelabel.setGeometry(QtCore.QRect(70, 410, 211, 16))
        self.timelabel.setObjectName("timelabel")
        self.dark_mode_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.dark_mode_checkbox.setGeometry(QtCore.QRect(70, 440, 111, 21))
        self.dark_mode_checkbox.setObjectName("dark_mode_checkbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 26))
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
        self.label.setText(_translate("MainWindow", "აირჩიე ქალაქი:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "თბილისი"))
        self.comboBox.setItemText(1, _translate("MainWindow", "რუსთავი"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ქუთაისი"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ბათუმი"))
        self.comboBox.setItemText(4, _translate("MainWindow", "გორი"))
        self.comboBox.setItemText(5, _translate("MainWindow", "ზუგდიდი"))
        self.label_3.setText(_translate("MainWindow", "ჩაწერე მისამართი:"))
        self.label_4.setText(_translate("MainWindow", "აირჩიე ტაქსის სახეობა: "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "ეკონომი"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "სტანდარტი"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "ბიზნესი"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "მინივენი"))
        self.pushButton.setText(_translate("MainWindow", "გამოიძახე ტაქსი"))
        self.pricelabel.setText(_translate("MainWindow", "ფასი:"))
        self.timelabel.setText(_translate("MainWindow", "დრო: "))
        self.dark_mode_checkbox.setText(_translate("MainWindow", "ღამის რეჟიმი"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
