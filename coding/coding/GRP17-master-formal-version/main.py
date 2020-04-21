from PyQt5.Qt import *
from Login_View import login_View
from Login_ctr import login_Ctr
import sys
from CommonHelper import CommonHelper

# The entry of program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = login_View()
    loginCtr = login_Ctr()
    loginCtr.setView(loginWindow)
    CommonHelper.readQSS("/Users/liyiming/Desktop/GRP/GRP-P19/coding/coding/GRP17-master-formal-version/resources/qss/login.qss",app)
    loginWindow.show()
    sys.exit(app.exec_())