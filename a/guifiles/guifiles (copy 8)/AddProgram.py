# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_program.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addProgram(object):
    def setupUi(self, addProgram):
        addProgram.setObjectName("addProgram")
        addProgram.resize(399, 282)
        self.departmentNameLabel = QtWidgets.QLabel(addProgram)
        self.departmentNameLabel.setGeometry(QtCore.QRect(40, 70, 81, 16))
        self.departmentNameLabel.setObjectName("departmentNameLabel")
        self.programNameLabel = QtWidgets.QLabel(addProgram)
        self.programNameLabel.setGeometry(QtCore.QRect(40, 120, 121, 16))
        self.programNameLabel.setObjectName("programNameLabel")
        self.saveButton = QtWidgets.QPushButton(addProgram)
        self.saveButton.setGeometry(QtCore.QRect(160, 200, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.departmentName = QtWidgets.QComboBox(addProgram)
        self.departmentName.setGeometry(QtCore.QRect(190, 70, 151, 22))
        self.departmentName.setObjectName("departmentName")
        self.programName = QtWidgets.QLineEdit(addProgram)
        self.programName.setGeometry(QtCore.QRect(190, 120, 151, 20))
        self.programName.setObjectName("programName")

        self.retranslateUi(addProgram)
        
        
        self.addDepartmentsToList()
        self.saveButton.clicked.connect(self.saveDegreeProgram)
        QtCore.QMetaObject.connectSlotsByName(addProgram)

    def retranslateUi(self, addProgram):
        _translate = QtCore.QCoreApplication.translate
        addProgram.setWindowTitle(_translate("addProgram", "Add Degree Program"))
        self.departmentNameLabel.setText(_translate("addProgram", "Department:"))
        self.programNameLabel.setText(_translate("addProgram", "Degree Program Name:"))
        self.saveButton.setText(_translate("addProgram", "Save"))
        
    def addDepartmentsToList(self):
        import Filer
        d = Filer.listAllDepartments()
        for i in range(len(d)):
            self.departmentName.addItem('%s'%(d[i]))

    def saveDegreeProgram(self):
        import Filer
        Filer.createDegreeProgramFolder(
            self.departmentName.currentText(), self.programName.text())

