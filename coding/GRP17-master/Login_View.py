from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from resources.teacherUIPY.login_mainWindow import login_MainWindow
import sys


class login_View(QMainWindow, login_MainWindow):

    # send signals to login controller to operate
    login_Signal = pyqtSignal()
    forgetPwd_Signal = pyqtSignal()

    def __init__(self):
        # setup UI
        super(login_View, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.toolButton.clicked.connect(self.forgetPwd)

        # hintLabel
        # TODO: provide login hint for user
        self.hintLabel.setText(" Login ? ")

    def login(self):
        print("login")
        self.login_Signal.emit()

    def forgetPwd(self):
        self.forgetPwd_Signal.emit()



# test code for the single view
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = login_View()
    mainWindow.show()
    sys.exit(app.exec_())