from studentRecordFrame_View import studentRecordFrame_View
from studentRecordFrame_Ctr import studentRecordFrame_Ctr
from upcomingEvent_View import upcomingEvent_view
from PyQt5.QtWidgets import QMainWindow

class studentRecordPage_View(QMainWindow):
    def __init__(self):
        super(studentRecordPage_View, self).__init__()
        self.window = None
    
    def setMainWindow(self, mainWindow):
        self.window = mainWindow
        self.setupMyUI()

    def setupMyUI(self):
        self.upcomingFrame = upcomingEvent_view()
        self.Frame1 = studentRecordFrame_View()

        #connect with Ctr
        self.studentRecordFrame_Ctr = studentRecordFrame_Ctr()
        self.studentRecordFrame_Ctr.setCtr(self.Frame1)

        self.Frame1.setupUi(self.window.studentRecordFrame1)

        self.upcomingFrame.setupUi(self.window.studentRecordFrame2)
        self.upcomingFrame.connectToRecord(self.window)