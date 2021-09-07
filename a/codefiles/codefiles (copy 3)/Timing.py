def daysOfWeek():
    
    import Filer
    data = Filer.readGeneralSettingsFile('WorkingDays')    
    daysList = eval(data)
    #print(type(daysList))
    if(len(daysList) != 0):
        return daysList
    else:
        print('No working day.File was read but no working day was present.')
        input('TODO: Exception...')

        
def toMin(time):
    
    t = time.split(':')
    return int(t[0])*60 + int(t[1])

def toHour(minutes):
    return ('%02d:%02d'%(minutes//60, minutes%60))


def makePeriods():
    import Filer
    start = Filer.readGeneralSettingsFile('StartTime')
    end = Filer.readGeneralSettingsFile('EndTime')
    duration = int(Filer.readGeneralSettingsFile('PeriodDuration'))
    shortBreak = int(Filer.readGeneralSettingsFile('BreakDuration'))

    temp = toMin(start)
    timeList=[]
    e = toMin(end)
    while (temp < e):

        if(temp + duration <= e):
            other = temp + duration
        else:
            temp -= shortBreak
            other = e            
        #print(toHour(temp),toHour(other))
        timeList.append('%s-%s'%(toHour(temp),toHour(other)))
        temp = other + shortBreak

    f = open('%s/%s'% (Filer.DATA_FOLDER, Filer.TIME_HEADER_FILE_NAME), 'w')
    f.write(str(timeList))
    f.close()
    return timeList
