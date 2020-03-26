from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate, QWidget

from lineWidget_View import lineWidget


class moduleFrame_Deletagte(QStyledItemDelegate):

    def __init__(self,parent=None):
        QStyledItemDelegate.__init__(self,parent)

    def createEditor(self, parent: QWidget,
                     option: 'QStyleOptionViewItem',
                     index: QtCore.QModelIndex) :
        # edit the lineWidget for module page
        editor = lineWidget(parent)
        editor.toolButton_8.hide()
        editor.toolButton_9.hide()

        # TODO: implementation of buttons on editor
        # editor.toolButton_10.clicked.connect(editor.enterEvent())
        return editor

    # load data to editor from model
    def setEditorData(self, editor: lineWidget, index: QtCore.QModelIndex):
        value = index.model().data(index, Qt.DisplayRole)
        editor.lineEdit.setText(str(value.value()))

    # load data to model from editor
    def setModelData(self, editor: lineWidget, model, index):
        model.setData(index,editor.lineEdit.text())

    # set geometry for editor
    def updateEditorGeometry(self, editor: lineWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex):
        editor.setGeometry(option.rect)
