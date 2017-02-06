# Reo Kimura, Asher Lasday
#SoftDev2 pd8
#HW2 -- You Boys Like Mexico?
#2017-02-07

from pymongo import MongoClient
import csv

server = MongoClient('lisa.stuy.edu')
ourDB = server.automatic_funicular
cursor = ourDB.students.find()
print cursor

averages = {} #dictionary of students' averages

# for student in ourDB.students.find():
#     print student