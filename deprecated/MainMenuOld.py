# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
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
        mainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        mainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainMenu)
        self.statusbar.setObjectName("statusbar")
        mainMenu.setStatusBar(self.statusbar)
        self.timeToolBar = QtWidgets.QToolBar(mainMenu)
        self.timeToolBar.setEnabled(True)
        self.timeToolBar.setMovable(True)
        self.timeToolBar.setOrientation(QtCore.Qt.Vertical)
        self.timeToolBar.setIconSize(QtCore.QSize(43, 43))
        self.timeToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.timeToolBar.setObjectName("timeToolBar")
        mainMenu.addToolBar(QtCore.Qt.RightToolBarArea, self.timeToolBar)
        self.departmentToolBar = QtWidgets.QToolBar(mainMenu)
        self.departmentToolBar.setMovable(False)
        self.departmentToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.departmentToolBar.setObjectName("departmentToolBar")
        mainMenu.addToolBar(QtCore.Qt.LeftToolBarArea, self.departmentToolBar)
        mainMenu.insertToolBarBreak(self.departmentToolBar)
        self.actionGenerateTimeTable = QtWidgets.QAction(mainMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/TimeTable/icons/generate.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGenerateTimeTable.setIcon(icon)
        self.actionGenerateTimeTable.setObjectName("actionGenerateTimeTable")
        self.actionRemoveDuplicates = QtWidgets.QAction(mainMenu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/TimeTable/icons/duplicate.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveDuplicates.setIcon(icon1)
        self.actionRemoveDuplicates.setObjectName("actionRemoveDuplicates")
        self.actionEditTimeTable = QtWidgets.QAction(mainMenu)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/TimeTable/icons/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditTimeTable.setIcon(icon2)
        self.actionEditTimeTable.setObjectName("actionEditTimeTable")
        self.actionFindClashes = QtWidgets.QAction(mainMenu)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/TimeTable/icons/clashes.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFindClashes.setIcon(icon3)
        self.actionFindClashes.setObjectName("actionFindClashes")
        self.actionCreateDepartment = QtWidgets.QAction(mainMenu)
        self.actionCreateDepartment.setObjectName("actionCreateDepartment")
        self.actionDeleteDepartment = QtWidgets.QAction(mainMenu)
        self.actionDeleteDepartment.setObjectName("actionDeleteDepartment")
        self.actionSettings = QtWidgets.QAction(mainMenu)
        self.actionSettings.setObjectName("actionSettings")
        self.actionViewAllDepartments = QtWidgets.QAction(mainMenu)
        self.actionViewAllDepartments.setObjectName("actionViewAllDepartments")
        self.actionViewAllTeachers = QtWidgets.QAction(mainMenu)
        self.actionViewAllTeachers.setObjectName("actionViewAllTeachers")
        self.actionAddTeacher = QtWidgets.QAction(mainMenu)
        self.actionAddTeacher.setObjectName("actionAddTeacher")
        self.actionDeleteTeacher = QtWidgets.QAction(mainMenu)
        self.actionDeleteTeacher.setObjectName("actionDeleteTeacher")
        self.actionEditDepartment = QtWidgets.QAction(mainMenu)
        self.actionEditDepartment.setObjectName("actionEditDepartment")
        self.actionEditTeacher = QtWidgets.QAction(mainMenu)
        self.actionEditTeacher.setObjectName("actionEditTeacher")
        self.actionCreateClass = QtWidgets.QAction(mainMenu)
        self.actionCreateClass.setObjectName("actionCreateClass")
        self.actionCreateProgram = QtWidgets.QAction(mainMenu)
        self.actionCreateProgram.setObjectName("actionCreateProgram")
        self.menubar.addAction(self.menuAbout.menuAction())
        self.timeToolBar.addAction(self.actionGenerateTimeTable)
        self.timeToolBar.addAction(self.actionRemoveDuplicates)
        self.timeToolBar.addAction(self.actionEditTimeTable)
        self.timeToolBar.addAction(self.actionFindClashes)
        self.timeToolBar.addSeparator()
        self.timeToolBar.addAction(self.actionSettings)
        self.departmentToolBar.addAction(self.actionViewAllDepartments)
        self.departmentToolBar.addAction(self.actionCreateDepartment)
        self.departmentToolBar.addAction(self.actionEditDepartment)
        self.departmentToolBar.addAction(self.actionDeleteDepartment)
        self.departmentToolBar.addSeparator()
        self.departmentToolBar.addAction(self.actionViewAllTeachers)
        self.departmentToolBar.addAction(self.actionAddTeacher)
        self.departmentToolBar.addAction(self.actionEditTeacher)
        self.departmentToolBar.addAction(self.actionDeleteTeacher)
        self.departmentToolBar.addSeparator()
        self.departmentToolBar.addAction(self.actionCreateClass)
        self.departmentToolBar.addAction(self.actionCreateProgram)

        self.retranslateUi(mainMenu)

        self.actionSettings.triggered.connect(self.showGeneralSettingsWindow)
        self.actionAddTeacher.triggered.connect(self.showAddTeacherDialog)
        self.actionCreateDepartment.triggered.connect(self.showCreateDepartmentWindow)
        self.actionCreateProgram.triggered.connect(self.showAddProgramWindow)
        self.actionCreateClass.triggered.connect(self.showCreateClassWindow)
        self.actionGenerateTimeTable.triggered.connect(self.showGenerateTimeTableWindow)
        self.actionEditTimeTable.triggered.connect(self.showEditTimeTableWindow)
        
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "Smart Time Scheduler"))
        self.menuAbout.setTitle(_translate("mainMenu", "About"))
        self.timeToolBar.setWindowTitle(_translate("mainMenu", "toolBar"))
        self.departmentToolBar.setWindowTitle(_translate("mainMenu", "toolBar"))
        self.actionGenerateTimeTable.setText(_translate("mainMenu", "Generate Time Table"))
        self.actionGenerateTimeTable.setToolTip(_translate("mainMenu", "Generates Time Table"))
        self.actionRemoveDuplicates.setText(_translate("mainMenu", "Remove Duplicates"))
        self.actionRemoveDuplicates.setToolTip(_translate("mainMenu", "Removes Duplicate Periods of a Day"))
        self.actionEditTimeTable.setText(_translate("mainMenu", "Edit Time Table"))
        self.actionEditTimeTable.setToolTip(_translate("mainMenu", "Edit Time Table"))
        self.actionFindClashes.setText(_translate("mainMenu", "Find Clashes"))
        self.actionFindClashes.setToolTip(_translate("mainMenu", "Finds Clashes in Time Table"))
        self.actionCreateDepartment.setText(_translate("mainMenu", "Create Department"))
        self.actionCreateDepartment.setToolTip(_translate("mainMenu", "Create New Department"))
        self.actionDeleteDepartment.setText(_translate("mainMenu", "Delete Department"))
        self.actionDeleteDepartment.setToolTip(_translate("mainMenu", "Deletes a Department"))
        self.actionSettings.setText(_translate("mainMenu", "Settings"))
        self.actionSettings.setToolTip(_translate("mainMenu", "Settings"))
        self.actionViewAllDepartments.setText(_translate("mainMenu", "View All Departments"))
        self.actionViewAllDepartments.setToolTip(_translate("mainMenu", "Lists all departments"))
        self.actionViewAllTeachers.setText(_translate("mainMenu", "View All Teachers"))
        self.actionViewAllTeachers.setToolTip(_translate("mainMenu", "View All Teachers"))
        self.actionAddTeacher.setText(_translate("mainMenu", "Add Teacher"))
        self.actionAddTeacher.setToolTip(_translate("mainMenu", "Add a new Teacher"))
        self.actionDeleteTeacher.setText(_translate("mainMenu", "Delete Teacher"))
        self.actionDeleteTeacher.setToolTip(_translate("mainMenu", "Delete an existing Teacher"))
        self.actionEditDepartment.setText(_translate("mainMenu", "Edit Department"))
        self.actionEditDepartment.setToolTip(_translate("mainMenu", "Edit a Department"))
        self.actionEditTeacher.setText(_translate("mainMenu", "Edit Teacher"))
        self.actionEditTeacher.setToolTip(_translate("mainMenu", "Edit a existing Teacher"))
        self.actionCreateClass.setText(_translate("mainMenu", "Create Class"))
        self.actionCreateClass.setToolTip(_translate("mainMenu", "Create a new class"))
        self.actionCreateProgram.setText(_translate("mainMenu", "Create Program"))
        self.actionCreateProgram.setToolTip(_translate("mainMenu", "Create a new Degree Program"))

    def showGeneralSettingsWindow(self):
        import GeneralSettings
        self.generalSettingsWindow = QtWidgets.QMainWindow()
        self.ui = GeneralSettings.Ui_generalSettingsWindow()
        self.ui.setupUi(self.generalSettingsWindow)
        self.generalSettingsWindow.show()

    def showAddTeacherDialog(self):        
        import AddTeacher
        self.addTeacherDialog = QtWidgets.QDialog()
        self.ui = AddTeacher.Ui_addTeacherDialog()
        self.ui.setupUi(self.addTeacherDialog)
        self.addTeacherDialog.show()
    
    def showCreateDepartmentWindow(self):

        import CreateDepartment
        self.createDepartment = QtWidgets.QMainWindow()
        self.ui = CreateDepartment.Ui_createDepartment()
        self.ui.setupUi(self.createDepartment)
        self.createDepartment.show()

    def showAddProgramWindow(self):
        import AddProgram
        self.addProgram = QtWidgets.QWidget()
        self.ui = AddProgram.Ui_addProgram()
        self.ui.setupUi(self.addProgram)
        self.addProgram.show()

    def showCreateClassWindow(self):

        import CreateClass
        self.createClass = QtWidgets.QDialog()
        self.ui = CreateClass.Ui_createClass()
        self.ui.setupUi(self.createClass)
        self.createClass.show()

    def showGenerateTimeTableWindow(self):
        import GenerateTimeTable
        self.generateTimeTable = QtWidgets.QWidget()
        self.ui = GenerateTimeTable.Ui_generateTimeTable()
        self.ui.setupUi(self.generateTimeTable)
        self.generateTimeTable.show()

    def showEditTimeTableWindow(self):
        import EditTimeTable
        self.editTimeTable = QtWidgets.QWidget()
        self.ui = EditTimeTable.Ui_editTimeTable()
        self.ui.setupUi(self.editTimeTable)
        self.editTimeTable.show()


    def showInHTML(self):
        import os
        import Filer
        os.startfile('%s/%s.html'%( Filer.TIME_TABLE_FOLDER, Filer.TIME_TABLE_FILE_NAME))
        
    def showInCSV(self):
        import os
        import Filer
        os.startfile('%s/%s.csv'%( Filer.TIME_TABLE_FOLDER, Filer.TIME_TABLE_FILE_NAME))
        


import Icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainMenu = QtWidgets.QMainWindow()
    ui = Ui_mainMenu()
    ui.setupUi(mainMenu)
    mainMenu.show()
    sys.exit(app.exec_())

