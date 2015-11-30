# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ryan\Dropbox\python workspace\projectUI\Register.ui'
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

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName(_fromUtf8("Register"))
        Register.resize(284, 218)
        self.frame = QtGui.QFrame(Register)
        self.frame.setGeometry(QtCore.QRect(10, 10, 161, 191))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 100, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_6 = QtGui.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.lineEdit_6.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_5 = QtGui.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 140, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.registerButton = QtGui.QPushButton(Register)
        self.registerButton.setGeometry(QtCore.QRect(180, 30, 75, 23))
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.cancelButton = QtGui.QPushButton(Register)
        self.cancelButton.setGeometry(QtCore.QRect(180, 70, 75, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)
        Register.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        Register.setTabOrder(self.lineEdit_6, self.lineEdit_4)
        Register.setTabOrder(self.lineEdit_4, self.lineEdit)

    def retranslateUi(self, Register):
        Register.setWindowTitle(_translate("Register", "Register New User", None))
        self.label_3.setText(_translate("Register", "Confirm Password:", None))
        self.label_2.setText(_translate("Register", "Password:", None))
        self.label.setText(_translate("Register", "Username:", None))
        self.label_4.setText(_translate("Register", "Email address", None))
        self.registerButton.setText(_translate("Register", "Register", None))
        self.cancelButton.setText(_translate("Register", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Register = QtGui.QDialog()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())

