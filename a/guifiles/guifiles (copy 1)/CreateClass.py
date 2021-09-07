# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_class.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createClass(object):
    def setupUi(self, createClass):
        createClass.setObjectName("createClass")
        createClass.resize(659, 736)
        self.classDetails = QtWidgets.QGroupBox(createClass)
        self.classDetails.setGeometry(QtCore.QRect(40, 30, 571, 581))
        self.classDetails.setObjectName("classDetails")
        self.classNameLabel = QtWidgets.QLabel(self.classDetails)
        self.classNameLabel.setGeometry(QtCore.QRect(60, 100, 81, 16))
        self.classNameLabel.setObjectName("classNameLabel")
        self.contactHourLabel = QtWidgets.QLabel(self.classDetails)
        self.contactHourLabel.setGeometry(QtCore.QRect(70, 300, 81, 21))
        self.contactHourLabel.setObjectName("contactHourLabel")
        self.className = QtWidgets.QLineEdit(self.classDetails)
        self.className.setGeometry(QtCore.QRect(160, 100, 291, 20))
        self.className.setObjectName("className")
        self.courseNameLabel = QtWidgets.QLabel(self.classDetails)
        self.courseNameLabel.setGeometry(QtCore.QRect(60, 180, 81, 16))
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.courseCodeLabel = QtWidgets.QLabel(self.classDetails)
        self.courseCodeLabel.setGeometry(QtCore.QRect(60, 140, 81, 16))
        self.courseCodeLabel.setObjectName("courseCodeLabel")
        self.courseCode = QtWidgets.QLineEdit(self.classDetails)
        self.courseCode.setGeometry(QtCore.QRect(150, 140, 291, 20))
        self.courseCode.setObjectName("courseCode")
        self.courseName = QtWidgets.QLineEdit(self.classDetails)
        self.courseName.setGeometry(QtCore.QRect(150, 180, 291, 20))
        self.courseName.setObjectName("courseName")
        self.theory = QtWidgets.QRadioButton(self.classDetails)
        self.theory.setGeometry(QtCore.QRect(80, 220, 131, 17))
        self.theory.setChecked(True)
        self.theory.setObjectName("theory")
        self.lab = QtWidgets.QRadioButton(self.classDetails)
        self.lab.setGeometry(QtCore.QRect(280, 220, 141, 17))
        self.lab.setObjectName("lab")
        self.totalCHLabel = QtWidgets.QLabel(self.classDetails)
        self.totalCHLabel.setGeometry(QtCore.QRect(70, 330, 111, 20))
        self.totalCHLabel.setObjectName("totalCHLabel")
        self.contactHour = QtWidgets.QSpinBox(self.classDetails)
        self.contactHour.setGeometry(QtCore.QRect(210, 300, 131, 22))
        self.contactHour.setMinimum(1)
        self.contactHour.setMaximum(10)
        self.contactHour.setObjectName("contactHour")
        self.totalCH = QtWidgets.QSpinBox(self.classDetails)
        self.totalCH.setGeometry(QtCore.QRect(210, 330, 131, 22))
        self.totalCH.setMinimum(1)
        self.totalCH.setMaximum(10)
        self.totalCH.setProperty("value", 3)
        self.totalCH.setObjectName("totalCH")
        self.sampleCourseLabel = QtWidgets.QLabel(self.classDetails)
        self.sampleCourseLabel.setGeometry(QtCore.QRect(60, 260, 201, 21))
        self.sampleCourseLabel.setObjectName("sampleCourseLabel")
        self.sampleCourseName = QtWidgets.QLineEdit(self.classDetails)
        self.sampleCourseName.setGeometry(QtCore.QRect(270, 259, 181, 21))
        self.sampleCourseName.setReadOnly(True)
        self.sampleCourseName.setObjectName("sampleCourseName")
        self.instructorLabel = QtWidgets.QLabel(self.classDetails)
        self.instructorLabel.setGeometry(QtCore.QRect(50, 520, 121, 21))
        self.instructorLabel.setObjectName("instructorLabel")
        self.instructor = QtWidgets.QComboBox(self.classDetails)
        self.instructor.setGeometry(QtCore.QRect(190, 520, 251, 22))
        self.instructor.setEditable(False)
        self.instructor.setObjectName("instructor")
        self.line = QtWidgets.QFrame(self.classDetails)
        self.line.setGeometry(QtCore.QRect(60, 120, 471, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.departmentLabel = QtWidgets.QLabel(self.classDetails)
        self.departmentLabel.setGeometry(QtCore.QRect(60, 40, 71, 16))
        self.departmentLabel.setObjectName("departmentLabel")
        self.department = QtWidgets.QComboBox(self.classDetails)
        self.department.setGeometry(QtCore.QRect(160, 40, 291, 22))
        self.department.setEditable(False)
        self.department.setCurrentText("")
        self.department.setObjectName("department")
        self.degreeProgramLabel = QtWidgets.QLabel(self.classDetails)
        self.degreeProgramLabel.setGeometry(QtCore.QRect(60, 70, 91, 16))
        self.degreeProgramLabel.setObjectName("degreeProgramLabel")
        self.degreeProgram = QtWidgets.QComboBox(self.classDetails)
        self.degreeProgram.setGeometry(QtCore.QRect(160, 70, 291, 22))
        self.degreeProgram.setEditable(False)
        self.degreeProgram.setObjectName("degreeProgram")
        self.instructorsDepartmentLabel = QtWidgets.QLabel(self.classDetails)
        self.instructorsDepartmentLabel.setGeometry(QtCore.QRect(50, 470, 131, 16))
        self.instructorsDepartmentLabel.setObjectName("instructorsDepartmentLabel")
        self.instructorDepartment = QtWidgets.QComboBox(self.classDetails)
        self.instructorDepartment.setGeometry(QtCore.QRect(190, 470, 251, 22))
        self.instructorDepartment.setObjectName("instructorDepartment")
        self.labDepartmentLabel = QtWidgets.QLabel(self.classDetails)
        self.labDepartmentLabel.setGeometry(QtCore.QRect(50, 390, 111, 16))
        self.labDepartmentLabel.setObjectName("labDepartmentLabel")
        self.labNameLabel = QtWidgets.QLabel(self.classDetails)
        self.labNameLabel.setGeometry(QtCore.QRect(50, 430, 111, 16))
        self.labNameLabel.setObjectName("labNameLabel")
        self.labDepartment = QtWidgets.QComboBox(self.classDetails)
        self.labDepartment.setGeometry(QtCore.QRect(190, 390, 251, 22))
        self.labDepartment.setObjectName("labDepartment")
        self.labDepartment.setEnabled(False)
        self.labName = QtWidgets.QComboBox(self.classDetails)
        self.labName.setGeometry(QtCore.QRect(190, 430, 251, 22))
        self.labName.setObjectName("labName")
        self.labName.setEnabled(False)
        self.saveCourse = QtWidgets.QPushButton(createClass)
        self.saveCourse.setGeometry(QtCore.QRect(290, 660, 101, 31))
        self.saveCourse.setObjectName("saveCourse")

        self.retranslateUi(createClass)

        #=====================
        self.addDepartmentsToLists()
        self.updateLists()
        #=====================
        
        #============Event Handling===========

        self.department.currentTextChanged.connect(self.updateLists)
        self.instructorDepartment.currentTextChanged.connect(self.addTeachersToList)
        self.labDepartment.currentTextChanged.connect(self.addLabsToList)
        self.courseCode.textChanged['QString'].connect(self.setSampleCourseName)
        self.courseName.textChanged['QString'].connect(self.setSampleCourseName)
        self.theory.toggled.connect(self.theoreticalSettings)
        self.lab.toggled.connect(self.practicalSettings)
        self.saveCourse.clicked.connect(self.addCourse)
        
        #======================================
        
        QtCore.QMetaObject.connectSlotsByName(createClass)
        createClass.setTabOrder(self.className, self.courseCode)
        createClass.setTabOrder(self.courseCode, self.courseName)
        createClass.setTabOrder(self.courseName, self.theory)
        createClass.setTabOrder(self.theory, self.lab)
        createClass.setTabOrder(self.lab, self.sampleCourseName)
        createClass.setTabOrder(self.sampleCourseName, self.contactHour)
        createClass.setTabOrder(self.contactHour, self.totalCH)
        createClass.setTabOrder(self.totalCH, self.instructor)

    def retranslateUi(self, createClass):
        _translate = QtCore.QCoreApplication.translate
        createClass.setWindowTitle(_translate("createClass", "Create Class"))
        self.classDetails.setTitle(_translate("createClass", "Class Details"))
        self.classNameLabel.setText(_translate("createClass", "Class Name:"))
        self.contactHourLabel.setText(_translate("createClass", "1 Credit Hour = "))
        self.courseNameLabel.setText(_translate("createClass", "Course Name:"))
        self.courseCodeLabel.setText(_translate("createClass", "Course Code:"))
        self.theory.setText(_translate("createClass", "Theoretical Course"))
        self.lab.setText(_translate("createClass", "Practical Course (Lab)"))
        self.totalCHLabel.setText(_translate("createClass", "Total Credit Hours = "))
        self.contactHour.setSuffix(_translate("createClass", "    Contact Hours"))
        self.sampleCourseLabel.setText(_translate("createClass", "In TimeTable, the name will appear as:"))
        self.instructorLabel.setText(_translate("createClass", "Instructor :"))
        self.departmentLabel.setText(_translate("createClass", "Department : "))
        self.department.setToolTip(_translate("createClass", "Select"))
        self.degreeProgramLabel.setText(_translate("createClass", "Deegre Program:"))
        self.instructorsDepartmentLabel.setText(_translate("createClass", "Instructor`s Department:"))
        self.labDepartmentLabel.setText(_translate("createClass", "Lab Department:"))
        self.labNameLabel.setText(_translate("createClass", "Lab Name:"))
        self.saveCourse.setText(_translate("createClass", "Save Course"))

    def addTeachersToList(self):
        self.instructor.clear()
        import teacher
        t = teacher.readAllTeachersOfDepartment(self.instructorDepartment.currentText())

        for i in range(len(t)):
            self.instructor.addItem('%s : %s'%(t[i][0],t[i][1]))


    def addLabsToList(self):
        self.labName.clear()
        import lab
        t = lab.readAllLabsOfDepartment(self.instructorDepartment.currentText())
        for i in range(len(t)):
            self.labName.addItem('%s'%(t[i]))            


    def addDepartmentsToLists(self):
        import Filer
        d = Filer.listAllDepartments()
        for i in range(len(d)):
            temp = '%s'%(d[i])
            self.department.addItem(temp)
            self.instructorDepartment.addItem(temp)
            self.labDepartment.addItem(temp)          

        
    def addProgramsToList(self):
        self.degreeProgram.clear()
        import Filer
        p = Filer.programsOfDepartment(self.department.currentText())
        for i in range(len(p)):
            self.degreeProgram.addItem('%s'%(p[i]))

    def updateLists(self):
        self.addProgramsToList()
        self.instructorDepartment.setCurrentText(self.department.currentText())
        self.labDepartment.setCurrentText(self.department.currentText())
        self.addTeachersToList()            
        self.addLabsToList()

    def setSampleCourseName(self):
        self.sampleCourseName.setText('%s - %s'%(self.courseCode.text(),
                                               self.courseName.text()))

    def addCourse(self):
        import Semester
        import TimeTable
        if(self.lab.isChecked()):
            courseName = '%s %s'%(self.courseName.text(),TimeTable.theDefaultLabChars())
            import lab
            lab.assignLab(self.courseCode.text(),
                          self.className.text(), self.labName.currentText())
        else:
            courseName = self.courseName.text()
            
        Semester.addCourse(self.department.currentText(),
                           self.degreeProgram.currentText(),
                           self.className.text(),self.courseCode.text(), courseName,
                           self.contactHour.value(), self.totalCH.value())
        import teacher
        t = self.instructor.currentText().split(' : ')
        
        teacher.assignTeacher(self.courseCode.text(),
                              self.className.text(),t[0],t[1])
        self.courseName.clear()
        self.courseCode.clear()
        self.theory.setChecked(True)

    def theoreticalSettings(self):
        if(self.theory.isChecked()):
            self.contactHour.setValue(1)
            self.totalCH.setValue(3)
            self.setSampleCourseName()
            self.labDepartment.setEnabled(False)
            self.labName.setEnabled(False)
    def practicalSettings(self):
        if(self.lab.isChecked()):
            
            self.contactHour.setValue(3)
            self.totalCH.setValue(1)
            self.setSampleCourseName()
            import TimeTable
            self.sampleCourseName.setText('%s %s'% (self.sampleCourseName.text(),
                                                      TimeTable.theDefaultLabChars()))

            self.labDepartment.setEnabled(True)
            self.labName.setEnabled(True)

            
