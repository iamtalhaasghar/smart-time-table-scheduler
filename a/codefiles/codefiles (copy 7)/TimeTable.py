def createTimeTable():
    
    import Timing
    periods = Timing.makePeriods()

    import Room
    import Lab
    allRooms = Room.readAllRooms().Name
    allLabs = Lab.readAllLabs().Name

    combinedRoom = list()
    combinedRoom.extend(allRooms)
    combinedRoom.extend(allLabs)
    
    days = list()
    for i in Timing.daysOfWeek():
        for j in range(0, len(combinedRoom)):
            days.append(i)

    room = list()
    for i in range(0,len(Timing.daysOfWeek())):
        room.extend(combinedRoom)

    import pandas as pd
    dataF = pd.DataFrame(index = [days,room],columns = ['P%s'%(i) for i in range(1,len(periods)+1)])
    dataF = dataF.rename_axis(['Days','Rooms'], axis = 'index')
    dataF = dataF.fillna(theDefaultEmptyChar())
    
    import Filer
    folder = Filer.createTimeTableFolder()
    dataF.to_csv('%s/%sFormat.csv'%(folder, Filer.TIME_TABLE_FILE_NAME))
    dataF.to_csv('%s/%s.csv'%(folder, Filer.TIME_TABLE_FILE_NAME))

def readTimeTable():
    import Filer
    fileName = '%s/%s.csv' % (Filer.TIME_TABLE_FOLDER, Filer.TIME_TABLE_FILE_NAME)
    import pandas as pd
    data = pd.read_csv(fileName)
    data = data.set_index(['Days','Rooms'])
    return data


def theDefaultEmptyChar():
    return '#'
def theDefaultLabChars():
    return 'LAB'
def readTimeHeaders():
    import os
    import Filer
    p = '%s/%s' % (Filer.DATA_FOLDER, Filer.TIME_HEADER_FILE_NAME)
    if(not os.path.exists(p)):
        print('Path %s does not exists.'%(p))
        input('TODO: Exception')
    timeList = list()
    with open(p,'r') as f:
        data = f.read()
        timeList = eval(data)
        timeList.insert(0,'')
    return timeList

def putDollarsForNextPeriods(timeTable,className,subjectCode,subject
                             ,day, room, period,startTime,endTime):
    import Timing
    timeList = readTimeHeaders()
    periodList = list(timeTable.columns)
    currentEndTime = Timing.toMin(timeList[int(period[-1])].split('-')[1])
    if(currentEndTime < Timing.toMin(endTime)):
        nextPeriod = (periodList.index(period)) + 1

        if(nextPeriod >= len(timeTable.columns)):
            return False
        nextPeriodName = periodList[nextPeriod]

        import TimeTable
        if(timeTable.loc[(day,room),nextPeriodName] != TimeTable.theDefaultEmptyChar()):
            return False

        # Clash Resolve
        import Duplicates
        import Teacher
        teacherName = Teacher.findTeacherOfSubject(subjectCode,className)
        if((Duplicates.doesClassClashExist(timeTable, day, period, className)) or
            (Duplicates.doesTeacherClashExist(timeTable, day,period, teacherName))):
                 return False

        if(putDollarsForNextPeriods(
            timeTable, className, subjectCode, subject, day, room,
            nextPeriodName,startTime,endTime)):
                import Teacher
                teacherName = Teacher.findTeacherOfSubject(subjectCode,className)
                timeTable.loc[(day,room), nextPeriodName] = str(
                    [className,'%s-%s'%(period[-1],subject),teacherName,'%s-%s'%(startTime,endTime)])
        else:
            return False
    return True

