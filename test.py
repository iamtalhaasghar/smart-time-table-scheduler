import os
import sys
sys.path.append(os.getcwd()+'/codefiles')
sys.path.append(os.getcwd()+'/guifiles')
import pandas as pd
pd.set_option('display.max_colwidth',0)
'''
import TimeTable
p = TimeTable.readTimeTable()
s, e = TimeTable.splitTimeTable(p)
o = TimeTable.joinTimeTables(s,e)
'''
import teacher
print(teacher.searchTeachersWithNameLike('Dr'))
