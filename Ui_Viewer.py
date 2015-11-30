# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ryan\Dropbox\python workspace\projectUI\Viewer.ui'
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

class Ui_Viewer(object):
    def setupUi(self, Viewer):
        Viewer.setObjectName(_fromUtf8("Viewer"))
        Viewer.resize(400, 300)
        self.webView = QtWebKit.QWebView(Viewer)
        self.webView.setGeometry(QtCore.QRect(30, 50, 300, 200))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.label = QtGui.QLabel(Viewer)
        self.label.setGeometry(QtCore.QRect(30, 30, 221, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Viewer)
        QtCore.QMetaObject.connectSlotsByName(Viewer)

    def retranslateUi(self, Viewer):
        Viewer.setWindowTitle(_translate("Viewer", "Form", None))
        self.label.setText(_translate("Viewer", "connection status gets changed in init", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Viewer = QtGui.QWidget()
    ui = Ui_Viewer()
    ui.setupUi(Viewer)
    Viewer.show()
    sys.exit(app.exec_())

