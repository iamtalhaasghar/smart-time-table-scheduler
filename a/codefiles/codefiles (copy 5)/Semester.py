    
def addCourse(className,courseCode,subject, oneCreditHour, creditHour):
    
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
    folder = Filer.createFolder('classes')
    
    import os
    p ='%s/%s.csv'% (folder,className)
    import pandas as pd
    
    if(os.path.exists(p)):
        courses = readClass(className)
        courses = courses.T
        courses.insert(len(courses.columns),courseCode,[subject,creditHour,contactMins])
        courses = courses.T
    else:
        
        data = {'Subjects':[subject], 'CH':[creditHour],'CM':[contactMins]}
        courses = pd.DataFrame(data, index=[courseCode])
        courses = courses.rename_axis('CourseCode')
        
    courses.to_csv('%s' % p)
    
def readClass(className):
    'ClassName whose data is to be read'
    import os
    file = '%s/classes/%s.csv' % (os.getcwd(),className)
    if(not os.path.exists(file)):
        print('Path %s does not exists.'%(p))
        input('TODO: Excpetion')

    import pandas as pd
    data = pd.read_csv('%s'%(file))
    data = data.set_index('CourseCode')
    return data

