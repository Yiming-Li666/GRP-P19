from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.searchStudent_frame1 import Ui_Frame

class searchStudentFrame_View(QFrame, Ui_Frame):

    def __init__(self):
        super(searchStudentFrame_View, self).__init__()
        self.setupUi(self)
    