def allotLab(timeTable,className,subject,duration):
    
    import Lab
    import Timing
    import Teacher
    timeList = readTimeHeaders()
    uniEndTime = Timing.toMin(timeList[-1].split('-')[1])

    labName = Lab.findLabOfSubject(subject[0],className)

    for l in list(Lab.readAllLabs().Name):
        for p in timeTable.columns:
            for d in Timing.daysOfWeek():
                
                if(labName == l and (timeTable.loc[(d,l),p] == theDefaultEmptyChar())):
                    teacherName = Teacher.findTeacherOfSubject(subject[0],className)
                    # Clash Resolves
                    import Duplicates
                    if((Duplicates.doesClassClashExist(timeTable, d, p, className)) or
                       (Duplicates.doesTeacherClashExist(timeTable, d,p, teacherName))):
                            continue
                    #---------------
                    s = timeList[int(p[-1])].split('-')[0]
                    e = Timing.toMin(s) + subject[2]
                    if(e > uniEndTime):
                        continue
                    
                    e = Timing.toHour(e)
                    if(subject[2] <= duration):
                        timeTable.loc[(d,l),p] = [
                            className,subject[1],teacherName,('%s-%s'%(s,e))]
                        return True
                    else:
                        if(putDollarsForNextPeriods(
                            timeTable,className,subject[0],subject[1],d,l,p,s,e)):
                            timeTable.loc[(d,l),p] = [
                                className,subject[1],teacherName,('%s-%s'%(s,e))]
                        else:
                            continue
                        return True
    return False
                
def generateTimeTable(department, degree, className):
    'class whose timetable is to be generated'

    import Filer
    duration = int(Filer.readGeneralSettingsFile('PeriodDuration'))
    import pandas as pd
    import Semester
    import Teacher
    timeTable = readTimeTable()
    courseTable = Semester.readClass(department, degree, className)

    subjects = list()   # [courseCode, courseName, duration]

    for i in courseTable.index:
        tempSubject = courseTable.loc[i,'Subjects']
        creditMin = courseTable.loc[i,'CM']
        if(tempSubject.endswith(theDefaultLabChars())):
            subjects.append([i,tempSubject,creditMin])
            continue
        while(creditMin != 0):
            if(creditMin == duration):
                subjects.append([i,tempSubject,duration])
                creditMin -= duration
            elif(creditMin > duration):
                if((creditMin-duration) >= duration):
                    subjects.append([i,tempSubject,duration])
                    creditMin -= duration
                else:
                    subjects.append([i,tempSubject,creditMin])
                    creditMin -= creditMin
            else:
                subjects.append([i,tempSubject, creditMin])
                creditMin -= creditMin
                
    import Timing
    timeList = readTimeHeaders()
    uniEndTime = Timing.toMin(timeList[-1].split('-')[1])
    import random
    random.shuffle(subjects)
    import Room
    
    for r in list(Room.readAllRooms().Name):
        for p in timeTable.columns:
                for d in Timing.daysOfWeek():
                    if((len(subjects)!=0)):
                        temp = subjects[-1]
                        if(temp[1].endswith(theDefaultLabChars())):
                            if(allotLab(timeTable,className,temp,duration)):
                                temp = subjects.pop()
                            else:
                                print('Not enough labs...')
                                return
                            continue
                        teacherName = Teacher.findTeacherOfSubject(temp[0],className)
                        if((timeTable.loc[(d,r),p] == theDefaultEmptyChar())):
                            # Clash Resolves
                            import Duplicates
                            if((Duplicates.doesClassClashExist(timeTable, d, p, className)) or
                               (Duplicates.doesTeacherClashExist(timeTable, d,p, teacherName))):
                                    continue
                            #---------------
                            
                            s = timeList[int(p[-1])].split('-')[0]
                            e = Timing.toMin(s) + temp[2]
                            if(e > uniEndTime):
                                continue
                            e = Timing.toHour(e)
                            
                            if(temp[2] <= duration):
                                timeTable.loc[(d,r),p] = [
                                    className,temp[1],teacherName,('%s-%s'%(s,e))]
                            else:
                                if(putDollarsForNextPeriods(
                                    timeTable,className,temp[0],temp[1],d,r,p,s,e)):
                                    timeTable.loc[(d,r),p] = [
                                        className,temp[1],teacherName,('%s-%s'%(s,e))]
                                else:
                                    continue
                            temp = subjects.pop()
                                 
                                
    if(len(subjects)!=0):
        print('Not enough rooms...')
        
    import Filer
    timeTable.to_csv('%s/%s.csv'%(Filer.TIME_TABLE_FOLDER, Filer.TIME_TABLE_FILE_NAME))
    timeTable.to_html('%s/%s.html'%(Filer.TIME_TABLE_FOLDER, Filer.TIME_TABLE_FILE_NAME))
