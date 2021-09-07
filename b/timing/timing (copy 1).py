
def daysOfWeek():
    days = ['Mon','Tue','Wed','Thu','Fri']
    return days

def toMin(hour):
    return (int(hour[0:2])*60 + int(hour[2:4]))

def toHour(minutes):
    return ('%02d%02d'%(minutes//60, minutes%60))

def makePeriods():
    start = '0800'#input('Uni Start Time: ')
    end = '1800'#input('Uni End Time: ')
    duration = '0130'#input('Duration of a period: ')
    shortBreak = '0015'#input('Enter length of short break: ')

    p = ((toMin(end)+toMin(shortBreak) - toMin(start))/(toMin(duration)+toMin(shortBreak)) )
    #print('p: ',p) # for debugging 
    import math
    #print('trunc: ',math.trunc(p)) # for debugging
    periods = math.trunc(p)

    temp = int(toMin(start))
    timeList=[]
    i = 0
    while (i<periods):
        other = temp + int(toMin(duration))
        #print(toHour(temp),toHour(other))  #for debugging purposes 
        timeList.append('%s-%s'%(toHour(temp),toHour(other)))
        temp = other + int(toMin(shortBreak))
        i += 1
    f = open('timeHeader.txt','w')
    f.write(str(timeList))
    f.close()
    return timeList












