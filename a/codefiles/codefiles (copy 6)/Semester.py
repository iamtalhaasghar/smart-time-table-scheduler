def makeClass():
    
    className = input('Class Name: ')
    creditHours = list()
    subjects = list()
    contactMins = list()
    oneCreditHour = 1

    s = input('Enter Subject (q = quit) : ')
    import math
    import Timing
    import TimeTable
    import Teacher
    while (s!='q'):
        c = int(input('Enter Credit Hours : '))
        if(s.endswith(TimeTable.theDefaultLabChars())):
            oneCreditHour = 3
            import Lab
            Lab.selectLab(s)
        else:
            oneCreditHour = 1
        Teacher.selectTeacher(s)
        totalContactMins = (c * oneCreditHour) * 60
        subjects.append(s)
        creditHours.append(c)
        contactMins.append(totalContactMins)
        s = input('Enter Subject (q = quit) : ')
        
    data = {'Subjects':subjects, 'CH':creditHours,'CM':contactMins}
    import pandas as pd
    courses = pd.DataFrame(data, index = [i for i in range(1, len(subjects)+1)])
    courses = courses.rename_axis('Serial')
    import Filer
    folder = Filer.createFolder('classes')
    courses.to_csv('%s/%s.csv'%(folder,className))
    
def readClass(className):
    'ClassName whose data is to be read'
    import os
    file = '%s/classes/%s.csv' % (os.getcwd(),className)
    if(not os.path.exists(file)):
        print('Path %s does not exists.'%(p))
        input('TODO: Excpetion')

    import pandas as pd
    data = pd.read_csv('%s'%(file))
    data = data.set_index('Serial')
    return data

