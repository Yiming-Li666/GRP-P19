from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow, QListView
from resources.teacherUIPY.upcomingEvents_frame2 import upcomingEvents_frame2
from upcomingEvent_Model import upcomingEvent_Model
import sys


class upcomingEvent_view(QFrame, upcomingEvents_frame2):

    def __init__(self):
        # setup UI
        super(upcomingEvent_view, self).__init__()
        self.setupUi(self)

    def editShowNum(self):
        print("edit show num")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def leftPage(self):
        print("left page")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def rightPage(self):
        print("right page")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.resize(1000,500)

    frame1 = QFrame(mainWindow)
    frame1.setGeometry(QtCore.QRect(400, 30, 300, 400))

    test = upcomingEvent_view()
    test.setupUi(frame1)
    model = upcomingEvent_Model()
    test.listView_2.setModel(model)

    mainWindow.show()

    sys.exit(app.exec_())