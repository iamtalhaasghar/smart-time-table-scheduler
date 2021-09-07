# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_timetable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editTimeTable(object):
    def setupUi(self, editTimeTable):
        editTimeTable.setObjectName("editTimeTable")
        editTimeTable.resize(1070, 723)
        self.timeTable = QtWidgets.QTableWidget(editTimeTable)
        self.timeTable.setGeometry(QtCore.QRect(10, 10, 1051, 621))
        self.timeTable.setDragEnabled(True)
        self.timeTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.timeTable.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.timeTable.setAlternatingRowColors(True)
        self.timeTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.timeTable.setRowCount(20)
        self.timeTable.setColumnCount(12)
        self.timeTable.setObjectName("timeTable")
        item = QtWidgets.QTableWidgetItem()
        self.timeTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable.setHorizontalHeaderItem(1, item)
        self.loadTimeTable = QtWidgets.QPushButton(editTimeTable)
        self.loadTimeTable.setGeometry(QtCore.QRect(140, 660, 151, 31))
        self.loadTimeTable.setObjectName("loadTimeTable")
        
        self.swapPeriods = QtWidgets.QPushButton(editTimeTable)
        self.swapPeriods.setGeometry(QtCore.QRect(364, 662, 121, 31))
        self.swapPeriods.setObjectName("swapPeriods")

        self.retranslateUi(editTimeTable)
        self.loadTimeTable.clicked.connect(self.timeTable.clear)
        QtCore.QMetaObject.connectSlotsByName(editTimeTable)

    def retranslateUi(self, editTimeTable):
        _translate = QtCore.QCoreApplication.translate
        editTimeTable.setWindowTitle(_translate("editTimeTable", "Edit Time Table"))
        item = self.timeTable.verticalHeaderItem(0)
        item.setText(_translate("editTimeTable", "One"))
        item = self.timeTable.horizontalHeaderItem(0)
        item.setText(_translate("editTimeTable", "Day"))
        item = self.timeTable.horizontalHeaderItem(1)
        item.setText(_translate("editTimeTable", "Room"))
        self.loadTimeTable.setText(_translate("editTimeTable", "Load Time Table"))
        self.swapPeriods.setText(_translate("editTimeTable", "Swap Periods"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editTimeTable = QtWidgets.QWidget()
    ui = Ui_editTimeTable()
    ui.setupUi(editTimeTable)
    editTimeTable.show()
    sys.exit(app.exec_())

