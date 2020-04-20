from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import COVID19Py
from pycountry import countries
import pandas as pd
import matplotlib.pyplot as plt 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 564)
        MainWindow.setStyleSheet("background-color:black;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 641, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images (11).jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images (10).jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 400, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color:white;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 470, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{border-radius:25px;\n"
"background-color:green;}\n"
"\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 360, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#ddd;")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.corona)
        self.pushButton.clicked.connect(self.lineEdit.clear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Corona Virus Update News (Developer Chando)"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images (11).jpeg\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>COUNTER</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Check"))
        self.label_3.setText(_translate("MainWindow", "Country Name"))

    def corona(self):
        user=self.lineEdit.text()
        user=user.capitalize()
        try:
            code=countries.get(name=user).alpha_2
            covid=COVID19Py.COVID19()
            location=covid.getLocationByCountryCode(code)
            loc_data=location[0]
            virus_data=dict(loc_data['latest'])
            names=list(virus_data.keys())
            value=list(virus_data.values())
            plt.bar(range(len(virus_data)), value, tick_label= names)
            plt.xlabel(virus_data)
            plt.title("Corona Update News")
            plt.show()
        except Exception as e:
            msg=QMessageBox()
            msg.setWindowTitle("Alert")
            msg.setWindowIcon(QtGui.QIcon('images (10).jpeg'))
            msg.setIcon(QMessageBox.Question)
            msg.setText("Please Check Your Internet Connection and Also Country Code")
            x=msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
