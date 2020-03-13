from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
from resources.teacherUIPY.studentInfo_frame1 import Ui_Frame


class oneStudentFrame_view(QFrame, Ui_Frame):

    # send signal to student search page
    enterAttendancePage_SignalToPage = pyqtSignal()

    def __init__(self):
        super(oneStudentFrame_view, self).__init__()
        self.setupUi(self)

    def goAttendance(self, qModelIndex):
        # TODO: jump to the page
        print("go to " + str(qModelIndex.row()))
        self.enterSessionPage_SignalToPage.emit()

# test code
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    test = oneStudentFrame_view()
    test.show()
    sys.exit(app.exec_())