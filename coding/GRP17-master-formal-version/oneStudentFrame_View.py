from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
from resources.teacherUIPY.studentInfo_frame1 import Ui_Frame
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from CommonHelper import CommonHelper
from oneStudentFrame_Model import oneStudentFrame_model
from searchResult_Ctr import searchResult_Ctr
import sessionPage_View
import sessionFrame1_View
import dbController

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

    def sort(self):
        searchResult_Ctr.studentAttend.clear()
        self.studentAttendanceModel = oneStudentFrame_model()
        
        if self.comboBox.currentText() != 'Module Name':
            # sort by module
            if self.comboBox_2.currentText() == 'Session Type' and self.comboBox_5.currentText() == 'Attendance':
                studentDetail = dbController.GetStudentInfo(searchResult_Ctr.IdName[0])
                self.sortByModule(studentDetail)
            # sort by module and Session Type
            elif self.comboBox_2.currentText() != 'Session Type' and self.comboBox_5.currentText() == 'Attendance':
                studentDetail = dbController.GetStudentInfoLesson(searchResult_Ctr.IdName[0],str.lower(self.comboBox_2.currentText()))
                self.sortByModule(studentDetail)
            # sort by module and Attendance
            elif self.comboBox_2.currentText() == 'Session Type' and self.comboBox_5.currentText() != 'Attendance':
                if self.comboBox_5.currentText() == 'Attended':
                    studentDetail = dbController.GetStudentInfoAttend(searchResult_Ctr.IdName[0], 1)
                else:
                    studentDetail = dbController.GetStudentInfoAttend(searchResult_Ctr.IdName[0], 0)
                self.sortByModule(studentDetail)
            # sort by all
            else:
                if self.comboBox_5.currentText() == 'Attended':
                    studentDetail = dbController.GetStudentInfoLessonAttend(searchResult_Ctr.IdName[0], str.lower(self.comboBox_2.currentText()), 1)
                else:
                    studentDetail = dbController.GetStudentInfoLessonAttend(searchResult_Ctr.IdName[0], str.lower(self.comboBox_2.currentText()), 1)
                self.sortByModule(studentDetail)
        else:
            # do not sort
            if self.comboBox_2.currentText() == 'Session Type' and self.comboBox_5.currentText() == 'Attendance':
                studentDetail = dbController.GetStudentInfo(searchResult_Ctr.IdName[0])
                self.sortNothing(studentDetail)
            # sort by session type
            elif self.comboBox_2.currentText() != 'Session Type' and self.comboBox_5.currentText() == 'Attendance':
                studentDetail = dbController.GetStudentInfoLesson(searchResult_Ctr.IdName[0],str.lower(self.comboBox_2.currentText()))
                self.sortNothing(studentDetail)
            # sort by attendance
            elif self.comboBox_2.currentText() == 'Session Type' and self.comboBox_5.currentText() != 'Attendance':
                if self.comboBox_5.currentText() == 'Attended':
                    studentDetail = dbController.GetStudentInfoAttend(searchResult_Ctr.IdName[0], 1)
                else:
                    studentDetail = dbController.GetStudentInfoAttend(searchResult_Ctr.IdName[0], 0)
                self.sortNothing(studentDetail)
            # sort by session type and attendance
            else:
                if self.comboBox_5.currentText() == 'Attended':
                    studentDetail = dbController.GetStudentInfoLessonAttend(searchResult_Ctr.IdName[0], str.lower(self.comboBox_2.currentText()), 1)
                else:
                    studentDetail = dbController.GetStudentInfoLessonAttend(searchResult_Ctr.IdName[0], str.lower(self.comboBox_2.currentText()), 0)
                self.sortNothing(studentDetail)
        self.attendance_listView.setModel(self.studentAttendanceModel)

    def sortNothing(self, studentDetail):
        for s in studentDetail:
            searchResult_Ctr.studentAttend.append(s)
            if s[3] == 1:
                self.studentAttendanceModel.listItemData.append(s[0] + "  " + s[1] + "  " + str(s[4]))
            else:
                self.studentAttendanceModel.listItemData.append(s[0] + "  " + s[1] + "  absent")

    def sortByModule(self,studentDetail):
        for s in studentDetail:
            if self.comboBox.currentText() == s[0]:
                searchResult_Ctr.studentAttend.append(s)
                if s[3] == 1:
                    self.studentAttendanceModel.listItemData.append(s[0] + "  " + s[1] + "  " + str(s[4]))
                else:
                    self.studentAttendanceModel.listItemData.append(s[0] + "  " + s[1] + "  absent")
    '''
    def sortBySession(self):
        # Lecture Tutorial Lab/Seminar
        self.studentAttendanceModel = oneStudentFrame_model()
        for sa in searchResult_Ctr.studentAttend:
            moduleId = sa[0]
            lessonId = sa[1]
            sessionType = dbController.GetSessionType(moduleId, lessonId)
            if str.lower(sessionType[0][0]) == str.lower(self.comboBox_2.currentText()):
                if sa[3] == 1:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  " + str(sa[4]))
                else:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  absent")
        if self.comboBox_2.currentText() == 'Session Type':
            for sa in searchResult_Ctr.studentAttend:
                if sa[3] == 1:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  " + str(sa[4]))
                else:
                    self.studentAttendanceModel.listItemData.append(sa[0] + "  " + sa[1] + "  absent")
        self.attendance_listView.setModel(self.studentAttendanceModel)

    def sortAttendance(self):
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
    '''
# test code
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    test = oneStudentFrame_view()
    test.show()
    CommonHelper.readQSS("resources/qss/oneStudentFrame.qss",app)
    sys.exit(app.exec_())