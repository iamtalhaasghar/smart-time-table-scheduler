# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'general_settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_generalSettingsWindow(object):
    def setupUi(self, generalSettingsWindow):
        generalSettingsWindow.setObjectName("generalSettingsWindow")
        generalSettingsWindow.resize(881, 795)
        self.generalSettings = QtWidgets.QWidget(generalSettingsWindow)
        self.generalSettings.setObjectName("generalSettings")
        self.saveButton = QtWidgets.QCommandLinkButton(self.generalSettings)
        self.saveButton.setGeometry(QtCore.QRect(710, 710, 151, 41))
        self.saveButton.setObjectName("saveButton")
        self.basicInformation = QtWidgets.QGroupBox(self.generalSettings)
        self.basicInformation.setGeometry(QtCore.QRect(20, 10, 831, 401))
        self.basicInformation.setObjectName("basicInformation")
        self.gridLayoutWidget = QtWidgets.QWidget(self.basicInformation)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 801, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.durationOfBreak = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.durationOfBreak.setEnabled(True)
        self.durationOfBreak.setMinimum(3)
        self.durationOfBreak.setMaximum(1440)
        self.durationOfBreak.setProperty("value", 15)
        self.durationOfBreak.setObjectName("durationOfBreak")
        self.gridLayout.addWidget(self.durationOfBreak, 4, 2, 1, 1)
        self.endTime = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.endTime.setTime(QtCore.QTime(23, 0, 0))
        self.endTime.setObjectName("endTime")
        self.gridLayout.addWidget(self.endTime, 1, 4, 1, 1)
        self.startTime = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.startTime.setTime(QtCore.QTime(5, 0, 0))
        self.startTime.setObjectName("startTime")
        self.gridLayout.addWidget(self.startTime, 1, 2, 1, 1)
        self.institutionName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.institutionName.setObjectName("institutionName")
        self.gridLayout.addWidget(self.institutionName, 0, 2, 1, 1)
        self.periodDurationLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.periodDurationLabel.setObjectName("periodDurationLabel")
        self.gridLayout.addWidget(self.periodDurationLabel, 2, 0, 1, 1)
        self.startTimeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.gridLayout.addWidget(self.startTimeLabel, 1, 0, 1, 1)
        self.endTimeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.endTimeLabel.setObjectName("endTimeLabel")
        self.gridLayout.addWidget(self.endTimeLabel, 1, 3, 1, 1)
        self.breakYes = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.breakYes.setChecked(True)
        self.breakYes.setObjectName("breakYes")
        self.gridLayout.addWidget(self.breakYes, 3, 2, 1, 1)
        self.breakNo = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.breakNo.setChecked(False)
        self.breakNo.setObjectName("breakNo")
        self.gridLayout.addWidget(self.breakNo, 3, 3, 1, 1)
        self.durationOfPeriod = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.durationOfPeriod.setMinimum(30)
        self.durationOfPeriod.setMaximum(1440)
        self.durationOfPeriod.setProperty("value", 90)
        self.durationOfPeriod.setObjectName("durationOfPeriod")
        self.gridLayout.addWidget(self.durationOfPeriod, 2, 2, 1, 1)
        self.breakLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.breakLabel.setObjectName("breakLabel")
        self.gridLayout.addWidget(self.breakLabel, 3, 0, 1, 1)
        self.durationOfBreakLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.durationOfBreakLabel.setEnabled(True)
        self.durationOfBreakLabel.setObjectName("durationOfBreakLabel")
        self.gridLayout.addWidget(self.durationOfBreakLabel, 4, 0, 1, 1)
        self.institutionNameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.institutionNameLabel.setObjectName("institutionNameLabel")
        self.gridLayout.addWidget(self.institutionNameLabel, 0, 0, 1, 1)
        self.firstWorkingDayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.firstWorkingDayLabel.setObjectName("firstWorkingDayLabel")
        self.gridLayout.addWidget(self.firstWorkingDayLabel, 5, 0, 1, 1)
        self.firstWorkingDay = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.firstWorkingDay.setObjectName("firstWorkingDay")
        self.firstWorkingDay.addItem("")
        self.firstWorkingDay.addItem("")
        self.firstWorkingDay.addItem("")
        self.firstWorkingDay.addItem("")
        self.firstWorkingDay.addItem("")
        self.firstWorkingDay.addItem("")
        self.firstWorkingDay.addItem("")
        self.gridLayout.addWidget(self.firstWorkingDay, 5, 2, 1, 1)
        generalSettingsWindow.setCentralWidget(self.generalSettings)
        self.menubar = QtWidgets.QMenuBar(generalSettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        generalSettingsWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(generalSettingsWindow)
        self.breakNo.toggled['bool'].connect(self.durationOfBreak.setDisabled)
        self.saveButton.clicked.connect(self.saveData)
        self.breakYes.toggled['bool'].connect(self.durationOfBreakLabel.setEnabled)
        self.breakNo.toggled['bool'].connect(self.durationOfBreakLabel.setDisabled)
        self.breakYes.toggled['bool'].connect(self.durationOfBreak.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(generalSettingsWindow)
        generalSettingsWindow.setTabOrder(self.institutionName, self.startTime)
        generalSettingsWindow.setTabOrder(self.startTime, self.endTime)
        generalSettingsWindow.setTabOrder(self.endTime, self.durationOfPeriod)
        generalSettingsWindow.setTabOrder(self.durationOfPeriod, self.breakYes)
        generalSettingsWindow.setTabOrder(self.breakYes, self.breakNo)
        generalSettingsWindow.setTabOrder(self.breakNo, self.durationOfBreak)

    def retranslateUi(self, generalSettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        generalSettingsWindow.setWindowTitle(_translate("generalSettingsWindow", "General Settings"))
        self.saveButton.setText(_translate("generalSettingsWindow", "Save and Next"))
        self.basicInformation.setTitle(_translate("generalSettingsWindow", "Basic Information"))
        self.durationOfBreak.setSuffix(_translate("generalSettingsWindow", "  Minutes"))
        self.institutionName.setText(_translate("generalSettingsWindow", "Khwaja Fareed University of Engineering & IT"))
        self.periodDurationLabel.setText(_translate("generalSettingsWindow", "Duration of a Period:"))
        self.startTimeLabel.setText(_translate("generalSettingsWindow", "Start Time:"))
        self.endTimeLabel.setText(_translate("generalSettingsWindow", "End Time: "))
        self.breakYes.setText(_translate("generalSettingsWindow", "Yes"))
        self.breakNo.setText(_translate("generalSettingsWindow", "No"))
        self.durationOfPeriod.setSuffix(_translate("generalSettingsWindow", "  Minutes"))
        self.breakLabel.setText(_translate("generalSettingsWindow", "Break:"))
        self.durationOfBreakLabel.setText(_translate("generalSettingsWindow", "Duration of Break:"))
        self.institutionNameLabel.setText(_translate("generalSettingsWindow", "Institution Name: "))
        self.firstWorkingDayLabel.setText(_translate("generalSettingsWindow", "First Working Day:"))
        self.firstWorkingDay.setItemText(0, _translate("generalSettingsWindow", "Mon"))
        self.firstWorkingDay.setItemText(1, _translate("generalSettingsWindow", "Tue"))
        self.firstWorkingDay.setItemText(2, _translate("generalSettingsWindow", "Wed"))
        self.firstWorkingDay.setItemText(3, _translate("generalSettingsWindow", "Thu"))
        self.firstWorkingDay.setItemText(4, _translate("generalSettingsWindow", "Fri"))
        self.firstWorkingDay.setItemText(5, _translate("generalSettingsWindow", "Sat"))
        self.firstWorkingDay.setItemText(6, _translate("generalSettingsWindow", "Sun"))
        self.menuAbout.setTitle(_translate("generalSettingsWindow", "About"))

    # These lines of codes were not generated by pyuic
    def saveData(self):
        'Saves data of general settings window'
        import GuiParser
        folder = GuiParser.createSettingsFolder()
        f=open('%s/%s.txt'%(folder,'GeneralSettings'),'w')
        f.write('InstitutionName==%s\n'%(self.institutionName.text()))
        f.write('StartTime==%s\n'%(self.startTime.time().toPyTime()))
        f.write('EndTime==%s\n'%(self.endTime.time().toPyTime()))
        f.write('PeriodDuration==%s\n'%(self.durationOfPeriod.value()))
        if(self.breakYes.isChecked()):
            f.write('BreakDuration==%s\n'%(self.durationOfBreak.value()))
        else:
            f.write('BreakDuration==%d\n'%(0))
        f.write('FirstWorkingDay==%s\n'%(self.firstWorkingDay.currentText()))
        f.close()
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    generalSettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_generalSettingsWindow()
    ui.setupUi(generalSettingsWindow)
    generalSettingsWindow.show()
    sys.exit(app.exec_())

