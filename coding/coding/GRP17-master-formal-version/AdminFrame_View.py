from PyQt5.QtWidgets import QFrame, QApplication
from resources.teacherUIPY.admin_totalFrame import Ui_Frame
import sys
from CommonHelper import CommonHelper

class adminFrame_view(QFrame, Ui_Frame):

    def __init__(self):
        # setup UI
        super(adminFrame_view, self).__init__()
        self.setupUi(self)

    # please refer to names in PYUI files. E.g. ATT - attendance, STU - student.
    def setSlot(self):
        # TODO: set slots there or in PY
        pass
    
    def Account(self):
        self.stackedWidget.setCurrentIndex(0)
    def Student(self):
        self.stackedWidget.setCurrentIndex(1)
    def Teacher(self):
        self.stackedWidget.setCurrentIndex(2)
    def Module(self):
        self.stackedWidget.setCurrentIndex(3)
    def Attendance(self):
        self.stackedWidget.setCurrentIndex(4)


    def AccountSearch(self):
        print("AccountSearch")
    def StudentSearch(self):
        print("StudentSearch")
    def TeacherSearch(self):
        print("TeacherSearch")
    def ModuleSearch(self):
        print("ModuleSearch")
    def AttendanceSearch(self):
        print("AttendanceSearch")
    
    def AccountModify(self):
        print("AccountModify")
    def StudentModify(self):
        print("StudentModify")
    def TeacherModify(self):
        print("TeacherModify")
    def ModuleModify(self):
        print("ModuleModify")
    def AttendanceModify(self):
        print("AttendanceModify")

    def AccountDelete(self):
        print("AccountDelete")
    def StudentDelete(self):
        print("StudentDelete")
    def TeacherDelete(self):
        print("TeacherDelete")
    def ModuleDelete(self):
        print("ModuleDelete")
    def AttendanceDelete(self):
        print("AttendanceDelete")

    def AccountAdd(self):
        print("AccountAdd")
    def StudentAdd(self):
        print("StudentAdd")
    def TeacherAdd(self):
        print("TeacherAdd")
    def ModuleAdd(self):
        print("ModuleAdd")
    def AttendanceAdd(self):
        print("AttendanceAdd")

# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    test = adminFrame_view()
    test.show()
    CommonHelper.readQSS("resources/qss/AdminFrame.qss",app)
    sys.exit(app.exec_())