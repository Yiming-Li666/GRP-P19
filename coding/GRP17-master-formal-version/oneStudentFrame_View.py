from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
from resources.teacherUIPY.studentInfo_frame1 import Ui_Frame
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from CommonHelper import CommonHelper
from oneStudentFrame_Model import oneStudentFrame_model
from searchResult_Ctr import searchResult_Ctr

class oneStudentFrame_view(QFrame, Ui_Frame):

    # send signal to student search page
    enterAttendancePage_SignalToPage = pyqtSignal()

    def __init__(self):
        super(oneStudentFrame_view, self).__init__()
        self.setupUi(self)
    
    def refresh(self):
        print("connect")
        self.attendance_listView.clicked.connect(self.goAttendance)
        
    def goAttendance(self, qModelIndex):
        # TODO: jump to the page
        #print("go to " + str(qModelIndex.row()))
        self.enterAttendancePage_SignalToPage.emit()

    def sortByModule(self):
        #print(self.comboBox.currentText())
        #TODO
        self.studentAttendanceModel = oneStudentFrame_model()
        for sa in searchResult_Ctr.studentAttend:
            if sa[0] == self.comboBox.currentText():
                if sa[3] == 1:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  " + str(sa[4]))
                else:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  absent")
        self.attendance_listView.setModel(self.studentAttendanceModel)

    def sortBySession(self):
        #print(self.comboBox_2.currentText())
        #TODO
        print("2")

    def sortAttendance(self):
        #print(self.comboBox_5.currentText())
        #TODO
        self.studentAttendanceModel = oneStudentFrame_model()
        if self.comboBox_5.currentText() == 'Attendance':
            for sa in searchResult_Ctr.studentAttend:
                if sa[3] == 1:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  " + str(sa[4]))
                else:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  absent")
        elif self.comboBox_5.currentText() == 'Attended':
            for sa in searchResult_Ctr.studentAttend:
                if sa[3] == 1:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  " + str(sa[4]))
        else:
            for sa in searchResult_Ctr.studentAttend:
                if sa[3] == 0:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  absent")
        self.attendance_listView.setModel(self.studentAttendanceModel)

# test code
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    test = oneStudentFrame_view()
    test.show()
    CommonHelper.readQSS("resources/qss/oneStudentFrame.qss",app)
    sys.exit(app.exec_())