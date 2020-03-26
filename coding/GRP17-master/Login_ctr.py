from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from Login_View import login_View
from ModulePage_View import modulePage_view
from basicMainWindow_View import basicMainWindow_view
from basicMainWindow_Ctr import basicMainWindow_Ctr

'''Login Controller is used for create main Window and show corresponding frames based on the main Window'''

class login_Ctr():

    def __init__(self):
        self.loginView = login_View()

        # create main window, set view and controllerx
        self.mainWindow = basicMainWindow_view()
        self.mainWindowCtr = basicMainWindow_Ctr()
        self.mainWindowCtr.setView(self.mainWindow)

        # pass main window to corresponding page class for use
        self.tmView = modulePage_view()
        self.tmView.setMainWindow(self.mainWindow)

        self.mainWindowCtr.setWindow(self.tmView)

    def setView(self, loginView):
        self.loginView = loginView
        self.connectSlot()

    def connectSlot(self):
        self.loginView.login_Signal.connect(self.enterMainPage)

    def enterMainPage(self):
        self.loginView.hide()
        self.tmView.show()




