def addTeachers():
    teacher = input('Enter Teacher Name (q=quit): ')
    teacherList = list()
    while(teacher != 'q'):
        teacherList.append(teacher)
        teacher = input('Enter Teacher name (q=quit): ')
    data = {'Name':teacherList}

    import pandas as pd
    teacherData = pd.DataFrame(data = data, index = [i for i in range(1, len(teacherList)+1)])
    teacherData = teacherData.rename_axis('Serial')
    teacherData.to_csv('teachers/teachers.csv')

def readAllTeachers():
    import pandas as pd
    data = pd.read_csv('teachers/teachers.csv')
    data = data.set_index('Serial')
    return data

def selectTeacher(subject):
    teachersData = readAllTeachers()
    allTeachers = list(teachersData.Name)
    for i in range(len(allTeachers)):
        print('%d : %s' %(i+1, allTeachers[i]))
    teacher = int(input('Select Teacher: '))
    teacher = allTeachers[teacher-1]
    
    teacherDataFrame = readTeacherManagementFile()
    teacherDataFrame = teacherDataFrame.T
    teacherDataFrame.insert(len(teacherDataFrame.columns),subject,teacher)
    teacherDataFrame = teacherDataFrame.T
    teacherDataFrame.to_csv('timetables/teachermanagement.csv')

def makeTeacherManagementFile():
    import pandas as pd
    teacherDataFrame = pd.DataFrame(data = {'Teacher':[],'Subject':[]})
    teacherDataFrame = teacherDataFrame.set_index('Subject')
    teacherDataFrame.to_csv('timetables/teachermanagement.csv')
    
def readTeacherManagementFile():
    import pandas as pd
    teacherDataFrame = pd.read_csv('timetables/teachermanagement.csv')
    teacherDataFrame = teacherDataFrame.set_index('Subject')
    return teacherDataFrame

def findTeacherOfSubject(subject):
    dataF = readTeacherManagementFile()
    return dataF.loc[subject,'Teacher']
