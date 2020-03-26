from PyQt5.QtCore import QAbstractListModel, QVariant, QModelIndex, Qt
from PyQt5.QtGui import QFont


class searchStudentFrame_model(QAbstractListModel):

    def __init__(self,parent=None):
        super(searchStudentFrame_model,self).__init__(parent)
        self.init_data()

    def init_data(self):
        self.listItemData = ["Student1"]
        # TODO: build the module data

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractListModel.flags(self, index) |
                            Qt.ItemIsEditable)

    def data(self, index, role):
        if index.isValid() or (0 <= index.row() < len(self.listItemData)):
            if role == Qt.DisplayRole:
                return QVariant(self.listItemData[index.row()])
            elif role == Qt.TextAlignmentRole:
                return QVariant(int(Qt.AlignLeft| Qt.AlignVCenter))
            elif role == Qt.FontRole:
                font = QFont()
                font.setPixelSize(20)
                return QVariant(font)
        else:
            return QVariant()

    def rowCount(self, parent=QModelIndex()):
        return len(self.listItemData)