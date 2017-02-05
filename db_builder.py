# Reo Kimura, Asher Lasday
#SoftDev2 pd8
#HW1 -- And Papayas
#2017-02-06

from pymongo import MongoClient
import csv


server = MongoClient('lisa.stuy.edu')
ourDB = server.automatic_funicular

students = open('peeps.csv')
studentData = csv.DictReader(students)
courses = open('courses.csv')
courseData = csv.DictReader(courses)

studentData.next()
for peep in studentData:
    entry = {}
    entry['name'] = peep['name']
    entry['id'] = peep['id']
    entry['age'] = peep['age']
    
    courseData.next()
    for course in courseData:
        if (entry['id'] == course['id']):
                entry[course['code']] = course['mark']
    courses.seek(0)
            
    ourDB.collection1.insert_one(entry)
    
students.close()
courses.close()
    

    
    
