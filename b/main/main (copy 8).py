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
from EditTimeTable import Ui_editTimeTable

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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editTimeTable = QtWidgets.QWidget()
    ui = Ui_editTimeTable()
    ui.setupUi(editTimeTable)
    editTimeTable.show()
    sys.exit(app.exec_())
    '''
    
