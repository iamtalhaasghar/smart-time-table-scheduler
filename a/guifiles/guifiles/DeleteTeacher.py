# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteTeacher.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_allTeachers(object):
    def setupUi(self, allTeachers):
        allTeachers.setObjectName("allTeachers")
        allTeachers.resize(682, 507)
        self.teachersList = QtWidgets.QTreeWidget(allTeachers)
        self.teachersList.setGeometry(QtCore.QRect(40, 30, 591, 401))
        self.teachersList.setObjectName("teachersList")
        self.deleteTeacher = QtWidgets.QPushButton(allTeachers)
        self.deleteTeacher.setGeometry(QtCore.QRect(474, 452, 111, 31))
        self.deleteTeacher.setObjectName("deleteTeacher")

        self.retranslateUi(allTeachers)

        self.addTeachersToTree()
        self.deleteTeacher.clicked.connect(self.deleteTeacherRecord)
        QtCore.QMetaObject.connectSlotsByName(allTeachers)

    def retranslateUi(self, allTeachers):
        _translate = QtCore.QCoreApplication.translate
        allTeachers.setWindowTitle(_translate("allTeachers", "All Teachers"))
        self.teachersList.headerItem().setText(0, _translate("allTeachers", "Teacher ID"))
        self.teachersList.headerItem().setText(1, _translate("allTeachers", "Teacher Name"))
        self.teachersList.headerItem().setText(2, _translate("allTeachers", "Department"))
        self.deleteTeacher.setText(_translate("allTeachers", "Delete Teacher"))

    def addTeachersToTree(self):
        import teacher
        tList = teacher.readAllTeachers()
        for t in tList:
            self.teachersList.addTopLevelItem(QtWidgets.QTreeWidgetItem(t))

    def deleteTeacherRecord(self):
        import teacher
        itemWidget =  self.teachersList.selectedItems()[0]
        teacher.deleteTeacher(itemWidget.data(0,0))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    allTeachers = QtWidgets.QDialog()
    ui = Ui_allTeachers()
    ui.setupUi(allTeachers)
    allTeachers.show()
    sys.exit(app.exec_())

