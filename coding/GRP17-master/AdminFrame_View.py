from PyQt5.QtWidgets import QFrame, QApplication
from resources.teacherUIPY.admin_totalFrame import Ui_Frame
import sys


class adminFrame_view(QFrame, Ui_Frame):

    def __init__(self):
        # setup UI
        super(adminFrame_view, self).__init__()
        self.setupUi(self)

    # please refer to names in PYUI files. E.g. ATT - attendance, STU - student.
    def setSlot(self):
        # TODO: set slots there or in PY
        pass


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    test = adminFrame_view()
    test.show()
    sys.exit(app.exec_())