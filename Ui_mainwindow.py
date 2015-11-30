# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ryan\Dropbox\python workspace\projectUI\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(305, 133)
        self.addressBox = QtGui.QLineEdit(mainWindow)
        self.addressBox.setGeometry(QtCore.QRect(30, 30, 181, 21))
        self.addressBox.setObjectName(_fromUtf8("addressBox"))
        self.pushButton = QtGui.QPushButton(mainWindow)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(mainWindow)
        self.label.setGeometry(QtCore.QRect(30, 10, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(mainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addressBox.clear)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Connect", None))
        self.pushButton.setText(_translate("mainWindow", "Connect", None))
        self.label.setText(_translate("mainWindow", "Server Address:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QDialog()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

