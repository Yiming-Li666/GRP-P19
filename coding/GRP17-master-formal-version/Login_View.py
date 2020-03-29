from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from resources.teacherUIPY.login_mainWindow import login_MainWindow
import sys
import dbController
from CommonHelper import CommonHelper

class login_View(QMainWindow, login_MainWindow):

    # send signals to login controller to operate
    userId = ''
    login_Signal = pyqtSignal(int)
    forgetPwd_Signal = pyqtSignal()

    def __init__(self):
        # setup UI
        super(login_View, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.toolButton.clicked.connect(self.forgetPwd)
        # self.lineEdit_2.password()

    def login(self):
        global userId
        userId = self.lineEdit.text()
        userPsw = self.lineEdit_2.text()
        if(userId != '' and  userPsw!= ''):
            #self.hintLabel.setText("loading...")
            if(dbController.CheckLogin(userId,userPsw)):
                # if condition: userid not in teacher, emit 1
                if dbController.CheckAdmin(userId):
                    self.login_Signal.emit(1)
                else:
                    moduleName = self.checkModule(userId)
                    '''
                    for r in moduleName:
                        ModuleFrame1_Model.__init__()
                        ModuleFrame1_Model.listItemData.addItem(moduleName[r][2])
                    '''
                    self.login_Signal.emit(0)
        self.hintLabel.setText("Invalid username or password!")
        

    def forgetPwd(self):
        #self.forgetPwd_Signal.emit()
        print("forget")
        self.hintLabel.setText("Please contact the admin! 188-8888-8888")

    def checkModule(self,userId):
        #print(userId)
        d = dbController.GetTeacherInfo(userId)
        #print(d)
        return d
    

# test code for the single view
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = login_View()
    mainWindow.show()
    CommonHelper.readQSS("resources/qss/login.qss",app)
    sys.exit(app.exec_())
