from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.studentInfo_frame1 import Ui_Frame

class oneStudentFrame_View(QFrame, Ui_Frame):

    def __init__(self):
        super(oneStudentFrame_View, self).__init__()
        self.setupUi(self)