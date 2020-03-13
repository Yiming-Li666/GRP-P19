from oneStudentPage_View import oneStudentPage_View
from oneStudentFrame_Model import oneStudentFrame_model

from upcomingEvent_Model import upcomingEvent_Model

class searchResult_Ctr():
    def setCtr(self, searchResultView, mainwindow):
        self.searchResultView = searchResultView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.searchResultView.OneStudentInfo_Signal.connect(self.OneStudentInfo)
    
    def OneStudentInfo(self):
        print("One Student")
        # set model for view in oneStudentPage_View
        self.upcomingModel = upcomingEvent_Model()
        self.searchResultView.logCtr.oneStudentPage_View.upcomingFrame.listView.setModel(self.upcomingModel)

        self.studentAttendanceModel = oneStudentFrame_model()
        self.searchResultView.logCtr.oneStudentPage_View.Frame1.attendance_listView.setModel(self.studentAttendanceModel)

        self.mainwindow.stackedWidget.setCurrentIndex(4)
