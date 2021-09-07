# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateCourse.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addCourseDialog(object):
    def setupUi(self, addCourseDialog):
        addCourseDialog.setObjectName("addCourseDialog")
        addCourseDialog.resize(408, 454)
        self.gridLayoutWidget = QtWidgets.QWidget(addCourseDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 40, 321, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.courseCodeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.courseCodeLabel.setObjectName("courseCodeLabel")
        self.gridLayout.addWidget(self.courseCodeLabel, 0, 0, 1, 1)
        self.courseNameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.gridLayout.addWidget(self.courseNameLabel, 2, 0, 1, 1)
        self.courseCode = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.courseCode.setObjectName("courseCode")
        self.gridLayout.addWidget(self.courseCode, 0, 1, 1, 1)
        self.courseName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.courseName.setObjectName("courseName")
        self.gridLayout.addWidget(self.courseName, 2, 1, 1, 1)
        self.theoreticalCourse = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.theoreticalCourse.setChecked(True)
        self.theoreticalCourse.setObjectName("theoreticalCourse")
        self.gridLayout.addWidget(self.theoreticalCourse, 1, 0, 1, 1)
        self.practicalCourse = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.practicalCourse.setObjectName("practicalCourse")
        self.gridLayout.addWidget(self.practicalCourse, 1, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(addCourseDialog)
        self.saveButton.setGeometry(QtCore.QRect(170, 330, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.cancelButton = QtWidgets.QPushButton(addCourseDialog)
        self.cancelButton.setGeometry(QtCore.QRect(290, 330, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.sampleCourseNameLabel = QtWidgets.QLabel(addCourseDialog)
        self.sampleCourseNameLabel.setGeometry(QtCore.QRect(40, 240, 281, 16))
        self.sampleCourseNameLabel.setObjectName("sampleCourseNameLabel")
        self.sampleCourseName = QtWidgets.QLineEdit(addCourseDialog)
        self.sampleCourseName.setGeometry(QtCore.QRect(40, 270, 311, 20))
        self.sampleCourseName.setReadOnly(True)
        self.sampleCourseName.setObjectName("sampleCourseName")

        self.retranslateUi(addCourseDialog)
        self.theoreticalCourse.toggled.connect(self.setSampleCourseName)
        self.practicalCourse.toggled.connect(self.setSampleCourseName)
        self.courseName.textChanged['QString'].connect(self.setSampleCourseName)
        self.saveButton.clicked.connect(self.createNewCourse)
        
        QtCore.QMetaObject.connectSlotsByName(addCourseDialog)

    def retranslateUi(self, addCourseDialog):
        _translate = QtCore.QCoreApplication.translate
        addCourseDialog.setWindowTitle(_translate("addCourseDialog", "Create New Course"))
        self.courseCodeLabel.setText(_translate("addCourseDialog", "Course Code:"))
        self.courseNameLabel.setText(_translate("addCourseDialog", "Course Name:"))
        self.theoreticalCourse.setText(_translate("addCourseDialog", "Theoretical Course"))
        self.practicalCourse.setText(_translate("addCourseDialog", "Practical Course (Lab)"))
        self.saveButton.setText(_translate("addCourseDialog", "Save"))
        self.cancelButton.setText(_translate("addCourseDialog", "Cancel"))
        self.sampleCourseNameLabel.setText(_translate("addCourseDialog", "In Time Table, course name will appear as:"))

    def setSampleCourseName(self):
        if(self.practicalCourse.isChecked()):
            import TimeTable
            self.sampleCourseName.setText('%s %s' % (self.courseName.text(),
                    TimeTable.theDefaultLabChars()))
        else:
            self.sampleCourseName.setText(self.courseName.text())
                                                 

    def createNewCourse(self):
        from course import Course
        newCourse = Course(self.courseCode.text(), self.sampleCourseName.text())
        newCourse.saveToDatabase()
        self.courseCode.clear()
        self.courseName.clear()
        self.sampleCourseName.clear()
        self.theoreticalCourse.setChecked(True)
