import sys

from PyQt5.Qt import *
from Demo.teacherModule_pane import Ui_MainWindow


class teacherModule_Pane(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def login(self):
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = teacherModule_Pane()
    mainWindow.show()
    sys.exit(app.exec_())