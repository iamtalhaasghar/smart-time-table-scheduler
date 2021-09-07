# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_teacher_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addTeacherDialog(object):
    def setupUi(self, addTeacherDialog):
        addTeacherDialog.setObjectName("addTeacherDialog")
        addTeacherDialog.resize(423, 681)
        self.teacherNameLabel = QtWidgets.QLabel(addTeacherDialog)
        self.teacherNameLabel.setGeometry(QtCore.QRect(40, 90, 91, 16))
        self.teacherNameLabel.setObjectName("teacherNameLabel")
        self.facultyIDLabel = QtWidgets.QLabel(addTeacherDialog)
        self.facultyIDLabel.setGeometry(QtCore.QRect(50, 60, 61, 20))
        self.facultyIDLabel.setObjectName("facultyIDLabel")
        self.saveButton = QtWidgets.QPushButton(addTeacherDialog)
        self.saveButton.setGeometry(QtCore.QRect(300, 190, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.teacherName = QtWidgets.QLineEdit(addTeacherDialog)
        self.teacherName.setGeometry(QtCore.QRect(140, 90, 151, 20))
        self.teacherName.setObjectName("teacherName")
        self.facultyID = QtWidgets.QLineEdit(addTeacherDialog)
        self.facultyID.setGeometry(QtCore.QRect(140, 60, 151, 20))
        self.facultyID.setObjectName("facultyID")
        self.teachersList = QtWidgets.QTextBrowser(addTeacherDialog)
        self.teachersList.setGeometry(QtCore.QRect(40, 240, 341, 401))
        self.teachersList.setObjectName("teachersList")
        self.departmentLabel = QtWidgets.QLabel(addTeacherDialog)
        self.departmentLabel.setGeometry(QtCore.QRect(50, 130, 71, 16))
        self.departmentLabel.setObjectName("departmentLabel")
        self.department = QtWidgets.QComboBox(addTeacherDialog)
        self.department.setGeometry(QtCore.QRect(140, 130, 151, 22))
        self.department.setObjectName("department")

        self.addDepartmentsToList()
        self.saveButton.pressed.connect(self.saveTeacherData)

        self.retranslateUi(addTeacherDialog)
        self.saveButton.pressed.connect(self.teacherName.selectAll)
        QtCore.QMetaObject.connectSlotsByName(addTeacherDialog)
        addTeacherDialog.setTabOrder(self.facultyID, self.teacherName)
        addTeacherDialog.setTabOrder(self.teacherName, self.department)
        addTeacherDialog.setTabOrder(self.department, self.saveButton)
        addTeacherDialog.setTabOrder(self.saveButton, self.teachersList)

    def retranslateUi(self, addTeacherDialog):
        _translate = QtCore.QCoreApplication.translate
        addTeacherDialog.setWindowTitle(_translate("addTeacherDialog", "Add New Teacher"))
        self.teacherNameLabel.setText(_translate("addTeacherDialog", "Teacher Name: "))
        self.facultyIDLabel.setText(_translate("addTeacherDialog", "Faculty ID:"))
        self.saveButton.setText(_translate("addTeacherDialog", "Save"))
        self.departmentLabel.setText(_translate("addTeacherDialog", "Department:"))
        
    def addDepartmentsToList(self):
        import Filer
        d = Filer.listAllDepartments()
        for i in range(len(d)):
            self.department.addItem('%s'%(d[i]))
            
    def saveTeacherData(self):

        tId = self.facultyID.text()
        tName = self.teacherName.text()
        import Teacher
        Teacher.addTeacherInDepartment(self.department.currentText(),tId,tName)
        self.teachersList.append('%s  %s %s'% (tId,tName,self.department.currentText()))
        self.facultyID.clear()
        self.teacherName.clear()


