from upcomingEvent_Model import upcomingEvent_Model
class oneStudentPage_Ctr():
    def __init__(self):
        self.oneStudentPageView = None
        self.mainwindow = None

    def setCtr(self, oneStudentPageView, mainwindow):
        self.oneStudentPageView = oneStudentPageView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.oneStudentPageView.studentRecord_Sig.connect(self.enterStudentRecordPage)

    def enterStudentRecordPage(self):
        self.upcomingModel = upcomingEvent_Model()
        self.oneStudentPageView.logCtr.studentRecordPage_View.upcomingFrame.listView.setModel(self.upcomingModel)
        self.mainwindow.stackedWidget.setCurrentIndex(6)