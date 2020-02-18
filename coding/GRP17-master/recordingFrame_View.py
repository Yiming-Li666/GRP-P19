from resources.teacherUIPY.recording_totalframe import recording_totalframe
from PyQt5.QtCore import pyqtSignal
from recordingFrame_ctr import recordingFrame_ctr
from PyQt5.QtWidgets import QFrame


class recordingFrame_View(QFrame, recording_totalframe):
    start_Signal = pyqtSignal()
    

    def __init__(self):
        super(recordingFrame_View, self).__init__()
        self.setupUi(self)

        #connect with ctr
        self.recordingFrameCtr = recordingFrame_ctr()
        self.recordingFrameCtr.setCtr(self)
        

    #for hide session window
    def setSessionWindow(self, Session):
        self.sessionWindow = Session

    def start(self):
        self.start_Signal.emit()