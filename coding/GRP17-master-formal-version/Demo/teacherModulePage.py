from PyQt5.QtWidgets import QMainWindow
from resources.teacherUIPY.basicStructure_mainWindow import basicStructure

class teacherModulePage(QMainWindow,basicStructure):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(MainWindow.login)

