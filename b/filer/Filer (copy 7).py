import os
CURRENT_FOLDER = os.getcwd()
DATA_FOLDER = CURRENT_FOLDER + '/data'
SETTINGS_FOLDER = CURRENT_FOLDER + '/settings'
SETTINGS_FILE_NAME = 'GeneralSettings.txt'
LAB_FILE_NAME = 'Labs.csv'
TEACHER_FILE_NAME = 'Teachers.csv'
ROOM_FILE_NAME = 'Rooms.csv'
LAB_MANAGEMENT_FILE_NAME = 'LabManagement.csv'
TEACHER_MANAGEMENT_FILE_NAME = 'TeacherManagement.csv'
TIME_HEADER_FILE_NAME = 'TimeHeader.txt'
TIME_TABLE_FOLDER = CURRENT_FOLDER + '/timetables'
TIME_TABLE_FILE_NAME = 'TimeTable'


def createTimeTableFolder():
    
    import os
    target = TIME_TABLE_FOLDER
    if(not os.path.exists(target)):
        os.mkdir(target)
    return target

def createDataFolder():
    
    import os
    target = DATA_FOLDER
    if(not os.path.exists(target)):
        os.mkdir(target)
        import Teacher
        import Lab
        Teacher.makeTeacherManagementFile()
        Lab.makeLabManagementFile()
    return target

def createSettingsFolder():
    
    import os
    target = SETTINGS_FOLDER
    if(not os.path.exists(target)):
        os.mkdir(target)
    return target

def createDepartmentFolder(departmentName):
    import os
    target = '%s/%s' % (DATA_FOLDER, departmentName)
    if(not os.path.exists(target)):
        os.mkdir(target)
    return target

def createDegreeProgramFolder(departmentName,degree):
    import os
    target = '%s/%s' % (createDepartmentFolder(departmentName),degree)
    if(not os.path.exists(target)):
        os.mkdir(target)
    return target

def listAllDepartments():
    import os
    'TODO: if path does not exists...'
    folders = os.listdir(DATA_FOLDER)
    departs = list()
    for i in folders:
        if(os.path.isdir('%s/%s'%(DATA_FOLDER,i))):
            departs.append(i)
    departs.sort()
    return tuple(departs)

def programsOfDepartment(department):
    import os
    p = '%s/%s'%(DATA_FOLDER,department)
    'TODO: if path does not exists...'
    folders = os.listdir(p)
    programs = list()
    for i in folders:
        if(os.path.isdir('%s/%s'%(p,i))):
            programs.append(i)
    programs.sort()
    return tuple(programs)

def readGeneralSettingsFile(request):
    import os
    settings = SETTINGS_FOLDER + '/' + SETTINGS_FILE_NAME
    
    if(not os.path.exists(settings)):
        print('Path %s does not exists'%(settings))
        input('TODO: Exception should be raised here....')        
    else:
        f = open(settings,'r')
        tokens = f.readline().strip()
        for l in f:
            if(l.startswith('%s'%(request))):
                t  = l.strip().split('%s'%(tokens))
                return t[-1]
    print('Nothing found about %s in generalSettingsfile...'%(request))
    input('TODO: Exception')        
    return None
