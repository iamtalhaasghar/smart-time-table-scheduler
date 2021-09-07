def duplicatesInDay(timeTable,day):
    'Returns list of all lectures of a day irrespective of class and room'
    dayData = timeTable.loc[day]
    periodList = list()
    for period in dayData:
        for room in dayData[period]:
            if(periodList.count(dayData[period][room]) >= 1):
                return [room,period]
            else:
                periodList.append(dayData[period][room])            
    return None

def checkSameSubjects(timeTable):
    import TimeTable
    for d in timeTable.index:
        temp = list(timeTable.loc[d])
        for t in temp:
            if( t!= TimeTable.theDefaultEmptyChar() and temp.count(t)>1):
                print('Duplicates : %s'%(t))
                timeTable.to_html('Duplicate.html')
                input('Removing the duplicate...')
                removeDuplicateSubjects(timeTable, d)
                checkSameSubjects(timeTable)
                return
    return
def removeDuplicateSubjects(timeTable, errorIndex):

    import TimeTable

    errorSubjects = list((timeTable.loc[errorIndex]))
    elementIndex = 0
    for i in range(len(errorSubjects)):
        if( errorSubjects[i]!= TimeTable.theDefaultEmptyChar() and
            errorSubjects.count(errorSubjects[i])>1):
                elementIndex = i
                break

    className = eval(errorSubjects[elementIndex])[0]
    
    day = errorIndex[0]
    room = errorIndex[1]
    
    for d in timeTable.index:
        if (d[0] == day):
            continue
        rows = list(timeTable.loc[(d[0],room)])
        for j in range(len(rows)):
            print('Check row: ',rows)
            if((eval(rows[j])[0] == className) and
               (rows.count(errorSubjects[elementIndex]) == 0)):
                   if(rows[j] != TimeTable.theDefaultEmptyChar() and
                       errorSubjects.count(rows[j]) == 0):
                        temp = rows[j]
                        rows[j] = errorSubjects[elementIndex]
                        errorSubjects[elementIndex] = temp
                        timeTable.loc[errorIndex] = errorSubjects
                        timeTable.loc[(d[0],room)] = rows
                        timeTable.to_csv('TimeTable.csv')
                        timeTable.to_html('TimeTable.html')
                        return
