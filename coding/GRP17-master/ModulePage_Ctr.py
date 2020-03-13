from sessionFrame1_Model import sessionFrame1_model
from sessionFrame1_Delegate import sessionFrame_delegate
from upcomingEvent_Model import upcomingEvent_Model


class ModulePage_ctr():

    def __init__(self):
        self.modulePageView = None

    def setCtr(self, modulePageView, mainwindow):
        self.modulePageView = modulePageView
        self.mainwindow = mainwindow
        self.connectSlot()

    def connectSlot(self):
        self.modulePageView.enterSessionPage_Signal.connect(self.enterSessionPage)

    def enterSessionPage(self):

        print("to session")
        '''
        Change the related list module
        '''
        #load related session Model
        self.sessionModel = sessionFrame1_model()
        self.sessionDelegate = sessionFrame_delegate()
        self.modulePageView.logCtr.sessionView.Frame1.listView.setModel(self.sessionModel)
        self.modulePageView.logCtr.sessionView.Frame1.listView.setItemDelegate(self.sessionDelegate)

        self.upcomingModel = upcomingEvent_Model()
        self.modulePageView.logCtr.sessionView.upcomingFrame.listView.setModel(self.upcomingModel)
        
        #change page
        self.mainwindow.stackedWidget.setCurrentIndex(1)
