# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_course.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QStringListModel
        
class Ui_addCourse(object):
    
    def __init__(self, semester):
        self.newSemester = semester
        from course import Course
        self.newCourse = Course()

        self.courseCompleter = QCompleter()
        self.courseModel = QStringListModel()
        self.courseCompleter.setModel(self.courseModel)

        self.instructorCompleter = QCompleter()
        self.instructorModel = QStringListModel()
        self.instructorCompleter.setModel(self.instructorModel)

    def setupUi(self, addCourse):
        addCourse.setObjectName("addCourse")
        addCourse.resize(659, 686)
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

        
        self.instructorLabel = QtWidgets.QLabel(self.classDetails)
        self.instructorLabel.setGeometry(QtCore.QRect(60, 460, 121, 21))
        self.instructorLabel.setObjectName("instructorLabel")
        self.instructor = QtWidgets.QLineEdit(self.classDetails)
        self.instructor.setGeometry(QtCore.QRect(200, 460, 251, 22))
        self.instructor.setObjectName("instructor")
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
        self.saveCourse = QtWidgets.QPushButton(addCourse)
        self.saveCourse.setGeometry(QtCore.QRect(270, 560, 101, 31))
        self.saveCourse.setObjectName("saveCourse")
        
        
        self.retranslateUi(addCourse)
        
        #=====================
        self.addDepartmentsToLists()
        self.updateLists()
        self.theoreticalSettings()
        #=====================
        
        #============Event Handling===========

        self.instructorDepartment.currentTextChanged.connect(self.addTeachersToCompleter)
        self.labDepartment.currentTextChanged.connect(self.addLabsToList)
        self.courseCode.textChanged['QString'].connect(self.setCourseNameAndCode)
        self.courseName.textChanged['QString'].connect(self.searchAndSetCourseByName)
        self.theory.toggled.connect(self.theoreticalSettings)
        self.lab.toggled.connect(self.practicalSettings)

        self.saveCourse.clicked.connect(self.saveCourseData)
               
        QtCore.QMetaObject.connectSlotsByName(addCourse)
        addCourse.setTabOrder(self.courseCode, self.courseName)
        addCourse.setTabOrder(self.courseName, self.theory)
        addCourse.setTabOrder(self.theory, self.lab)
        addCourse.setTabOrder(self.lab, self.contactHour)
        addCourse.setTabOrder(self.contactHour, self.totalCH)
        addCourse.setTabOrder(self.totalCH, self.instructor)

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
        self.instructorLabel.setText(_translate("addCourse", "Instructor :"))
        self.instructorsDepartmentLabel.setText(_translate("addCourse", "Instructors Department:"))
        self.labDepartmentLabel.setText(_translate("addCourse", "Lab Department:"))
        self.labNameLabel.setText(_translate("addCourse", "Lab Name:"))
        self.saveCourse.setText(_translate("addCourse", "Save Course"))

    def updateLists(self):
        self.instructorDepartment.setCurrentText(self.newSemester.getDepartment())
        self.labDepartment.setCurrentText(self.newSemester.getDepartment())
        self.addTeachersToCompleter()            
        self.addLabsToList()

    def addTeachersToCompleter(self):
        self.instructor.clear()
        import teacher
        t = teacher.readAllTeachersOfDepartment(self.instructorDepartment.currentText())
        self.instructor.setCompleter(self.instructorCompleter)
        self.instructorModel.setStringList(t)
        
    def addLabsToList(self):
        self.labName.clear()
        import lab
        t = lab.readAllLabsOfDepartment(self.labDepartment.currentText())
        for i in range(len(t)):
            self.labName.addItem('%s'%(t[i]))            


    def addDepartmentsToLists(self):
        import Filer
        d = Filer.listAllDepartments()
        for i in range(len(d)):
            temp = '%s'%(d[i])
            self.instructorDepartment.addItem(temp)
            self.labDepartment.addItem(temp)
            
    def setCourseNameAndCode(self):
        import course
        results = course.searchCourseCodeLike(self.courseCode.text())
        self.courseCode.setCompleter(self.courseCompleter)
        self.courseModel.setStringList(results)
        
        if ( (not self.courseCode.text().isspace())
             and (len(self.courseCode.text()) != 0)):
            self.newCourse.setCodeAndName(self.courseCode.text())
            self.courseName.setText(self.newCourse.getName())
            import TimeTable
            if(self.newCourse.getName().endswith(TimeTable.theDefaultLabChars())):
                self.lab.setChecked(True)
            else:
                self.theory.setChecked(True)

    def searchAndSetCourseByName(self):
        import course
        results = course.searchCourseNameLike(self.courseName.text())
        self.courseName.setCompleter(self.courseCompleter)
        self.courseModel.setStringList(results)
        
        if ( (not self.courseName.text().isspace())
             and (len(self.courseName.text()) != 0)):
            self.newCourse.setNameAndCode(self.courseName.text())
            self.courseCode.setText(self.newCourse.getCode())
            import TimeTable
            if(self.newCourse.getName().endswith(TimeTable.theDefaultLabChars())):
                self.lab.setChecked(True)
            else:
                self.theory.setChecked(True)
 
        
    def saveCourseData(self):
        
        import Semester
        import TimeTable
        if(self.lab.isChecked()):
            import lab
            lab.assignLab(self.newCourse.getCode(),
                          self.newSemester.getClassName(), self.labName.currentText())
            
        self.newSemester.addCourse(
            self.newCourse,self.contactHour.value(), self.totalCH.value())

        import teacher
        t = self.instructor.text().split(' : ')
        theTeacher = teacher.Teacher(t[1], t[0],
                                     self.instructorDepartment.currentText())
        teacher.assignTeacher(self.newCourse.getCode(),
                              self.newSemester.getClassName(),theTeacher)
        
        self.courseName.clear()
        self.courseCode.clear()
        self.instructor.clear()
        self.theory.setChecked(True)

            
    def theoreticalSettings(self):
        if(self.theory.isChecked()):
            self.contactHour.setValue(1)
            self.totalCH.setValue(3)
            self.labDepartment.setEnabled(False)
            self.labName.setEnabled(False)
            
    def practicalSettings(self):
        if(self.lab.isChecked()):
            
            self.contactHour.setValue(3)
            self.totalCH.setValue(1)
            self.labDepartment.setEnabled(True)
            self.labName.setEnabled(True)




'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addCourse = QtWidgets.QDialog()
    ui = Ui_addCourse()
    ui.setupUi(addCourse)
    addCourse.show()
    sys.exit(app.exec_())
'''

