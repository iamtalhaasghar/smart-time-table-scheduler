def duplicatesInDay(timeTable):
    'Returns list of all lectures of a day irrespective of class and room'
    import Timing
    import TimeTable
    for d in Timing.daysOfWeek():
        dayData = timeTable.loc[d]
        periodList = list()
        for room in dayData.index:
            for period in dayData.columns:
                if(dayData[period][room] == TimeTable.theDefaultEmptyChar()):
                    continue
                data = extractPeriodDetail(timeTable, d,room,period)
                if(periodList.count(data) >= 1):
                    print('Duplicate : %s'%(data))
                    if(not removeDuplicateSubjectsOfDay(timeTable,d,room,period)):
                        continue
                    duplicatesInDay(timeTable)
                    import Filer
                    timeTable.to_html('%s/Duplicate%s.html'%(Filer.TIME_TABLE_FOLDER,
                                                  Filer.TIME_TABLE_FILE_NAME))
                    return
                else:
                    periodList.append(data)
    import Filer
    timeTable.to_csv('%s/%s.csv'%(Filer.TIME_TABLE_FOLDER,
                                  Filer.TIME_TABLE_FILE_NAME))
    '''
    timeTable.to_excel('%s/%s.xlsx'%(Filer.TIME_TABLE_FOLDER,
                                  Filer.TIME_TABLE_FILE_NAME))
    '''
    return

def calculateDuration(timeTable, day,room, period):
    import Timing
    temp = eval(timeTable.loc[(day,room),period])
    time = temp[3].split('-')
    duration = (Timing.toMin(time[1]) - Timing.toMin(time[0]))
    return duration


def trySwap(timeTable,day,room,period,nextDay):
    import TimeTable
    oldDayData = timeTable.loc[day]
    nextDayData = timeTable.loc[nextDay]
    oldDayPeriodList = list()
    nextDayPeriodList = list()
    for r in oldDayData.index:
        for p in oldDayData.columns:
            if(oldDayData[p][r] != TimeTable.theDefaultEmptyChar()):
                oldDayPeriodList.append(extractPeriodDetail(timeTable,day,r,p))            
    for r in nextDayData.index:
        for p in nextDayData.columns:
            if(nextDayData[p][r] != TimeTable.theDefaultEmptyChar()):
                nextDayPeriodList.append(extractPeriodDetail(timeTable,nextDay,r,p))

    clashingPeriod = extractPeriodDetail(timeTable,day,room,period)
    if(nextDayPeriodList.count(clashingPeriod) == 0):
        print('%s Fits in %s'%(clashingPeriod,nextDay))
        for temp in nextDayPeriodList:

            clashingPeriodData = eval(clashingPeriod)
            clashingPeriodClassName = clashingPeriodData[0]
            clashingPeriodTeacherName = clashingPeriodData[2]

            nextDayPeriodData = eval(temp)
            nextDayPeriodClassName = nextDayPeriodData[0]
            nextDayPeriodTeacherName = nextDayPeriodData[2]
            
            if((nextDayPeriodData[3] == clashingPeriodData[3]) and
               (nextDayPeriodClassName == clashingPeriodClassName) and
               oldDayPeriodList.count(temp) == 0
            ):
                print('%s Fits in %s'%(temp,day))
                location = findTimeVenueOfPeriodOn(timeTable,nextDay,temp)
                if(len(location)!= 0):
                    import TimeTable
                    timeTable_copy = timeTable.copy(deep = True)
                    timeTable_copy.loc[(day,room),period] = TimeTable.theDefaultEmptyChar()
                    timeTable_copy.loc[(nextDay,location[0]),location[1]] = TimeTable.theDefaultEmptyChar()

                    print('location = ',location)
                    input('...')
                    if(doesTeacherClashExist(timeTable_copy,day,period,nextDayPeriodTeacherName)):
                        print('Teacher clash for %s in %s %s '%(nextDayPeriodTeacherName,day,period))
                        continue
                    if(doesClassClashExist(timeTable_copy,day,period, nextDayPeriodClassName)):
                        print('Class clash for %s in %s %s '%(nextDayPeriodClassName,day,period))
                        continue
                    if(doesTeacherClashExist(timeTable_copy,nextDay,location[1],clashingPeriodTeacherName)):
                        print('Teacher clash for %s in %s %s '%(clashingPeriodTeacherName,nextDay,location[1]))
                        continue
                    if(doesClassClashExist(timeTable_copy,nextDay,location[1],clashingPeriodClassName)):
                        print('Class clash for %s in %s %s'%(clashingPeriodClassName,nextDay, location[1]))
                        continue
                    input('Doing swapping...')
                    clashingPeriodData = eval(timeTable.loc[(day,room),period])
                    nextDayPeriodData = eval(
                        timeTable.loc[(nextDay,location[0]),location[1]])

                    small1 = clashingPeriodData[:3].copy()
                    small2 = nextDayPeriodData[:3].copy()
                    small2.extend(clashingPeriodData[3:].copy())
                    small1.extend(nextDayPeriodData[3:].copy())
                    timeTable.loc[(day,room),period] = str(small2)
                    timeTable.loc[(nextDay,location[0]),location[1]] = str(small1)
                    print('Swapped %s with %s' %(small1, small2))
                    import Filer
                    timeTable.to_html('%s/Duplicate%s.html'%(Filer.TIME_TABLE_FOLDER,
                                                  Filer.TIME_TABLE_FILE_NAME))
                    return True
                else:
                    print('Unable to find next Day period which is impossible...')
    return False

def findTimeVenueOfPeriodOn(timeTable,day,periodDetails):
    import Timing
    import Room
    index = []
    for r in Room.readAllRooms().Name:
        for p in timeTable.columns:
                if(extractPeriodDetail(timeTable,day,r,p) == periodDetails):
                    index = [r,p]      
    return index
    
def removeDuplicateSubjectsOfDay(timeTable,day,room,period):

    import Timing
    for d in Timing.daysOfWeek():
        print('*'*50)
        if (d == day):
            continue
        if(trySwap(timeTable, day,room,period, d)):
            return True
        input('Wait...')
    print('Can`t remove clash of %s %s %s'%(day,room,period))
    return False
   
def extractPeriodDetail(timeTable,day,room,period):
    import TimeTable
    if(timeTable.loc[(day,room),period] == TimeTable.theDefaultEmptyChar()):
        return TimeTable.theDefaultEmptyChar()
    import Timing
    temp = eval(timeTable.loc[(day,room),period])
    temp[3] = calculateDuration(timeTable, day,room, period)
    data = str(temp)
    return data

def doesClassClashExist(timeTable, day, period, className):
    lectureList = list(timeTable.loc[day,period])
    classesList = list()
    import TimeTable
    for k in lectureList:
        if(k != TimeTable.theDefaultEmptyChar()):
            if(type(k) == list):
                classesList.append(k[0])
            elif(type(k) == str):
                t = eval(k)
                classesList.append(t[0])
    if(className in classesList):
        return True
    else:
        return False
    
def doesTeacherClashExist(timeTable, day, period, teacherName):
    lectureList = list(timeTable.loc[day,period])
    teacherList = list()
    import TimeTable
    for k in lectureList:
        if(k != TimeTable.theDefaultEmptyChar()):
            if(type(k) == list):
                teacherList.append(k[2])
            elif(type(k) == str):
                t = eval(k)
                teacherList.append(t[2])
    if(teacherName in teacherList):
        return True
    else:
        return False
