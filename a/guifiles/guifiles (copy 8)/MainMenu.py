# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(578, 376)
        self.centralwidget = QtWidgets.QWidget(mainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.generalSettings = QtWidgets.QPushButton(self.centralwidget)
        self.generalSettings.setGeometry(QtCore.QRect(50, 60, 131, 31))
        self.generalSettings.setObjectName("generalSettings")
        self.createDepartment = QtWidgets.QPushButton(self.centralwidget)
        self.createDepartment.setGeometry(QtCore.QRect(50, 120, 131, 31))
        self.createDepartment.setObjectName("createDepartment")
        self.viewRooms = QtWidgets.QPushButton(self.centralwidget)
        self.viewRooms.setGeometry(QtCore.QRect(220, 60, 131, 31))
        self.viewRooms.setObjectName("viewRooms")
        self.viewDepartments = QtWidgets.QPushButton(self.centralwidget)
        self.viewDepartments.setGeometry(QtCore.QRect(220, 120, 131, 31))
        self.viewDepartments.setObjectName("viewDepartments")
        self.viewTeachers = QtWidgets.QPushButton(self.centralwidget)
        self.viewTeachers.setGeometry(QtCore.QRect(220, 180, 131, 31))
        self.viewTeachers.setObjectName("viewTeachers")
        self.createClass = QtWidgets.QPushButton(self.centralwidget)
        self.createClass.setGeometry(QtCore.QRect(400, 120, 131, 31))
        self.createClass.setObjectName("createClass")
        self.createNewProgram = QtWidgets.QPushButton(self.centralwidget)
        self.createNewProgram.setGeometry(QtCore.QRect(50, 180, 131, 31))
        self.createNewProgram.setObjectName("createNewProgram")
        self.addRooms = QtWidgets.QPushButton(self.centralwidget)
        self.addRooms.setGeometry(QtCore.QRect(400, 60, 131, 31))
        self.addRooms.setObjectName("addRooms")
        self.addTeachers = QtWidgets.QPushButton(self.centralwidget)
        self.addTeachers.setGeometry(QtCore.QRect(400, 180, 131, 31))
        self.addTeachers.setObjectName("addTeachers")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 131, 16))
        self.label.setObjectName("label")
        self.generateTimeTable = QtWidgets.QPushButton(self.centralwidget)
        self.generateTimeTable.setGeometry(QtCore.QRect(50, 240, 131, 31))
        self.generateTimeTable.setObjectName("generateTimeTable")
        self.viewTimeTableHtml = QtWidgets.QPushButton(self.centralwidget)
        self.viewTimeTableHtml.setGeometry(QtCore.QRect(220, 240, 131, 31))
        self.viewTimeTableHtml.setObjectName("viewTimeTableHtml")
        self.viewTimeTableExcel = QtWidgets.QPushButton(self.centralwidget)
        self.viewTimeTableExcel.setGeometry(QtCore.QRect(400, 240, 131, 31))
        self.viewTimeTableExcel.setObjectName("viewTimeTableExcel")
        mainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 21))
        self.menubar.setObjectName("menubar")
        mainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainMenu)
        self.statusbar.setObjectName("statusbar")
        mainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(mainMenu)

        #=====================
        self.generalSettings.clicked.connect(self.showGeneralSettingsWindow)
        self.createDepartment.clicked.connect(self.showCreateDepartmentWindow)
        self.addTeachers.clicked.connect(self.showAddTeacherWindow)
        self.createNewProgram.clicked.connect(self.showAddProgramWindow)
        self.createClass.clicked.connect(self.showCreateClassWindow)
        self.generateTimeTable.clicked.connect(self.showGenerateTimeTableWindow)
        self.viewTimeTableHtml.clicked.connect(self.showInHTML)
        self.viewTimeTableExcel.clicked.connect(self.showInCSV)
        #------------------------
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "MainWindow"))
        self.generalSettings.setText(_translate("mainMenu", "General Settings"))
        self.createDepartment.setText(_translate("mainMenu", "Create Department"))
        self.viewRooms.setText(_translate("mainMenu", "View All Rooms"))
        self.viewDepartments.setText(_translate("mainMenu", "View All Departments"))
        self.viewTeachers.setText(_translate("mainMenu", "View All Teachers"))
        self.createClass.setText(_translate("mainMenu", "Create Class"))
        self.createNewProgram.setText(_translate("mainMenu", "Create New Program"))
        self.addRooms.setText(_translate("mainMenu", "Add Rooms"))
        self.addTeachers.setText(_translate("mainMenu", "Add Teachers"))
        self.label.setText(_translate("mainMenu", "The Smart Time Scheduler"))
        self.generateTimeTable.setText(_translate("mainMenu", "Generate Time Table"))
        self.viewTimeTableHtml.setText(_translate("mainMenu", "View Time Table HTML"))
        self.viewTimeTableExcel.setText(_translate("mainMenu", "View Time Table Excel"))

    def showGeneralSettingsWindow(self):

        import GeneralSettings
        self.generalSettingsWindow = QtWidgets.QMainWindow()
        self.ui = GeneralSettings.Ui_generalSettingsWindow()
        self.ui.setupUi(self.generalSettingsWindow)
        self.generalSettingsWindow.show()

    def showCreateDepartmentWindow(self):

        import CreateDepartment
        
        self.createDepartment = QtWidgets.QMainWindow()
        self.ui = CreateDepartment.Ui_createDepartment()
        self.ui.setupUi(self.createDepartment)
        self.createDepartment.show()

    def showCreateClassWindow(self):

        import CreateClass
        self.createClass = QtWidgets.QDialog()
        self.ui = CreateClass.Ui_createClass()
        self.ui.setupUi(self.createClass)
        self.createClass.show()

    def showAddProgramWindow(self):
        import AddProgram
        self.addProgram = QtWidgets.QWidget()
        self.ui = AddProgram.Ui_addProgram()
        self.ui.setupUi(self.addProgram)
        self.addProgram.show()
        
    def showAddTeacherWindow(self):
        import AddTeacher
        self.addTeacherDialog = QtWidgets.QDialog()
        self.ui = AddTeacher.Ui_addTeacherDialog()
        self.ui.setupUi(self.addTeacherDialog)
        self.addTeacherDialog.show()

    def showGenerateTimeTableWindow(self):
        import GenerateTimeTable
        self.generateTimeTable = QtWidgets.QWidget()
        self.ui = GenerateTimeTable.Ui_generateTimeTable()
        self.ui.setupUi(self.generateTimeTable)
        self.generateTimeTable.show()

    def showInHTML(self):
        import os
        import Filer
        os.startfile('%s/%s.html'%( Filer.TIME_TABLE_FOLDER, Filer.TIME_TABLE_FILE_NAME))
        
    def showInCSV(self):
        import os
        import Filer
        os.startfile('%s/%s.csv'%( Filer.TIME_TABLE_FOLDER, Filer.TIME_TABLE_FILE_NAME))
        
    
