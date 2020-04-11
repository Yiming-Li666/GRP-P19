from resources.teacherUIPY.print_Dialog import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.Qt import *
from PyQt5 import QtCore
import basicMainWindow_Ctr
import dbController
import csv

class printDialog_view(QDialog, Ui_Dialog):

    def __init__(self):
        super(printDialog_view, self).__init__()
        self.setupUi(self)

    def sort(self):
        sessionList = []
        printDialogModel = QStringListModel()
        if self.module_comboBox.currentText() == 'Module' and self.sessionType_comboBox.currentText() == 'Session Type':
            data = dbController.GetSession()
        elif self.module_comboBox.currentText() != 'Module' and self.sessionType_comboBox.currentText() == 'Session Type':
            data = dbController.GetSessionByModule(self.module_comboBox.currentText())
        elif self.module_comboBox.currentText() == 'Module' and self.sessionType_comboBox.currentText() != 'Session Type':
            data = dbController.GetSessionByType(str.lower(self.sessionType_comboBox.currentText()))
        else:
            data = dbController.GetSessionByBoth(self.module_comboBox.currentText(),str.lower(self.sessionType_comboBox.currentText()))
        for session in data:
            sessionList.append(session[0] + " " + session[1])
        printDialogModel.setStringList(sessionList)
        self.listView.setModel(printDialogModel)
        #if self.module_comboBox.currentText() = 'Module'
        #self.module_comboBox.currentText()
        #self.sessionType_comboBox.currentText() = 'Session Type'
        print("sort")

    def sortByStudent(self):
        """
           Slot documentation goes here.
        """
        # TODO: not implemented yet

    def sortByStartTime(self):
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def sortByEndTime(self):
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def toPrint(self):
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def toSave(self):
        print(basicMainWindow_Ctr.basicMainWindow_Ctr.sessionList)
        selected = self.listView.selectedIndexes()
        rowNum = selected[0].row()
        s = basicMainWindow_Ctr.basicMainWindow_Ctr.sessionList[rowNum].split()
        data = dbController.GetSessionAttendance(s[0],s[1])
        with open('/Users/liyiming/Desktop/GRP/GRP-P19/SavedFile/' + s[0] + s[1] + '.csv', 'w', newline='') as t_file:
            csv_writer = csv.writer(t_file)
            attribute = ['ModuleId','lessonId','studentId','isAttend','AttendTime']
            csv_writer.writerow(attribute)
            for l in data:
                csv_writer.writerow(l)
        print("saved!")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = printDialog_view()
    Dialog.show()
    sys.exit(app.exec_())
