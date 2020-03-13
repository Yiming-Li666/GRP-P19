from teacherInfoFrame_View import teacherInfoFrame_View
from PyQt5.QtWidgets import QMainWindow
from upcomingEvent_View import upcomingEvent_view

class teacherInfoPage_View(QMainWindow):

    def __init__(self):
        super(teacherInfoPage_View, self).__init__()
        self.window = None

    def setMainWindow(self, mainWindow):
        self.window = mainWindow
        self.setupMyUI()
    
    def setupMyUI(self):
        self.upcomingFrame = upcomingEvent_view()
        self.Frame1 = teacherInfoFrame_View()
        self.Frame1.setupUi(self.window.teacherInfoFrame1)
        self.upcomingFrame.setupUi(self.window.teacherInfoFrame2)
