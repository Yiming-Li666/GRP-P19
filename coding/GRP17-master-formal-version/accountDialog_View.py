from resources.teacherUIPY.account_Dialog import accountDialog
from PyQt5.QtWidgets import QDialog, QApplication


class accountDialog_view(QDialog, accountDialog):

    def __init__(self):
        super(accountDialog_view, self).__init__()
        self.setupUi(self)





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = accountDialog_view()
    Dialog.show()
    sys.exit(app.exec_())
