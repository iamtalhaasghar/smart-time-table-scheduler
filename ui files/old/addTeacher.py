# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_course.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addCourse(object):
    def setupUi(self, addCourse):
        addCourse.setObjectName("addCourse")
        addCourse.resize(659, 627)
        self.classDetails = QtWidgets.QGroupBox(addCourse)
        self.classDetails.setGeometry(QtCore.QRect(40, 30, 571, 501))
        self.classDetails.setObjectName("classDetails")
        self.contactHourLabel = QtWidgets.QLabel(self.classDetails)
        self.contactHourLabel.setGeometry(QtCore.QRect(80, 230, 81, 21))
        self.contactHourLabel.setObjectName("contactHourLabel")
        self.courseNameLabel = QtWidgets.QLabel(self.classDetails)
        self.courseNameLabel.setGeometry(QtCore.QRect(50, 90, 81, 16))
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.courseCodeLabel = QtWidgets.QLabel(self.classDetails)
        self.courseCodeLabel.setGeometry(QtCore.QRect(50, 50, 81, 16))
        self.courseCodeLabel.setObjectName("courseCodeLabel")
        self.courseCode = QtWidgets.QLineEdit(self.classDetails)
        self.courseCode.setGeometry(QtCore.QRect(140, 50, 291, 20))
        self.courseCode.setObjectName("courseCode")
        self.courseName = QtWidgets.QLineEdit(self.classDetails)
        self.courseName.setGeometry(QtCore.QRect(140, 90, 291, 20))
        self.courseName.setObjectName("courseName")
        self.theory = QtWidgets.QRadioButton(self.classDetails)
        self.theory.setGeometry(QtCore.QRect(110, 140, 131, 17))
        self.theory.setChecked(True)
        self.theory.setObjectName("theory")
        self.lab = QtWidgets.QRadioButton(self.classDetails)
        self.lab.setGeometry(QtCore.QRect(280, 140, 141, 17))
        self.lab.setObjectName("lab")
        self.totalCHLabel = QtWidgets.QLabel(self.classDetails)
        self.totalCHLabel.setGeometry(QtCore.QRect(70, 270, 111, 20))
        self.totalCHLabel.setObjectName("totalCHLabel")
        self.contactHour = QtWidgets.QSpinBox(self.classDetails)
        self.contactHour.setGeometry(QtCore.QRect(220, 230, 131, 22))
        self.contactHour.setMinimum(1)
        self.contactHour.setMaximum(10)
        self.contactHour.setObjectName("contactHour")
        self.totalCH = QtWidgets.QSpinBox(self.classDetails)
        self.totalCH.setGeometry(QtCore.QRect(220, 270, 131, 22))
        self.totalCH.setMinimum(1)
        self.totalCH.setMaximum(10)
        self.totalCH.setProperty("value", 3)
        self.totalCH.setObjectName("totalCH")
        self.sampleCourseLabel = QtWidgets.QLabel(self.classDetails)
        self.sampleCourseLabel.setGeometry(QtCore.QRect(40, 180, 201, 21))
        self.sampleCourseLabel.setObjectName("sampleCourseLabel")
        self.sampleCourseName = QtWidgets.QLineEdit(self.classDetails)
        self.sampleCourseName.setGeometry(QtCore.QRect(260, 180, 181, 21))
        self.sampleCourseName.setReadOnly(True)
        self.sampleCourseName.setObjectName("sampleCourseName")
        self.instructorLabel = QtWidgets.QLabel(self.classDetails)
        self.instructorLabel.setGeometry(QtCore.QRect(60, 460, 121, 21))
        self.instructorLabel.setObjectName("instructorLabel")
        self.instructorsDepartmentLabel = QtWidgets.QLabel(self.classDetails)
        self.instructorsDepartmentLabel.setGeometry(QtCore.QRect(60, 410, 131, 16))
        self.instructorsDepartmentLabel.setObjectName("instructorsDepartmentLabel")
        self.instructorDepartment = QtWidgets.QComboBox(self.classDetails)
        self.instructorDepartment.setGeometry(QtCore.QRect(200, 410, 251, 22))
        self.instructorDepartment.setObjectName("instructorDepartment")
        self.labDepartmentLabel = QtWidgets.QLabel(self.classDetails)
        self.labDepartmentLabel.setGeometry(QtCore.QRect(70, 320, 111, 16))
        self.labDepartmentLabel.setObjectName("labDepartmentLabel")
        self.labNameLabel = QtWidgets.QLabel(self.classDetails)
        self.labNameLabel.setGeometry(QtCore.QRect(70, 360, 111, 16))
        self.labNameLabel.setObjectName("labNameLabel")
        self.labDepartment = QtWidgets.QComboBox(self.classDetails)
        self.labDepartment.setGeometry(QtCore.QRect(200, 320, 251, 22))
        self.labDepartment.setObjectName("labDepartment")
        self.labName = QtWidgets.QComboBox(self.classDetails)
        self.labName.setGeometry(QtCore.QRect(200, 360, 251, 22))
        self.labName.setObjectName("labName")
        self.instructor = QtWidgets.QLineEdit(self.classDetails)
        self.instructor.setGeometry(QtCore.QRect(200, 460, 251, 20))
        self.instructor.setObjectName("instructor")
        self.saveCourse = QtWidgets.QPushButton(addCourse)
        self.saveCourse.setGeometry(QtCore.QRect(270, 560, 101, 31))
        self.saveCourse.setObjectName("saveCourse")

        self.retranslateUi(addCourse)
        self.instructor.textChanged['QString'].connect(self.classDetails.lower)
        QtCore.QMetaObject.connectSlotsByName(addCourse)
        addCourse.setTabOrder(self.courseCode, self.courseName)
        addCourse.setTabOrder(self.courseName, self.theory)
        addCourse.setTabOrder(self.theory, self.lab)
        addCourse.setTabOrder(self.lab, self.sampleCourseName)
        addCourse.setTabOrder(self.sampleCourseName, self.contactHour)
        addCourse.setTabOrder(self.contactHour, self.totalCH)

    def retranslateUi(self, addCourse):
        _translate = QtCore.QCoreApplication.translate
        addCourse.setWindowTitle(_translate("addCourse", "Add Course for Class"))
        self.classDetails.setTitle(_translate("addCourse", "Course Details"))
        self.contactHourLabel.setText(_translate("addCourse", "1 Credit Hour = "))
        self.courseNameLabel.setText(_translate("addCourse", "Course Name:"))
        self.courseCodeLabel.setText(_translate("addCourse", "Course Code:"))
        self.theory.setText(_translate("addCourse", "Theoretical Course"))
        self.lab.setText(_translate("addCourse", "Practical Course (Lab)"))
        self.totalCHLabel.setText(_translate("addCourse", "Total Credit Hours = "))
        self.contactHour.setSuffix(_translate("addCourse", "    Contact Hours"))
        self.sampleCourseLabel.setText(_translate("addCourse", "In TimeTable, the name will appear as:"))
        self.instructorLabel.setText(_translate("addCourse", "Instructor :"))
        self.instructorsDepartmentLabel.setText(_translate("addCourse", "Instructors Department:"))
        self.labDepartmentLabel.setText(_translate("addCourse", "Lab Department:"))
        self.labNameLabel.setText(_translate("addCourse", "Lab Name:"))
        self.saveCourse.setText(_translate("addCourse", "Save Course"))
