from resources.teacherUIPY.recordedSession_Frame import recordedSession_Frame
from PyQt5.QtWidgets import QFrame
class recordedSessionFrame_View(QFrame, recordedSession_Frame):

    def __init__(self):
        super(recordedSessionFrame_View, self).__init__()
        self.setupUi(self)