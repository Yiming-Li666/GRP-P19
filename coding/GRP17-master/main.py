from PyQt5.Qt import *
from Login_View import login_View
from Login_ctr import login_Ctr
import sys

# The entry of program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = login_View()
    loginCtr = login_Ctr()
    loginCtr.setView(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())