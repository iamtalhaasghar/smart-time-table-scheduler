def createTimeTable():
    import timing
    periods = timing.makePeriods()

    import room
    import lab
    allRooms = room.readAllRooms().Name
    allLabs = lab.readAllLabs().Name

    combinedRoom = list()
    combinedRoom.extend(allRooms)
    combinedRoom.extend(allLabs)
    
    days = list()
    for i in timing.daysOfWeek():
        for j in range(0, len(combinedRoom)):
            days.append(i)

    room = list()
    for i in range(0,len(timing.daysOfWeek())):
        room.extend(combinedRoom)

    import pandas as pd
    dataF = pd.DataFrame(index = [days,room],columns = ['P%s'%(i) for i in range(1,len(periods)+1)])
    dataF = dataF.rename_axis(['Days','Rooms'], axis = 'index')
    dataF = dataF.fillna(theDefaultEmptyChar())
    dataF.to_csv('timetables/TimeTable.csv')
    dataF.to_html('timetables/TimeTable.html')

def readTimeTable(fileName='timetables/TimeTable.csv'):
    import pandas as pd
    data = pd.read_csv(fileName)
    data = data.set_index(['Days','Rooms'])
    return data


def theDefaultEmptyChar():
    return '#'
def theDefaultLabChars():
    return 'LAB'
def readTimeHeaders():
    timeList = list()
    with open('timetables/timeHeader.txt') as f:
        data = f.read()
        timeList = eval(data)
        timeList.insert(0,'')
    return timeList

def putDollarsForNextPeriods(timeTable,className,subject,day, room, period,startTime,endTime):
    import timing
    timeList = readTimeHeaders()
    periodList = list(timeTable.columns)
    currentEndTime = timing.toMin(timeList[int(period[-1])].split('-')[1])
    if(currentEndTime < timing.toMin(endTime)):
        nextPeriod = (periodList.index(period)) + 1

        if(nextPeriod >= len(timeTable.columns)):
            return False
        nextPeriodName = periodList[nextPeriod]

        import TimeTable
        if(timeTable.loc[(day,room),nextPeriodName] != TimeTable.theDefaultEmptyChar()):
            return False

        # Clash Resolve
        import duplicates
        import teacher
        teacherName = teacher.findTeacherOfSubject(subject)
        if((duplicates.doesClassClashExist(timeTable, day, period, className)) or
            (duplicates.doesTeacherClashExist(timeTable, day,period, teacherName))):
                 return False

        if(putDollarsForNextPeriods(
            timeTable, className, subject, day, room, nextPeriodName,startTime,endTime)):
                import teacher
                teacherName = teacher.findTeacherOfSubject(subject)
                timeTable.loc[(day,room), nextPeriodName] = str(
                    [className,'%s-%s'%(period[-1],subject),teacherName,'%s-%s'%(startTime,endTime)])
        else:
            return False
    return True

def allotLab(timeTable,className,subject,duration):

    import lab
    import timing
    import teacher
    timeList = readTimeHeaders()
    uniEndTime = timing.toMin(timeList[-1].split('-')[1])
    labName = lab.findLabOfSubject(subject[0])
    for l in list(lab.readAllLabs().Name):
        for p in timeTable.columns:
            for d in timing.daysOfWeek():
                if(labName == l and (timeTable.loc[(d,l),p] == theDefaultEmptyChar())):

                    teacherName = teacher.findTeacherOfSubject(subject[0])
                    # Clash Resolves
                    import duplicates
                    if((duplicates.doesClassClashExist(timeTable, d, p, className)) or
                       (duplicates.doesTeacherClashExist(timeTable, d,p, teacherName))):
                            continue
                    #---------------
                    s = timeList[int(p[-1])].split('-')[0]
                    e = timing.toMin(s) + subject[1]
                    if(e > uniEndTime):
                        continue
                    
                    e = timing.toHour(e)
                    if(subject[1] <= duration):
                        timeTable.loc[(d,l),p] = [
                            className,subject[0],teacherName,('%s-%s'%(s,e))]
                        return True
                    else:
                        if(putDollarsForNextPeriods(
                            timeTable,className,subject[0],d,l,p,s,e)):
                            timeTable.loc[(d,l),p] = [
                                className,subject[0],teacherName,('%s-%s'%(s,e))]
                        else:
                            continue
                        return True
    return False
                
def generateTimeTable(className,duration):
    'class whose timetable is to be generated'
    
    import pandas as pd
    import semester
    import teacher
    timeTable = readTimeTable()
    courseTable = semester.readClass(className)

    subjects = list()

    for i in courseTable.index:
        tempSubject = courseTable.loc[i,'Subjects']
        creditMin = courseTable.loc[i,'CM']
        if(tempSubject.endswith(theDefaultLabChars())):
            subjects.append([tempSubject,creditMin])
            continue
        while(creditMin != 0):
            if(creditMin == duration):
                subjects.append([tempSubject,duration])
                creditMin -= duration
            elif(creditMin > duration):
                if((creditMin-duration) >= duration):
                    subjects.append([tempSubject,duration])
                    creditMin -= duration
                else:
                    subjects.append([tempSubject,creditMin])
                    creditMin -= creditMin
            else:
                subjects.append([tempSubject, creditMin])
                creditMin -= creditMin
                
    import timing
    timeList = readTimeHeaders()
    uniEndTime = timing.toMin(timeList[-1].split('-')[1])
    import random
    random.shuffle(subjects)
    import room
    
    for r in list(room.readAllRooms().Name):
        for p in timeTable.columns:
                for d in timing.daysOfWeek():
                    if((len(subjects)!=0)):
                        temp = subjects[-1]
                        teacherName = teacher.findTeacherOfSubject(temp[0])
                        if(temp[0].endswith(theDefaultLabChars())):
                            if(allotLab(timeTable,className,temp,duration)):
                                temp = subjects.pop()
                            else:
                                print('Not enough labs...')
                                return
                            continue
                        if((timeTable.loc[(d,r),p] == theDefaultEmptyChar())):
                            # Clash Resolves
                            import duplicates
                            if((duplicates.doesClassClashExist(timeTable, d, p, className)) or
                               (duplicates.doesTeacherClashExist(timeTable, d,p, teacherName))):
                                    continue
                            #---------------
                            
                            s = timeList[int(p[-1])].split('-')[0]
                            e = timing.toMin(s) + temp[1]
                            if(e > uniEndTime):
                                continue
                            e = timing.toHour(e)
                            
                            if(temp[1] <= duration):
                                timeTable.loc[(d,r),p] = [
                                    className,temp[0],teacherName,('%s-%s'%(s,e))]
                            else:
                                if(putDollarsForNextPeriods(
                                    timeTable,className,temp[0],d,r,p,s,e)):
                                    timeTable.loc[(d,r),p] = [
                                        className,temp[0],teacherName,('%s-%s'%(s,e))]
                                else:
                                    continue
                            temp = subjects.pop()
                                 
                                
    if(len(subjects)!=0):
        print('Not enough rooms...')
    timeTable.to_csv('timetables/TimeTable.csv')




