from resources.teacherUIPY.print_Dialog import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication


class printDialog_view(QDialog, Ui_Dialog):

    def __init__(self):
        super(printDialog_view, self).__init__()
        self.setupUi(self)

    def sortByModule(self):
        """
            Slot documentation goes here.
         """
        # TODO: not implemented yet

    def sortBySessionType(self):
        """
             Slot documentation goes here.
        """
        # TODO: not implemented yet

    def sortByStudent(self):
        """
           Slot documentation goes here.
        """
        # TODO: not implemented yet

    def sortByStartTime(self):
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def sortByEndTime(self):
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def toPrint(self):
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def toSave(self):
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = printDialog_view()
    Dialog.show()
    sys.exit(app.exec_())
