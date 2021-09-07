import os
import sys
sys.path.append(os.getcwd()+'/codefiles')
sys.path.append(os.getcwd()+'/guifiles')

from PyQt5 import QtCore,QtWidgets,QtGui

from MainMenu import Ui_mainMenu
import Room
import Semester
import TimeTable
import Timing
import Lab
import Teacher
import Filer
import View
import Duplicates

Filer.createSettingsFolder()
Filer.createDataFolder()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainMenu = QtWidgets.QMainWindow()
    ui = Ui_mainMenu()
    ui.setupUi(mainMenu)
    mainMenu.show()
    sys.exit(app.exec_())

'''
TimeTable.createTimeTable()

TimeTable.generateTimeTable('CS','BSCS','CS1B')
table = TimeTable.readTimeTable()
Duplicates.duplicatesInDay(table)
#table.to_html('timetables/TimeTable.html')

TimeTable.generateTimeTable('CS2B')
table = TimeTable.readTimeTable()
table.to_html('timetables/TimeTable.html')




View.makeTeacherViews()
View.makeRoomViews()
'''
