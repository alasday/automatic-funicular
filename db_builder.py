# Reo Kimura, Asher Lasday
#SoftDev2 pd8
#HW1 -- And Papayas
#2017-02-06

from pymongo import MongoClient
import csv

server = MongoClient('lisa.stuy.edu')
ourDB = server['automatic_funicular']

students = open('peeps.csv')
studentDict = csv.DictReader(students)
courses = open('courses.csv')
courseDict = csv.DictReader(courses)

for peep in studentDict:
    entry = {}
    entry['name'] = peep['name']
    entry['id'] = peep['id']
    entry['age'] = int(peep['age'])
    entry['courses'] = []
    for course in courseDict:
        if (entry['id'] == course['id']):
            entry['courses'].append({'code': course['code'], 'mark': int(course['mark'])})
    courses.seek(0)
    ourDB.students.insert_one(entry)
    
students.close()
courses.close()
    

    
    
