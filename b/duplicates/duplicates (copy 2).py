def duplicatesInDay(timeTable):
    'Returns list of all lectures of a day irrespective of class and room'
    import timing
    import TimeTable
    for d in timing.daysOfWeek():
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
                    timeTable.to_html('timetables/Duplicate.html')
                    return
                else:
                    periodList.append(data)
    timeTable.to_csv('timetables/TimeTable.csv')
    return

def calculateDuration(timeTable, day,room, period):
    import timing
    temp = eval(timeTable.loc[(day,room),period])
    time = temp[3].split('-')
    duration = (timing.toMin(time[1]) - timing.toMin(time[0]))
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
    
    if(nextDayPeriodList.count(extractPeriodDetail(timeTable,day,room,period)) == 0):
        for temp in nextDayPeriodList:
            
            if((eval(temp)[3] == calculateDuration(timeTable, day,room,period)) and
               (eval(temp)[0] == eval(oldDayData[period][room])[0]) and
               oldDayPeriodList.count(temp) == 0):
                for r in nextDayData.index:
                    for p in nextDayData.columns:
                        if(extractPeriodDetail(timeTable,nextDay,r,p) == temp):
                            input('Doing swapping...')
                            data1 = eval(timeTable.loc[(day,room),period])
                            data2 = eval(timeTable.loc[(nextDay,r),p])
                            small1 = data1[:3].copy()
                            small2 = data2[:3].copy()
                            small2.extend(data1[3:].copy())
                            small1.extend(data2[3:].copy())
                            timeTable.loc[(day,room),period] = str(small2)
                            timeTable.loc[(nextDay,r),p] = str(small1)
                            print('Swapped %s with %s' %(small1, small2))
                            timeTable.to_html('timetables/Duplicate.html')
                            return True
    return False

def removeDuplicateSubjectsOfDay(timeTable,day,room,period):

    import timing
    for d in timing.daysOfWeek():
        if (d == day):
            continue
        if(trySwap(timeTable, day,room,period, d)):
            return True
    return False
   
def extractPeriodDetail(timeTable,day,room,period):
    import TimeTable
    if(timeTable.loc[(day,room),period] == TimeTable.theDefaultEmptyChar()):
        return TimeTable.theDefaultEmptyChar()
    import timing
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
