import os
import sys
sys.path.append(os.getcwd()+'/codefiles')
sys.path.append(os.getcwd()+'/guifiles')

from PyQt5 import QtCore,QtWidgets,QtGui

from MainMenu import Ui_mainMenu
from EditTimeTable import Ui_editTimeTable
import Filer
Filer.createDataFolder()
Filer.createSettingsFolder()

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainMenu = QtWidgets.QMainWindow()
    ui = Ui_mainMenu()
    ui.setupUi(mainMenu)
    mainMenu.show()
    sys.exit(app.exec_())

    
