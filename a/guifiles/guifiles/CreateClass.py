# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_class.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class Ui_createClass(object):

    def __init__(self):
        from Semester import Semester
        self.newClass = Semester()
    
    def setupUi(self, createClass):
        createClass.setObjectName("createClass")
        createClass.resize(659, 736)
        self.classDetails = QtWidgets.QGroupBox(createClass)
        self.classDetails.setGeometry(QtCore.QRect(40, 30, 571, 581))
        self.classDetails.setObjectName("classDetails")
        self.classNameLabel = QtWidgets.QLabel(self.classDetails)
        self.classNameLabel.setGeometry(QtCore.QRect(60, 100, 81, 16))
        self.classNameLabel.setObjectName("classNameLabel")
        self.className = QtWidgets.QLineEdit(self.classDetails)
        self.className.setGeometry(QtCore.QRect(160, 100, 291, 20))
        self.className.setObjectName("className")
        self.courseCodeLabel = QtWidgets.QLabel(self.classDetails)
        self.courseCodeLabel.setGeometry(QtCore.QRect(60, 140, 81, 16))
        self.courseCodeLabel.setText("")
        self.courseCodeLabel.setObjectName("courseCodeLabel")
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
        self.classCoursesDetails = QtWidgets.QTextBrowser(self.classDetails)
        self.classCoursesDetails.setGeometry(QtCore.QRect(40, 180, 491, 391))
        self.classCoursesDetails.setObjectName("classCoursesDetails")
        self.addCourse = QtWidgets.QPushButton(self.classDetails)
        self.addCourse.setGeometry(QtCore.QRect(240, 140, 75, 23))
        self.addCourse.setObjectName("addCourse")
        
        self.saveClass = QtWidgets.QPushButton(createClass)
        self.saveClass.setGeometry(QtCore.QRect(290, 660, 101, 31))
        self.saveClass.setObjectName("saveClass")

        self.retranslateUi(createClass)        
        
        self.addDepartmentsToList()
        self.updateLists()
        self.department.currentTextChanged.connect(self.updateLists)
        self.addCourse.clicked.connect(self.showAddCourseWindow)
        self.saveClass.clicked.connect(self.createClass)
        
        QtCore.QMetaObject.connectSlotsByName(createClass)

    def retranslateUi(self, createClass):
        _translate = QtCore.QCoreApplication.translate
        createClass.setWindowTitle(_translate("createClass", "Create Class"))
        self.classDetails.setTitle(_translate("createClass", "Class Details"))
        self.classNameLabel.setText(_translate("createClass", "Class Name:"))
        self.departmentLabel.setText(_translate("createClass", "Department : "))
        self.department.setToolTip(_translate("createClass", "Select"))
        self.degreeProgramLabel.setText(_translate("createClass", "Deegre Program:"))
        self.addCourse.setText(_translate("createClass", "Add Course"))
        self.saveClass.setText(_translate("createClass", "CreateClass"))


    def updateLists(self):
        self.addProgramsToList()


    def addDepartmentsToList(self):
        import Filer
        d = Filer.listAllDepartments()
        for i in range(len(d)):
            temp = '%s'%(d[i])
            self.department.addItem(temp)

    def addProgramsToList(self):
        self.degreeProgram.clear()
        import degree
        p = degree.programsOfDepartment(self.department.currentText())
        for i in range(len(p)):
            self.degreeProgram.addItem('%s'%(p[i])) 

       
    def showAddCourseWindow(self):
        self.updateClassFields()
        if(len(self.className.text()) == 0):
            QMessageBox.information(None,"No Class Name" ,
                                    "Please Enter a class name.")
        else:    
        
            import AddCourse
            self.addCourse = QtWidgets.QDialog()
            self.ui = AddCourse.Ui_addCourse(self.newClass)
            self.ui.setupUi(self.addCourse)
            self.addCourse.show()
            self.classCoursesDetails.clear()
            self.classCoursesDetails.setText(self.newClass.getCoursesString())
            
    def createClass(self):
        self.updateClassFields()
        self.newClass.saveToDatabase()

    def updateClassFields(self):
        self.newClass.setDepartment(self.department.currentText())
        self.newClass.setDegree(self.degreeProgram.currentText())
        self.newClass.setClassName(self.className.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createClass = QtWidgets.QDialog()
    ui = Ui_createClass()
    ui.setupUi(createClass)
    createClass.show()
    sys.exit(app.exec_())

