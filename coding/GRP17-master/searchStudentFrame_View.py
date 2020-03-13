from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame
from resources.teacherUIPY.basicStructure_frame1 import Ui_Frame
from searchStudentFrame_Model import searchStudentFrame_model

class searchStudentFrame_view(QFrame, Ui_Frame):

    # send signal to module page
    enterStudentPage_SignalToPage = pyqtSignal()

    def __init__(self):
        super(searchStudentFrame_view, self).__init__()
        self.setupUi(self)

    def refresh(self):
        self.addButton.hide()

        self.frameName_TBS.setText("Student Name")

        self.listView.clicked.connect(self.goToStudent)

    def goToStudent(self, qModelIndex):
        # TODO: jump to the page
        print("go to " + str(qModelIndex.row()))
        self.enterStudentPage_SignalToPage.emit()

    def sort(self):
        print("sort")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

# test code
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    test = searchStudentFrame_view()
    model = searchStudentFrame_model()
    test.listView.setModel(model)
    test.show()
    sys.exit(app.exec_())
