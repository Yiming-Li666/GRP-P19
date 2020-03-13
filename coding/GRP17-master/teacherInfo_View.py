from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.teacherInfo_frame1 import Ui_Frame
import sys


class teacherInfo_view(QFrame, Ui_Frame):

    def __init__(self):
        # setup UI
        super(teacherInfo_view, self).__init__()
        self.setupUi(self)


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.resize(1000,500)

    frame1 = QFrame(mainWindow)
    frame1.setGeometry(QtCore.QRect(400, 30, 300, 400))

    test = teacherInfo_view()
    test.setupUi(frame1)

    mainWindow.show()

    sys.exit(app.exec_())