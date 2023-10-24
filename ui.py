# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 181))
        self.frame.setStyleSheet("background-color: #ADFF2F")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(50, 0, 391, 171))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../d8226bc1/currency_exchange_FILL0_wght600_GRAD200_opsz48.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.input_currency = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(50, 210, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(14)
        font.setBold(True)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #ADFF2F;\n"
"border-radius: 30;\n"
"color: white\n"
"")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.input_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(50, 300, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(14)
        font.setBold(True)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #ADFF2F;\n"
"border-radius: 30;\n"
"color: white\n"
"")
        self.input_amount.setText("")
        self.input_amount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(50, 390, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(14)
        font.setBold(True)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #ADFF2F;\n"
"border-radius: 30;\n"
"color: white\n"
"")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(50, 480, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(14)
        font.setBold(True)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #ADFF2F;\n"
"border-radius: 30;\n"
"color: white\n"
"")
        self.output_amount.setText("")
        self.output_amount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 560, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #ADFF2F;\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fa4244\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "КОНВЕРТЕР ВАЛЮТ"))
        self.pushButton.setText(_translate("MainWindow", "КОНВЕРТИРУЙ"))
