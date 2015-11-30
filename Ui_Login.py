# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ryan\Dropbox\python workspace\projectUI\Login.ui'
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

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(260, 110)
        Login.setSizeGripEnabled(True)
        self.lineEdit = QtGui.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.loginButton = QtGui.QPushButton(Login)
        self.loginButton.setGeometry(QtCore.QRect(150, 30, 101, 23))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.newUserButton = QtGui.QPushButton(Login)
        self.newUserButton.setGeometry(QtCore.QRect(150, 70, 101, 23))
        self.newUserButton.setObjectName(_fromUtf8("newUserButton"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login", None))
        self.label.setText(_translate("Login", "Username:", None))
        self.label_2.setText(_translate("Login", "Password:", None))
        self.loginButton.setText(_translate("Login", "Login", None))
        self.newUserButton.setText(_translate("Login", "Register new User", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Login = QtGui.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

