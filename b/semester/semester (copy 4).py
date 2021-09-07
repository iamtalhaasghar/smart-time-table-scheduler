def makeClass(duration):
    'Requires Duration of a period'
    className = input('Class Name: ')
    creditHours = list()
    subjects = list()
    contactMins = list()
    oneCreditHour = 1

    s = input('Enter Subject (q = quit) : ')
    import math
    import timing
    import TimeTable
    while (s!='q'):
        c = int(input('Enter Credit Hours : '))
        if(s.endswith(TimeTable.theDefualtLabChars())):
            oneCreditHour = 3
            import lab
            lab.selectLab(s)
        else:
            oneCreditHour = 1
        totalContactMins = (c * oneCreditHour) * 60
        subjects.append(s)
        creditHours.append(c)
        contactMins.append(totalContactMins)
        s = input('Enter Subject (q = quit) : ')
        
    data = {'Subjects':subjects, 'CH':creditHours,'CM':contactMins}
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

