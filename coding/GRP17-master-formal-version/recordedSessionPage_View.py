from recordedSessionFrame_View import recordedSessionFrame_View
from upcomingEvent_View import upcomingEvent_view
from PyQt5.QtWidgets import QMainWindow
import globalVar


class recordedSessionPage_View (QMainWindow):
    def __init__(self):
        super(recordedSessionPage_View, self).__init__()
        self.window = None
    
    def setMainWindow(self, mainWindow):
        self.window = mainWindow
        self.setupMyUI()
    
    def setupMyUI(self):
        self.upcomingFrame = upcomingEvent_view()
        self.Frame1 = recordedSessionFrame_View()
        globalVar.set_value('RecordedPage', self.Frame1)
        self.Frame1.setupUi(self.window.RecordedSessionFrame1)

        self.upcomingFrame.setupUi(self.window.RecordedSessionFrame2)
        self.upcomingFrame.connectToRecord(self.window)