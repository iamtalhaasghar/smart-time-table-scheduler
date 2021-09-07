def addCourse(department,degree,className,courseCode,subject, oneCreditHour, creditHour):
    
    import TimeTable
    import Teacher

    '''
    if(s.endswith(TimeTable.theDefaultLabChars())):
        import Lab
        Lab.selectLab(s)
    else:
    '''
    contactMins = (creditHour * oneCreditHour) * 60
    
    import Filer
    folder = Filer.createDegreeProgramFolder(department,degree)
    
    import os
    p ='%s/%s.csv'% (folder,className)
    import pandas as pd
    
    if(os.path.exists(p)):
        courses = readClass(department, degree, className)
        courses = courses.T
        courses.insert(len(courses.columns),courseCode,[subject,creditHour,contactMins])
        courses = courses.T
    else:
        
        data = {'Subjects':[subject], 'CH':[creditHour],'CM':[contactMins]}
        courses = pd.DataFrame(data, index=[courseCode])
        courses = courses.rename_axis('CourseCode')
        
    courses.to_csv('%s' % p)


def readClass(department, degree, className):
    'ClassName whose data is to be read'
    import Filer
    import os
    file = '%s/%s/%s/%s.csv' % (Filer.DATA_FOLDER, department, degree, className)
    if(not os.path.exists(file)):
        print('Path %s does not exists.'%(file))
        input('TODO: Excpetion')

    import pandas as pd
    data = pd.read_csv('%s'%(file))
    data = data.set_index('CourseCode')
    return data
