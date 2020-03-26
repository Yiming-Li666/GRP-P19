from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.studentRecord_frame import studentRecord_frame
import sys

class studentRecordFrame_View(QFrame, studentRecord_frame):
    modifyDialog_Signal = pyqtSignal()
    def __init__(self):
        super(studentRecordFrame_View, self).__init__()
        self.setupUi(self)
    
    def modifyState(self):
        print("modify")
        self.modifyDialog_Signal.emit()