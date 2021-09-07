# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'complete_timetable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_generateTimeTable(object):
    def setupUi(self, generateTimeTable):
        generateTimeTable.setObjectName("generateTimeTable")
        generateTimeTable.resize(560, 737)
        self.timeTableInfo = QtWidgets.QTextBrowser(generateTimeTable)
        self.timeTableInfo.setGeometry(QtCore.QRect(80, 140, 401, 511))
        self.timeTableInfo.setObjectName("timeTableInfo")
        self.startGeneration = QtWidgets.QPushButton(generateTimeTable)
        self.startGeneration.setGeometry(QtCore.QRect(90, 60, 121, 23))
        self.startGeneration.setObjectName("startGeneration")
        self.removeDuplicates = QtWidgets.QPushButton(generateTimeTable)
        self.removeDuplicates.setGeometry(QtCore.QRect(300, 60, 121, 23))
        self.removeDuplicates.setObjectName("removeDuplicates")
        self.label = QtWidgets.QLabel(generateTimeTable)
        self.label.setGeometry(QtCore.QRect(90, 110, 391, 16))
        self.label.setObjectName("label")

        self.retranslateUi(generateTimeTable)
        self.startGeneration.clicked.connect(self.generateWholeTimeTable)
        self.removeDuplicates.clicked.connect(self.eliminateDuplicates)
        QtCore.QMetaObject.connectSlotsByName(generateTimeTable)

    def retranslateUi(self, generateTimeTable):
        _translate = QtCore.QCoreApplication.translate
        generateTimeTable.setWindowTitle(_translate("generateTimeTable", "Time Table Generation"))
        self.startGeneration.setText(_translate("generateTimeTable", "Start Generation"))
        self.removeDuplicates.setText(_translate("generateTimeTable", "Remove Duplicates"))
        self.label.setText(_translate("generateTimeTable", "Please wait as the process might take few minutes."))

    def generateWholeTimeTable(self):
        import Filer
        import TimeTable
        TimeTable.createTimeTable()
        departs = list(Filer.listAllDepartments())
        for d in departs:    
            programs = list(Filer.programsOfDepartment(d))
            for p in programs:
                classes = list(Filer.classesOfProgram(d, p))
                for c in classes:
                    self.timeTableInfo.append('Generating Time Table of : Depart: %s Program: %s Class: %s'
                                              % (p,d,c))
                    TimeTable.generateTimeTable(d, p, c.split('.')[0])
                    self.timeTableInfo.append('Done!! for %s'% c)
        self.timeTableInfo.append('Time Table Generation was successfull.')

    def eliminateDuplicates(self):
        import TimeTable
        import Duplicates
        self.timeTableInfo.append('Eliminating duplicates...')
        Duplicates.duplicatesInDay(TimeTable.readTimeTable())
        self.timeTableInfo.append('Done!!')
        import View
        self.timeTableInfo.append('Making Time Table Teacher Wise...')
        View.makeTeacherViews()
        self.timeTableInfo.append('Making Time Table Room wise...')
        View.makeRoomViews()
        self.timeTableInfo.append('Making Time Table Class Wise...')
        View.makeAllClassesViews()

        
        import Filer
        '''
        f = open('%s/%s.html' % (Filer.TIME_TABLE_FOLDER,
                                 Filer.TIME_TABLE_FILE_NAME)).read()
        from PyQt5.QtPrintSupport import QPrinter
        
        printer = QPrinter()
        printer.setOutputFileName('%s/%s.pdf' % (Filer.TIME_TABLE_FOLDER,
                                 Filer.TIME_TABLE_FILE_NAME))
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setPageSize(QPrinter.A4)
        
        doc = QtGui.QTextDocument()
        doc.setHtml(f)
        doc.print_(printer)
        '''
        import sqlite3
        c = sqlite3.connect('%s/%s.db' % (Filer.TIME_TABLE_FOLDER, Filer.TIME_TABLE_FILE_NAME) )
        import TimeTable
        TimeTable.readTimeTable().to_sql('TimeTable',c)
        c.close()
        self.timeTableInfo.append('EveryThing Done.')
        
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    generateTimeTable = QtWidgets.QWidget()
    ui = Ui_generateTimeTable()
    ui.setupUi(generateTimeTable)
    generateTimeTable.show()
    sys.exit(app.exec_())

