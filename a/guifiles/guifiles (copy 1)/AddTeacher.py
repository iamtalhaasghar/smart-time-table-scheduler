# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTeacher.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addTeacherDialog(object):
    def setupUi(self, addTeacherDialog):
        addTeacherDialog.setObjectName("addTeacherDialog")
        addTeacherDialog.resize(408, 306)
        self.gridLayoutWidget = QtWidgets.QWidget(addTeacherDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 40, 321, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.facultyIdLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.facultyIdLabel.setObjectName("facultyIdLabel")
        self.gridLayout.addWidget(self.facultyIdLabel, 0, 0, 1, 1)
        self.teacherNameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.teacherNameLabel.setObjectName("teacherNameLabel")
        self.gridLayout.addWidget(self.teacherNameLabel, 1, 0, 1, 1)
        self.departmentLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.gridLayout.addWidget(self.departmentLabel, 2, 0, 1, 1)
        self.facultyId = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.facultyId.setObjectName("facultyId")
        self.gridLayout.addWidget(self.facultyId, 0, 1, 1, 1)
        self.teacherName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.teacherName.setObjectName("teacherName")
        self.gridLayout.addWidget(self.teacherName, 1, 1, 1, 1)
        self.department = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.department.setObjectName("department")
        self.gridLayout.addWidget(self.department, 2, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(addTeacherDialog)
        self.saveButton.setGeometry(QtCore.QRect(170, 260, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.cancelButton = QtWidgets.QPushButton(addTeacherDialog)
        self.cancelButton.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(addTeacherDialog)

        self.addDepartmentsToList()
        self.saveButton.clicked.connect(self.saveTeacherData)
        
        QtCore.QMetaObject.connectSlotsByName(addTeacherDialog)

    def retranslateUi(self, addTeacherDialog):
        _translate = QtCore.QCoreApplication.translate
        addTeacherDialog.setWindowTitle(_translate("addTeacherDialog", "Add New Teacher"))
        self.facultyIdLabel.setText(_translate("addTeacherDialog", "Faculty ID:"))
        self.teacherNameLabel.setText(_translate("addTeacherDialog", "Teacher Name:"))
        self.departmentLabel.setText(_translate("addTeacherDialog", "Department:"))
        self.saveButton.setText(_translate("addTeacherDialog", "Save"))
        self.cancelButton.setText(_translate("addTeacherDialog", "Cancel"))

    def addDepartmentsToList(self):
        import Filer
        d = Filer.listAllDepartments()
        for i in range(len(d)):
            self.department.addItem('%s'%(d[i]))
            
    def saveTeacherData(self):

        tId = self.facultyId.text()
        tDepart = self.department.currentText()
        tName = self.teacherName.text()
        from teacher import Teacher
        t = Teacher(tId, tName, tDepart)
        t.saveToDatabase()
        self.facultyId.clear()
        self.teacherName.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addTeacherDialog = QtWidgets.QDialog()
    ui = Ui_addTeacherDialog()
    ui.setupUi(addTeacherDialog)
    addTeacherDialog.show()
    sys.exit(app.exec_())

