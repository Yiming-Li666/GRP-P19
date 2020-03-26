from recordDialog_View import recordDialog_View
from upcomingEvent_Model import upcomingEvent_Model

# TBC
class sessionPage_ctr():

    def setCtr(self, sessionPageView, mainwindow):
        self.sessionPageView = sessionPageView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.sessionPageView.recordDialog_Signal.connect(self.recordDialog)
        self.sessionPageView.recordedSession_Signal.connect(self.Recorded)

    def recordDialog(self):
        self.dialog = recordDialog_View()
        self.dialog.setSessionWindow(self.mainwindow)
        self.dialog.show()
    
    def Recorded(self):
        '''
        Load recored session info here!!!
        '''
        self.upcomingModel = upcomingEvent_Model()
        self.sessionPageView.logCtr.recordedSessionPage_View.upcomingFrame.listView.setModel(self.upcomingModel)
        self.mainwindow.stackedWidget.setCurrentIndex(7)