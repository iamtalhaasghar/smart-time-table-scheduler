# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewTeachers.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_viewTeachers(object):
    def setupUi(self, viewTeachers):
        viewTeachers.setObjectName("viewTeachers")
        viewTeachers.resize(682, 507)
        self.teachersList = QtWidgets.QTreeWidget(viewTeachers)
        self.teachersList.setGeometry(QtCore.QRect(40, 30, 601, 421))
        self.teachersList.setObjectName("teachersList")

        self.retranslateUi(viewTeachers)
        
        self.addTeachersToTree()
        
        QtCore.QMetaObject.connectSlotsByName(viewTeachers)

    def retranslateUi(self, viewTeachers):
        _translate = QtCore.QCoreApplication.translate
        viewTeachers.setWindowTitle(_translate("viewTeachers", "All Teachers"))
        self.teachersList.headerItem().setText(0, _translate("viewTeachers", "Teacher ID"))
        self.teachersList.headerItem().setText(1, _translate("viewTeachers", "Teacher Name"))
        self.teachersList.headerItem().setText(2, _translate("viewTeachers", "Department"))

    def addTeachersToTree(self):
        import teacher
        tList = teacher.readAllTeachers()

        for t in tList:
            self.teachersList.addTopLevelItem(QtWidgets.QTreeWidgetItem(t))

