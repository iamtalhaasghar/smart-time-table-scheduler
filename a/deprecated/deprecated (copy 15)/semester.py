def makeClass(duration):
    'Requires Duration of a period'
    className = input('Class Name: ')
    creditHours = list()
    subjects = list()
    lectures = list()
    contactMins = list()
    oneCreditHour = 1

    s = input('Enter Subject (q = quit) : ')
    import math
    import timing
    while (s!='q'):
        c = int(input('Enter Credit Hours : '))
        totalContactMins = (c * oneCreditHour) * 60
        l = math.trunc(totalContactMins / (duration))    #Warning: may be erroneous in some cases
        if(l*duration != totalContactMins):
            print('l = %d C.H = %d duration = %d'%(l,totalContactMins,duration))
            y = totalContactMins - (l*duration)
            print('Total Contact Mins: %d'%totalContactMins)
            print('No of allocated Mins: %d'%(l*duration))
            print('Loss of %d mins for %s'%(y,s))
            lectures.append(0)
        else:
            lectures.append(l)
        subjects.append(s)
        creditHours.append(c)
        contactMins.append(totalContactMins)
        
        s = input('Enter Subject (q = quit) : ')
    data = {'Subjects':subjects, 'CH':creditHours,'CM':contactMins, 'Lectures':lectures}
    import pandas as pd
    courses = pd.DataFrame(data, index = [i for i in range(1, len(subjects)+1)])
    courses = courses.rename_axis('Serial')
    courses.to_csv('classes/%s.csv'%(className))
    
def readClass(className):
    'ClassName whose data is to be read'
    import pandas as pd
    data = pd.read_csv('classes/%s.csv'%(className))
    data = data.set_index('Serial')
    return data

