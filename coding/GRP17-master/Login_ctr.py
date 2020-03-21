from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from Login_View import login_View
from ModulePage_View import modulePage_view
from basicMainWindow_View import basicMainWindow_view
from basicMainWindow_Ctr import basicMainWindow_Ctr

'''Login Controller is used for create main Window and show corresponding frames based on the main Window'''

class login_Ctr():

    def __init__(self):
        #super(login_Ctr, self).__init__()
        # TODO: test login input, link to data
        # bindModel = login_Model()
        # self.loginView = None
        self.loginView = login_View()
        #self.loginView.pushButton.clicked.connect(self.login)
        #self.loginView.toolButton.clicked.connect(self.forgetPwd)

        # create main window, set view and controller
        self.mainWindow = basicMainWindow_view()
        self.mainWindowCtr = basicMainWindow_Ctr()
        self.mainWindowCtr.setView(self.mainWindow)

        # pass main window to corresponding page class for use
        self.tmView = modulePage_view()
        self.tmView.setMainWindow(self.mainWindow)

        self.mainWindowCtr.setWindow(self.tmView)

    #def login(self):
    #    print("login")
    #    self.loginView.login_Signal.emit()

    #def forgetPwd(self):
    #    self.loginView.forgetPwd_Signal.emit()
    #    print("forget")
        """
               Slot documentation goes here.
        """
        # TODO: show the forget pw dialog

    def setView(self, loginView):
        self.loginView = loginView
        self.connectSlot()

    def connectSlot(self):
        self.loginView.login_Signal.connect(self.enterMainPage)
        #self.loginView.login_Signal.connect(self.login)
        #self.loginView.forgetPwd_Signal.connect(self.forgetPwd)

    def enterMainPage(self):
        self.loginView.hide()
        self.tmView.show()




