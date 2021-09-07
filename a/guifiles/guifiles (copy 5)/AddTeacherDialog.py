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
        addTeacherDialog.resize(423, 622)
        self.teacherNameLabel = QtWidgets.QLabel(addTeacherDialog)
        self.teacherNameLabel.setGeometry(QtCore.QRect(40, 90, 91, 16))
        self.teacherNameLabel.setObjectName("teacherNameLabel")
        self.facultyIDLabel = QtWidgets.QLabel(addTeacherDialog)
        self.facultyIDLabel.setGeometry(QtCore.QRect(50, 60, 61, 20))
        self.facultyIDLabel.setObjectName("facultyIDLabel")
        self.saveButton = QtWidgets.QPushButton(addTeacherDialog)
        self.saveButton.setGeometry(QtCore.QRect(300, 70, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.teacherName = QtWidgets.QLineEdit(addTeacherDialog)
        self.teacherName.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.teacherName.setObjectName("teacherName")
        self.facultyID = QtWidgets.QLineEdit(addTeacherDialog)
        self.facultyID.setGeometry(QtCore.QRect(140, 60, 113, 20))
        self.facultyID.setObjectName("facultyID")
        self.teachersList = QtWidgets.QTextBrowser(addTeacherDialog)
        self.teachersList.setGeometry(QtCore.QRect(30, 150, 341, 401))
        self.teachersList.setObjectName("teachersList")

        self.retranslateUi(addTeacherDialog)
        self.saveButton.pressed.connect(self.saveTeacherData)
        QtCore.QMetaObject.connectSlotsByName(addTeacherDialog)
        addTeacherDialog.setTabOrder(self.facultyID, self.teacherName)
        addTeacherDialog.setTabOrder(self.teacherName, self.saveButton)
        addTeacherDialog.setTabOrder(self.saveButton, self.teachersList)

    def retranslateUi(self, addTeacherDialog):
        _translate = QtCore.QCoreApplication.translate
        addTeacherDialog.setWindowTitle(_translate("addTeacherDialog", "Add New Teacher"))
        self.teacherNameLabel.setText(_translate("addTeacherDialog", "Teacher Name: "))
        self.facultyIDLabel.setText(_translate("addTeacherDialog", "Faculty ID:"))
        self.saveButton.setText(_translate("addTeacherDialog", "Save"))

    def saveTeacherData(self):
        tId = self.facultyID.text()
        tName = self.teacherName.text()
        import Teacher
        Teacher.addTeacher(tId,tName)
        self.teachersList.append('%s - %s'% (tId,tName))
        self.facultyID.clear()
        self.teacherName.clear()
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addTeacherDialog = QtWidgets.QDialog()
    ui = Ui_addTeacherDialog()
    ui.setupUi(addTeacherDialog)
    addTeacherDialog.show()
    sys.exit(app.exec_())
'''
