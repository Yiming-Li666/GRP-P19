from basicMainWindow_View import basicMainWindow_view

from basicMainWindow_Ctr import basicMainWindow_Ctr

from sessionPage_View import sessionPage_View

from PyQt5.QtWidgets import QFrame

from PyQt5 import QtCore, QtWidgets

# TBC
class ModulePage_ctr():

    def __init__(self):
        self.modulePageView = None

    def setCtr(self, modulePageView):
        self.modulePageView = modulePageView
        self.connectSlot()

    def connectSlot(self):
        self.modulePageView.enterSessionPage_Signal.connect(self.enterSessionPage)

    def enterSessionPage(self):

        print("to session")
        '''

        self.sessionFrame = sessionFrame1_View()

        self.sessionFrame.refresh()

        self.modulePageView.moduleFrame = self.sessionFrame

        self.modulePageView.window.frame1.reset()

        #self.sessionFrame.setupUi(self.modulePageView.window.frame1) 

        '''
        self.mainWindow = basicMainWindow_view()
        self.mainWindowCtr = basicMainWindow_Ctr()
        self.mainWindowCtr.setView(self.mainWindow)

        self.sessionView = sessionPage_View()
        self.sessionView.setMainWindow(self.mainWindow)
        self.modulePageView.hide()
        self.sessionView.show()