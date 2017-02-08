# Reo Kimura, Asher Lasday
# SoftDev2 pd8
# HW3 -- Untitled
# 2017-02-08

from pymongo import MongoClient
import csv

server = MongoClient('lisa.stuy.edu')
ourDB = server['automatic_funicular']

fd = open('teachers.csv')
d = csv.DictReader(fd)

def addStudents(code):
    studentList = []
    cursor = ourDB.students.find()
    for student in cursor:
        courseList = student['courses']
        for course in courseList:
            if course["code"]  == code:
                studentList.append(student['id'])
    return studentList

def genTeacherColl():
    for teacher in d:
        entry = {} # one teacher doc
        entry['teacher'] = teacher['teacher']
        entry['period'] = teacher['period']
        entry['code'] = teacher['code']
        entry['students'] = addStudents(entry['code'])
        ourDB.teachers.insert_one(entry)

genTeacherColl()
    
