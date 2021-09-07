# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.editSettings = QtWidgets.QPushButton(self.centralwidget)
        self.editSettings.setGeometry(QtCore.QRect(120, 60, 75, 23))
        self.editSettings.setObjectName("editSettings")
        self.addTeachers = QtWidgets.QPushButton(self.centralwidget)
        self.addTeachers.setGeometry(QtCore.QRect(330, 60, 75, 23))
        self.addTeachers.setObjectName("addTeachers")
        mainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        mainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainMenu)
        self.statusbar.setObjectName("statusbar")
        mainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(mainMenu)
        self.addTeachers.clicked.connect(self.showAddTeachers)
        self.editSettings.clicked.connect(self.showEditGeneralSettings)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "Smart Time Scheduler"))
        self.editSettings.setText(_translate("mainMenu", "Edit Settings"))
        self.addTeachers.setText(_translate("mainMenu", "Add Teachers"))

    def showEditGeneralSettings(self):
        import sys
        import GeneralSettings
        
        uiF = GeneralSettings.Ui_generalSettingsWindow() 
        uiF.setupUi(mainMenu)
        
    def showAddTeachers(self):
        import AddTeacherDialog
        uiT = AddTeacherDialog.Ui_addTeacherDialog()
        uiT.setupUi(mainMenu)
'''    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainMenu = QtWidgets.QMainWindow()
    ui = Ui_mainMenu()
    ui.setupUi(mainMenu)
    mainMenu.show()
    sys.exit(app.exec_())
'''

