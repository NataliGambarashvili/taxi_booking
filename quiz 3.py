
from PyQt5 import QtCore, QtWidgets
from taxxi import Ui_MainWindow

class TaxiApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)


        self.pushButton.clicked.connect(self.show_selection)
        self.comboBox.currentTextChanged.connect(self.on_city_changed)
        self.lineEdit.textChanged.connect(self.on_address_changed)
        self.comboBox_2.currentTextChanged.connect(self.update_price)


        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)


        self.update_price(self.comboBox_2.currentText())

    def show_selection(self):
        city = self.comboBox.currentText()
        address = self.lineEdit.text().strip()
        taxi_type = self.comboBox_2.currentText()

        if not address:
            QtWidgets.QMessageBox.warning(self, "შეცდომა", "მისამართის ველი ცარიელია! გთხოვთ შეავსეთ.")
            return

        message = f"ქალაქი: {city}\nმისამართი: {address}\nტაქსის ტიპი: {taxi_type}"
        QtWidgets.QMessageBox.information(self, "შეკვეთის ინფორმაცია", message)

    def update_time(self):
        now = QtCore.QDateTime.currentDateTime()
        current_time = now.toString("HH:mm:ss")
        current_date = now.toString("dd.MM.yyyy")
        self.timelabel.setText(f"დრო: {current_time}  თარიღი: {current_date}")


    def update_price(self, text):
        prices = {
            "ეკონომი": 5,
            "სტანდარტი": 10,
            "ბიზნესი": 20,
            "მინივენი": 15
        }
        price = prices.get(text, 0)
        self.pricelabel.setText(f"ფასი: {price}₾")

    def toggle_dark_mode(self, state):
        if state == QtCore.Qt.Checked:

            self.centralwidget.setStyleSheet("background-color: #2b2b2b; color: white;")
            self.label.setStyleSheet("color: white; background: #2b2b2b")
            self.label_3.setStyleSheet("color: white; background: #2b2b2b")
            self.label_4.setStyleSheet("color: white; background: #2b2b2b")
            self.pricelabel.setStyleSheet("color: white; background: #2b2b2b")
            self.timelabel.setStyleSheet("color: white; background: #2b2b2b")
            self.comboBox.setStyleSheet("background-color: #3c3c3c; color: white;")
            self.comboBox_2.setStyleSheet("background-color: #3c3c3c; color: white;")
            self.lineEdit.setStyleSheet("background-color: #3c3c3c; color: white;")
            self.dark_mode_checkbox.setStyleSheet("color: white; background: #2b2b2b")
            self.pushButton.setStyleSheet("background-color: #444; color: white;")
        else:

            self.centralwidget.setStyleSheet("")
            self.label.setStyleSheet("color: green; background: white")
            self.label_3.setStyleSheet("color: green; background: white")
            self.label_4.setStyleSheet("color: green; background: white")
            self.pricelabel.setStyleSheet("")
            self.timelabel.setStyleSheet("")
            self.comboBox.setStyleSheet("")
            self.comboBox_2.setStyleSheet("")
            self.lineEdit.setStyleSheet("")
            self.dark_mode_checkbox.setStyleSheet("")
            self.pushButton.setStyleSheet("")

    def on_city_changed(self, text):
        print("ქალაქი შეიცვალა:", text)

    def on_address_changed(self, text):
        print("მისამართი შეიცვალა:", text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TaxiApp()
    window.show()
    sys.exit(app.exec_())