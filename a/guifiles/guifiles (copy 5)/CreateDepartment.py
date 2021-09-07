# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'semester.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createDepartment(object):
    def setupUi(self, createDepartment):
        createDepartment.setObjectName("createDepartment")
        createDepartment.resize(659, 737)
        self.label = QtWidgets.QLabel(createDepartment)
        self.label.setGeometry(QtCore.QRect(70, 80, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(createDepartment)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(createDepartment)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 81, 16))
        self.label_3.setObjectName("label_3")
        self.departmentInfo = QtWidgets.QGroupBox(createDepartment)
        self.departmentInfo.setGeometry(QtCore.QRect(40, 40, 561, 161))
        self.departmentInfo.setObjectName("departmentInfo")
        self.departmentName = QtWidgets.QLineEdit(self.departmentInfo)
        self.departmentName.setGeometry(QtCore.QRect(200, 40, 211, 20))
        self.departmentName.setObjectName("departmentName")
        self.totalRooms = QtWidgets.QSpinBox(self.departmentInfo)
        self.totalRooms.setGeometry(QtCore.QRect(200, 70, 211, 22))
        self.totalRooms.setMinimum(1)
        self.totalRooms.setMaximum(9)
        self.totalRooms.setProperty("value", 3)
        self.totalRooms.setObjectName("totalRooms")
        self.totalLabs = QtWidgets.QSpinBox(self.departmentInfo)
        self.totalLabs.setGeometry(QtCore.QRect(200, 100, 211, 22))
        self.totalLabs.setMinimum(1)
        self.totalLabs.setMaximum(9)
        self.totalLabs.setProperty("value", 2)
        self.totalLabs.setObjectName("totalLabs")
        self.semester = QtWidgets.QGroupBox(createDepartment)
        self.semester.setGeometry(QtCore.QRect(40, 210, 561, 371))
        self.semester.setObjectName("semester")
        self.classNameLabel = QtWidgets.QLabel(self.semester)
        self.classNameLabel.setGeometry(QtCore.QRect(40, 30, 81, 16))
        self.classNameLabel.setObjectName("classNameLabel")
        self.contactHourLabel = QtWidgets.QLabel(self.semester)
        self.contactHourLabel.setGeometry(QtCore.QRect(50, 230, 81, 21))
        self.contactHourLabel.setObjectName("contactHourLabel")
        self.className = QtWidgets.QLineEdit(self.semester)
        self.className.setGeometry(QtCore.QRect(130, 30, 291, 20))
        self.className.setObjectName("className")
        self.courseNameLabel = QtWidgets.QLabel(self.semester)
        self.courseNameLabel.setGeometry(QtCore.QRect(40, 110, 81, 16))
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.courseCodeLabel = QtWidgets.QLabel(self.semester)
        self.courseCodeLabel.setGeometry(QtCore.QRect(40, 70, 81, 16))
        self.courseCodeLabel.setObjectName("courseCodeLabel")
        self.courseCode = QtWidgets.QLineEdit(self.semester)
        self.courseCode.setGeometry(QtCore.QRect(130, 70, 291, 20))
        self.courseCode.setObjectName("courseCode")
        self.courseName = QtWidgets.QLineEdit(self.semester)
        self.courseName.setGeometry(QtCore.QRect(130, 110, 291, 20))
        self.courseName.setObjectName("courseName")
        self.theory = QtWidgets.QRadioButton(self.semester)
        self.theory.setGeometry(QtCore.QRect(60, 150, 131, 17))
        self.theory.setChecked(True)
        self.theory.setObjectName("theory")
        self.lab = QtWidgets.QRadioButton(self.semester)
        self.lab.setGeometry(QtCore.QRect(260, 150, 141, 17))
        self.lab.setObjectName("lab")
        self.totalCHLabel = QtWidgets.QLabel(self.semester)
        self.totalCHLabel.setGeometry(QtCore.QRect(50, 260, 111, 20))
        self.totalCHLabel.setObjectName("totalCHLabel")
        self.contactHour = QtWidgets.QSpinBox(self.semester)
        self.contactHour.setGeometry(QtCore.QRect(190, 230, 131, 22))
        self.contactHour.setMinimum(1)
        self.contactHour.setMaximum(10)
        self.contactHour.setObjectName("contactHour")
        self.totalCH = QtWidgets.QSpinBox(self.semester)
        self.totalCH.setGeometry(QtCore.QRect(190, 260, 131, 22))
        self.totalCH.setMinimum(1)
        self.totalCH.setMaximum(10)
        self.totalCH.setProperty("value", 3)
        self.totalCH.setObjectName("totalCH")
        self.sampleCourseLabel = QtWidgets.QLabel(self.semester)
        self.sampleCourseLabel.setGeometry(QtCore.QRect(40, 190, 201, 21))
        self.sampleCourseLabel.setObjectName("sampleCourseLabel")
        self.sampleCourseName = QtWidgets.QLineEdit(self.semester)
        self.sampleCourseName.setGeometry(QtCore.QRect(250, 189, 181, 21))
        self.sampleCourseName.setReadOnly(True)
        self.sampleCourseName.setObjectName("sampleCourseName")
        self.instructorLabel = QtWidgets.QLabel(self.semester)
        self.instructorLabel.setGeometry(QtCore.QRect(60, 310, 121, 21))
        self.instructorLabel.setObjectName("instructorLabel")
        self.instructor = QtWidgets.QComboBox(self.semester)
        self.instructor.setGeometry(QtCore.QRect(160, 310, 251, 22))
        self.instructor.setObjectName("instructor")
        #=====================
        self.addTeachersToList()
        #=====================
        self.line = QtWidgets.QFrame(self.semester)
        self.line.setGeometry(QtCore.QRect(40, 50, 471, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.saveCourse = QtWidgets.QPushButton(createDepartment)
        self.saveCourse.setGeometry(QtCore.QRect(240, 620, 101, 31))
        self.saveCourse.setObjectName("saveCourse")
        self.saveDepartment = QtWidgets.QPushButton(createDepartment)
        self.saveDepartment.setGeometry(QtCore.QRect(60, 620, 121, 31))
        self.saveDepartment.setObjectName("saveDepartment")
        self.createClass = QtWidgets.QPushButton(createDepartment)
        self.createClass.setGeometry(QtCore.QRect(400, 620, 101, 31))
        self.createClass.setObjectName("createClass")

        #============Event Handling===========

        self.retranslateUi(createDepartment)
        self.courseCode.textChanged['QString'].connect(self.setSampleCourseName)
        self.courseName.textChanged['QString'].connect(self.setSampleCourseName)
        self.theory.toggled.connect(self.theoreticalSettings)
        self.lab.toggled.connect(self.practicalSettings)
        self.saveDepartment.clicked.connect(self.saveRoomsAndLabsData)
        self.saveCourse.clicked.connect(self.addCourse)
        
        #======================================
        
        QtCore.QMetaObject.connectSlotsByName(createDepartment)
        createDepartment.setTabOrder(self.departmentName, self.className)
        createDepartment.setTabOrder(self.className, self.courseCode)
        createDepartment.setTabOrder(self.courseCode, self.courseName)
        createDepartment.setTabOrder(self.courseName, self.theory)
        createDepartment.setTabOrder(self.theory, self.lab)
        createDepartment.setTabOrder(self.lab, self.sampleCourseName)
        createDepartment.setTabOrder(self.sampleCourseName, self.contactHour)
        createDepartment.setTabOrder(self.contactHour, self.totalCH)
        createDepartment.setTabOrder(self.totalCH, self.instructor)

    def retranslateUi(self, createDepartment):
        _translate = QtCore.QCoreApplication.translate
        createDepartment.setWindowTitle(_translate("createDepartment", "Create Department"))
        self.label.setText(_translate("createDepartment", "Department Name:"))
        self.label_2.setText(_translate("createDepartment", "Total Rooms:"))
        self.label_3.setText(_translate("createDepartment", "Total Labs:"))
        self.departmentInfo.setTitle(_translate("createDepartment", "Department Information"))
        self.semester.setTitle(_translate("createDepartment", "Semester"))
        self.classNameLabel.setText(_translate("createDepartment", "Class Name:"))
        self.contactHourLabel.setText(_translate("createDepartment", "1 Credit Hour = "))
        self.courseNameLabel.setText(_translate("createDepartment", "Course Name:"))
        self.courseCodeLabel.setText(_translate("createDepartment", "Course Code:"))
        self.theory.setText(_translate("createDepartment", "Theoretical Course"))
        self.lab.setText(_translate("createDepartment", "Practical Course (Lab)"))
        self.totalCHLabel.setText(_translate("createDepartment", "Total Credit Hours = "))
        self.contactHour.setSuffix(_translate("createDepartment", "    Contact Hours"))
        self.sampleCourseLabel.setText(_translate("createDepartment", "In TimeTable, the name will appear as:"))
        self.instructorLabel.setText(_translate("createDepartment", "Instructor :"))
        self.saveCourse.setText(_translate("createDepartment", "Save Course"))
        self.saveDepartment.setText(_translate("createDepartment", "Save Department"))
        self.createClass.setText(_translate("createDepartment", "Create Class"))

    def addTeachersToList(self):
        import Teacher
        t = Teacher.readAllTeachers()
        ids = tuple(t.index)
        names = tuple(t.Name)
        for i in range(len(ids)):
            self.instructor.addItem('%s : %s'%(ids[i],names[i]))

    def setSampleCourseName(self):
        self.sampleCourseName.setText('%s - %s'%(self.courseCode.text(),
                                               self.courseName.text()))

    def saveRoomsAndLabsData(self):
        import Room
        import Lab
        Room.createRooms(self.totalRooms.value())
        Lab.createLabs(self.totalLabs.value())

    def addCourse(self):
        import Semester
        import TimeTable
        if(self.lab.isChecked()):
            courseName = '%s %s'%(self.courseName.text(),TimeTable.theDefaultLabChars())
        else:
            courseName = self.courseName.text()
            
        Semester.addCourse(self.className.text(),self.courseCode.text(), courseName,
                           self.contactHour.value(), self.totalCH.value())
        import Teacher
        teacher = self.instructor.currentText().split(' : ')
        Teacher.assignTeacher(self.courseCode.text(),
                              self.className.text(),teacher[0],teacher[1])
        self.courseName.clear()
        self.courseCode.clear()
        self.theory.setChecked(True)

    def theoreticalSettings(self):
        if(self.theory.isChecked()):
            self.contactHour.setValue(1)
            self.totalCH.setValue(3)
            self.setSampleCourseName()
    def practicalSettings(self):
        if(self.lab.isChecked()):
            self.contactHour.setValue(3)
            self.totalCH.setValue(1)
            self.setSampleCourseName()
            import TimeTable
            self.sampleCourseName.setText('%s %s'% (self.sampleCourseName.text(),
                                                      TimeTable.theDefaultLabChars()))
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createDepartment = QtWidgets.QDialog()
    ui = Ui_createDepartment()
    ui.setupUi(createDepartment)
    createDepartment.show()
    sys.exit(app.exec_())

