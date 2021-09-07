# Ver Details: Dollar problem solved
import room
import semester
import TimeTable
import timing
'''
room.addRooms()
semester.makeClass(timing.toMin('0130'))
semester.makeClass(timing.toMin('0130'))
semester.makeClass(timing.toMin('0130'))
semester.makeClass(timing.toMin('0130'))
'''
TimeTable.createTimeTable()
TimeTable.generateTimeTable('CS1B',timing.toMin('0130'))
TimeTable.generateTimeTable('CS2B',timing.toMin('0130'))
TimeTable.generateTimeTable('CS3B',timing.toMin('0130'))
TimeTable.generateTimeTable('CS4B',timing.toMin('0130'))
table = TimeTable.readTimeTable()
table.to_html('TimeTable.html')
import duplicates
duplicates.duplicatesInDay(table)
table.to_html('TimeTable.html')
