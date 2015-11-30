# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import requests
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

from Ui_mainwindow import Ui_mainWindow
from Ui_Login import Ui_Login
from Ui_Register import Ui_Register


class MainWindow(QDialog, Ui_mainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
    
    @pyqtSlot()
    def on_pushButton_released(self):
        """
        Slot documentation goes here.
        """
        #TODO: Verify website URL. Be sure that it does the correct behavior on connecting to the correct website,
        #and delivers an error message for the incorrect website (every single other website)
        if (self.addressBox.text().startswith("http://")):
            url = self.addressBox.text()
        else:
            url = "http://" + self.addressBox.text()
        
        r = requests.get(url)
        
        if (r): #change this to input != database
            QMessageBox.critical(self, "Error", "Invalid server address. Please re-enter address.")
        else:
            self.nextform = Login(self,  url)
            self.nextform.show()
            
            
class Login(QDialog, Ui_Login):
    """
    Class documentation goes here.
    """
    def __init__(self,  url,  parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        self.__url = url
        super(Login, self).__init__(parent)
        self.setupUi(self)
    
    @property
    def url(self):
        return self.__url
        
    @pyqtSlot()
    def on_loginButton_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        s = requests.Session()
        r = s.get(url)
        print(r.codes)
        
        self.nextform = Viewer(self)

    @pyqtSlot()
    def on_newUserButton_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.nextform = Register(self)
        self.nextform.show()

        
class Register(QDialog, Ui_Register):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(Register, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_registerButton_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cancelButton_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

class Viewer(QWidget, Ui_Viewer):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        self.webView.setUrl(QUrl(parent.url()))
        super(Viewer, self).__init__(parent)
        self.setupUi(self)
        


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

	
main()