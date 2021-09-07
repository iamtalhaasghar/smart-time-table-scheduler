# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_department.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createDepartment(object):
    def setupUi(self, createDepartment):
        createDepartment.setObjectName("createDepartment")
        createDepartment.resize(606, 306)
        self.centralwidget = QtWidgets.QWidget(createDepartment)
        self.centralwidget.setObjectName("centralwidget")
        self.departmentInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.departmentInfo.setGeometry(QtCore.QRect(20, 30, 561, 161))
        self.departmentInfo.setObjectName("departmentInfo")
        self.totalLabsLabel = QtWidgets.QLabel(self.departmentInfo)
        self.totalLabsLabel.setGeometry(QtCore.QRect(60, 100, 81, 16))
        self.totalLabsLabel.setObjectName("totalLabsLabel")
        self.totalRoomsLabel = QtWidgets.QLabel(self.departmentInfo)
        self.totalRoomsLabel.setGeometry(QtCore.QRect(60, 70, 81, 16))
        self.totalRoomsLabel.setObjectName("totalRoomsLabel")
        self.departmentNameLabel = QtWidgets.QLabel(self.departmentInfo)
        self.departmentNameLabel.setGeometry(QtCore.QRect(60, 40, 111, 16))
        self.departmentNameLabel.setObjectName("departmentNameLabel")
        self.departmentName = QtWidgets.QLineEdit(self.departmentInfo)
        self.departmentName.setGeometry(QtCore.QRect(240, 40, 241, 20))
        self.departmentName.setObjectName("departmentName")
        self.totalRooms = QtWidgets.QSpinBox(self.departmentInfo)
        self.totalRooms.setGeometry(QtCore.QRect(240, 70, 121, 22))
        self.totalRooms.setMinimum(1)
        self.totalRooms.setMaximum(999999999)
        self.totalRooms.setProperty("value", 3)
        self.totalRooms.setObjectName("totalRooms")
        self.totalLabs = QtWidgets.QSpinBox(self.departmentInfo)
        self.totalLabs.setGeometry(QtCore.QRect(240, 100, 121, 22))
        self.totalLabs.setMinimum(1)
        self.totalLabs.setMaximum(999999999)
        self.totalLabs.setProperty("value", 2)
        self.totalLabs.setObjectName("totalLabs")
        self.saveDepartment = QtWidgets.QPushButton(self.centralwidget)
        self.saveDepartment.setGeometry(QtCore.QRect(220, 210, 121, 31))
        self.saveDepartment.setObjectName("saveDepartment")
        createDepartment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(createDepartment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 21))
        self.menubar.setObjectName("menubar")
        createDepartment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(createDepartment)
        self.statusbar.setObjectName("statusbar")
        createDepartment.setStatusBar(self.statusbar)

        self.retranslateUi(createDepartment)
        #-----------------------------------
        self.saveDepartment.clicked.connect(self.saveDepartmentData)

        #----------------------------------
        QtCore.QMetaObject.connectSlotsByName(createDepartment)

    def retranslateUi(self, createDepartment):
        _translate = QtCore.QCoreApplication.translate
        createDepartment.setWindowTitle(_translate("createDepartment", "Create New Department"))
        self.departmentInfo.setTitle(_translate("createDepartment", "Department Information"))
        self.totalLabsLabel.setText(_translate("createDepartment", "Total Labs:"))
        self.totalRoomsLabel.setText(_translate("createDepartment", "Total Rooms:"))
        self.departmentNameLabel.setText(_translate("createDepartment", "Department Name:"))
        self.saveDepartment.setText(_translate("createDepartment", "Save Department"))

    def saveDepartmentData(self):

        import Filer
        Filer.createDepartmentFolder(self.departmentName.text())
        import room
        room.createDepartmentRooms(self.departmentName.text(),self.totalRooms.value())
        import lab
        lab.createDepartmentLabs(self.departmentName.text(),self.totalLabs.value())
        
