# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'techniqueGhost.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(409, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.entryVideoInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.entryVideoInput.setGeometry(QtCore.QRect(10, 40, 271, 31))
        self.entryVideoInput.setObjectName("entryVideoInput")
        self.serchVideoButton = QtWidgets.QPushButton(self.centralwidget)
        self.serchVideoButton.setGeometry(QtCore.QRect(300, 40, 88, 31))
        self.serchVideoButton.setObjectName("serchVideoButton")
        self.entryImageOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.entryImageOutput.setGeometry(QtCore.QRect(10, 110, 271, 31))
        self.entryImageOutput.setObjectName("entryImageOutput")
        self.searchOutputFolder = QtWidgets.QPushButton(self.centralwidget)
        self.searchOutputFolder.setGeometry(QtCore.QRect(300, 110, 88, 31))
        self.searchOutputFolder.setObjectName("searchOutputFolder")
        self.acceptButton = QtWidgets.QPushButton(self.centralwidget)
        self.acceptButton.setGeometry(QtCore.QRect(10, 374, 381, 31))
        self.acceptButton.setObjectName("acceptButton")
        self.logEventText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.logEventText.setGeometry(QtCore.QRect(10, 235, 381, 121))
        self.logEventText.setObjectName("logEventText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 171, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(12, 161, 171, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(12, 202, 171, 18))
        self.label_4.setObjectName("label_4")
        self.ghostFactorEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.ghostFactorEntry.setGeometry(QtCore.QRect(140, 156, 250, 30))
        self.ghostFactorEntry.setObjectName("ghostFactorEntry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.serchVideoButton.setText(_translate("MainWindow", "Buscar"))
        self.searchOutputFolder.setText(_translate("MainWindow", "Buscar"))
        self.acceptButton.setText(_translate("MainWindow", "Aceptar"))
        self.label.setText(_translate("MainWindow", "Ingrese Video"))
        self.label_2.setText(_translate("MainWindow", "Ingrese Carpeta de Destino"))
        self.label_3.setText(_translate("MainWindow", "Factor de Fantasma"))
        self.label_4.setText(_translate("MainWindow", "Progreso"))
        self.ghostFactorEntry.setText(_translate("MainWindow", "4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
