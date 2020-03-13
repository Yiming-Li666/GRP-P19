from PyQt5.QtWidgets import QDialog

from ModulePage_View import modulePage_view
from basicMainWindow_View import basicMainWindow_view
from basicMainWindow_Ctr import basicMainWindow_Ctr
from sessionPage_View import sessionPage_View
from recordDialog_View import recordDialog_View
from recordingPage_View import recordingPage_View
from searchResult_View import searchResult_view
from oneStudentPage_View import oneStudentPage_View
from teacherInfoPage_View import teacherInfoPage_View
from resources.teacherUIPY.forgetPw_Dialog import forgetPw_dialog
'''Login Controller is used for create main Window and show corresponding frames based on the main Window'''

class login_Ctr():

    def __init__(self):
        # TODO: test login input, link to data
        # bindModel = login_Model()
        self.loginView = None

        # create main window, set view and controller
        self.mainWindow = basicMainWindow_view()
        self.mainWindowCtr = basicMainWindow_Ctr()
        #pass login_Ctr to be able to get searchResult_View in mainwindowCtr
        self.mainWindowCtr.setView(self.mainWindow, self)

        # pass main window to corresponding page class for use
        # create each basic page
        # information in each page will be loaded when change the page
        self.tmView = modulePage_view()
        self.sessionView = sessionPage_View()
        self.recordingPage_View = recordingPage_View()
        self.searchResult_View = searchResult_view()
        self.oneStudentPage_View = oneStudentPage_View()
        self.teacherInfoPage_View = teacherInfoPage_View()
        
        self.tmView.setMainWindow(self.mainWindow, self)
        self.sessionView.setMainWindow(self.mainWindow)
        self.recordingPage_View.setMainWindow(self.mainWindow)
        self.searchResult_View.setMainWindow(self.mainWindow, self)
        self.oneStudentPage_View.setMainWindow(self.mainWindow)
        self.teacherInfoPage_View.setMainWindow(self.mainWindow)
        
        

        self.mainWindowCtr.setWindow(self.tmView)

    def setView(self, loginView):
        self.loginView = loginView
        self.connectSlot()

    def connectSlot(self):
        self.loginView.login_Signal.connect(self.enterMainPage)
        self.loginView.forgetPwd_Signal.connect(self.forgetPwd)

    def enterMainPage(self):
        self.loginView.hide()
        self.tmView.show()

    def forgetPwd(self):
        """
               show the forget password dialog
        """
        self.dialog = QDialog()
        self.forgetPwDialog = forgetPw_dialog()
        self.forgetPwDialog.setupUi(self.dialog)
        self.dialog.show()





