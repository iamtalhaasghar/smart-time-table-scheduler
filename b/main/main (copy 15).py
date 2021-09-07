import os
import sys
sys.path.append(os.getcwd()+'/codefiles')
sys.path.append(os.getcwd()+'/guifiles')

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import GeneralSettings

'''
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    generalSettingsWindow = QMainWindow()
    ui = GeneralSettings.Ui_generalSettingsWindow()
    ui.setupUi(generalSettingsWindow)
    generalSettingsWindow.show()
    sys.exit(app.exec_())

'''
import Room
import Semester
import TimeTable
import Timing
import Lab
import Teacher
import Filer

'''
Room.addRooms()
Lab.makeLabs()
Teacher.addTeachers()

Semester.makeClass()
Semester.makeClass()
Semester.makeClass()
'''
TimeTable.createTimeTable()

TimeTable.generateTimeTable('CS1B')
TimeTable.generateTimeTable('CS2B')
TimeTable.generateTimeTable('CS3B')

table = TimeTable.readTimeTable()

table.to_html('timetables/TimeTable.html')

'''
import duplicates
table = TimeTable.readTimeTable()
duplicates.duplicatesInDay(table)
table.to_html('timetables/TimeTable.html')
'''
