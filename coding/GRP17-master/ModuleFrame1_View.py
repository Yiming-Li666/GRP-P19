from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QApplication
from resources.teacherUIPY.basicStructure_frame1 import Ui_Frame
import sys

#test
from ModuleFrame1_Model import moduleFrame1_Model
from ModuleFrame_Delegate import moduleFrame_Deletagte


class moduleFrame1_view(QFrame, Ui_Frame):

    # send signal to module page
    enterSessionPage_SignalToPage = pyqtSignal()

    def __init__(self):
        # setup UI
        super(moduleFrame1_view, self).__init__()
        self.setupUi(self)

    def refresh(self):
        self.frameName_TBS.setText("Module")
        self.search_lineEdit.hide()
        self.search_toolButton.hide()
        self.addButton.hide()
        self.listView.doubleClicked.connect(self.doubleClicked)
        self.listView.clicked.connect(self.goSession)

    def goSession(self, qModelIndex):
        # TODO: jump to the page
        print("go to " + str(qModelIndex.row()))
        self.enterSessionPage_SignalToPage.emit()


    def doubleClicked(self, qModelIndex):
        print("you choosed " + str(qModelIndex.row()))

    def print(self):
        print("print recording")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def showNum(self):
        print("edit show Num")
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

    def sort(self):
        print("sort")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    test = moduleFrame1_view()
    delegate = moduleFrame_Deletagte()
    model = moduleFrame1_Model()
    test.listView.setModel(model)
    test.listView.setItemDelegateForRow(0,delegate)
    test.show()
    sys.exit(app.exec_())