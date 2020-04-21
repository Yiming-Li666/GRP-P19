from oneStudentFrame_View import oneStudentFrame_view
from upcomingEvent_View import upcomingEvent_view
from PyQt5.QtWidgets import QApplication, QMainWindow
from upcomingEvent_Model import upcomingEvent_Model
from oneStudentPage_Ctr import oneStudentPage_Ctr
from PyQt5.QtCore import pyqtSignal

import sys

class oneStudentPage_View(QMainWindow):
    studentRecord_Sig = pyqtSignal()

    def __init__(self):
        super(oneStudentPage_View, self).__init__()
        
        ##connect with Ctr
        
    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()
    
    def setMainWindow(self, mainWindow, logCtr):
        self.window = mainWindow
        self.logCtr = logCtr
        self.setupMyUI()
    
    def setupMyUI(self):
        #set up Ctr
        self.oneStudentPageCtr = oneStudentPage_Ctr()
        self.oneStudentPageCtr.setCtr(self, self.window)
        
        #build view
        self.Frame1 = oneStudentFrame_view()
        self.upcomingFrame = upcomingEvent_view()
        
        self.Frame1.enterAttendancePage_SignalToPage.connect(self.goStudentRecord)
        

        #setUp view
        self.Frame1.setupUi(self.window.oneStudentFrame1)
        self.Frame1.refresh()
        self.upcomingFrame.setupUi(self.window.oneStudentFrame2)
        self.upcomingFrame.connectToRecord(self.window)
    
    def goStudentRecord(self):
        print("here")
        self.studentRecord_Sig.emit()