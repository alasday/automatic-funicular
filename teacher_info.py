# Reo Kimura, Asher Lasday
# SoftDev2 pd8
# HW3 -- Untitled
# 2017-02-08

from pymongo import MongoClient
import csv

#server = MongoClient('lisa.stuy.edu')
#ourDB = server['automatic_funicular']

fd = open('teachers.csv')
d = csv.DictReader(fd)

for teacher in d:
    print 'hello'
