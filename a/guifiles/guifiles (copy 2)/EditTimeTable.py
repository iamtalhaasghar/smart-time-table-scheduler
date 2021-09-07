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
        self.timeTable.setRowCount(1)
        self.timeTable.setColumnCount(1)
        self.timeTable.setObjectName("timeTable")

        self.setPeriodHeaders()


        self.loadTimeTable = QtWidgets.QPushButton(editTimeTable)
        self.loadTimeTable.setGeometry(QtCore.QRect(140, 660, 151, 31))
        self.loadTimeTable.setObjectName("loadTimeTable")

        self.swapPeriods = QtWidgets.QPushButton(editTimeTable)
        self.swapPeriods.setGeometry(QtCore.QRect(364, 662, 121, 31))
        self.swapPeriods.setObjectName("swapPeriods")

        
        self.retranslateUi(editTimeTable)
        self.loadTimeTable.clicked.connect(self.showTimeTable)
        self.swapPeriods.clicked.connect(self.interchangePeriods)
        QtCore.QMetaObject.connectSlotsByName(editTimeTable)

    def retranslateUi(self, editTimeTable):
        _translate = QtCore.QCoreApplication.translate
        editTimeTable.setWindowTitle(_translate("editTimeTable", "Edit Time Table"))
        self.loadTimeTable.setText(_translate("editTimeTable", "Load Time Table"))
        self.swapPeriods.setText(_translate("editTimeTable", "Swap Periods"))


        
    def showTimeTable(self):
        import sqlite3
        connection = sqlite3.connect('MasterTimeTable.db')
        query = "SELECT * FROM TimeTable"
        result = connection.execute(query)
        self.timeTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.timeTable.insertRow(row_number)
            for colmun_number, data in enumerate(row_data):
                self.timeTable.setItem(row_number, colmun_number,
                    QtWidgets.QTableWidgetItem(str(data)))

                    
        connection.close()

    def setPeriodHeaders(self):
        
        import TimeTable
        times = TimeTable.readTimeHeaders()
        times.pop(0)
        self.timeTable.setColumnCount(len(times) + 2)
        
        item = QtWidgets.QTableWidgetItem('Days')
        self.timeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem('Rooms')
        self.timeTable.setHorizontalHeaderItem(1, item)
        p = 1
        for i in range(2,self.timeTable.columnCount()+1):
            temp = QtWidgets.QTableWidgetItem('P%s'%p)
            self.timeTable.setHorizontalHeaderItem(i,temp)
            p += 1

    def interchangePeriods(self):
        periods = self.timeTable.selectedItems()
        temp = periods[0].data(0)
        periods[0].setData(0,periods[1].data(0))
        periods[1].setData(0,temp)
        

'''        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editTimeTable = QtWidgets.QWidget()
    ui = Ui_editTimeTable()
    ui.setupUi(editTimeTable)
    editTimeTable.show()
    sys.exit(app.exec_())
'''
