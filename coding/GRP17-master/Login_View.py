from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from resources.teacherUIPY.login_mainWindow import login_MainWindow
from CommonHelper import CommonHelper
import sys
import dbController


class login_View(QMainWindow, login_MainWindow):
    # send signals to login controller to operate
    userId = ''
    login_Signal = pyqtSignal()
    forgetPwd_Signal = pyqtSignal()

    def __init__(self):
        # setup UI
        super(login_View, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.toolButton.clicked.connect(self.forgetPwd)

    def login(self):
        global userId
        userId = self.lineEdit.text()
        userPsw = self.lineEdit_2.text()
        if(userId != '' and  userPsw!= ''):
            #self.hintLabel.setText("loading...")
            if(dbController.CheckLogin(userId,userPsw)):
                self.login_Signal.emit()
        self.hintLabel.setText("Invalid username or password!")

    def forgetPwd(self):
        self.forgetPwd_Signal.emit()
        print("forget")
        self.hintLabel.setText("Please contact the admin! 188-8888-8888")


# test code for the single view
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = login_View()
    mainWindow.show()
    CommonHelper.readQSS("resources/qss/login.qss",app)
    sys.exit(app.exec_())