import os
import sys
sys.path.append(os.getcwd()+'/codefiles')
sys.path.append(os.getcwd()+'/guifiles')

from PyQt5 import QtCore,QtWidgets,QtGui
import GeneralSettings
from AddTeacherDialog import Ui_addTeacherDialog
from CreateDepartment import Ui_createDepartment
import Room
import Semester
import TimeTable
import Timing
import Lab
import Teacher
import Filer
import View

'''

if __name__ == "__main__":

    
    app = QtWidgets.QApplication(sys.argv)
    generalSettingsWindow = QtWidgets.QMainWindow()
    ui = GeneralSettings.Ui_generalSettingsWindow()
    ui.setupUi(generalSettingsWindow)
    generalSettingsWindow.show()
    app.exec_()


    appN = QtWidgets.QApplication(sys.argv)
    addTeacherDialog = QtWidgets.QDialog()
    ui = Ui_addTeacherDialog()
    ui.setupUi(addTeacherDialog)
    addTeacherDialog.show()
    appN.exec_()

    
       
    appT = QtWidgets.QApplication(sys.argv)
    createDepartment = QtWidgets.QDialog()
    ui = Ui_createDepartment()
    ui.setupUi(createDepartment)
    createDepartment.show()
    appT.exec_()




TimeTable.createTimeTable()

TimeTable.generateTimeTable('CS1B')
TimeTable.generateTimeTable('CS2B')
table = TimeTable.readTimeTable()
table.to_html('timetables/TimeTable.html')
'''
import Duplicates
table = TimeTable.readTimeTable()
Duplicates.duplicatesInDay(table)
table.to_html('timetables/TimeTable.html')
'''
View.makeTeacherViews()
View.makeRoomViews()
'''
