# Reo Kimura, Asher Lasday
# SoftDev2 pd8
# HW2 -- You Boys Like Mexico?
# 2017-02-07

from pymongo import MongoClient
import csv 

server = MongoClient('lisa.stuy.edu')
ourDB = server['automatic_funicular']

def computeAverage(studentDict):
	courseList = studentDict['courses'] 
	total = 0.0
	tally = 0.0 
	for course in courseList:
		total += course['mark']
		tally += 1
	avg = total / tally
	return avg

def displayAverages():
	averages = []
	cursor = ourDB.students.find()
	for student in cursor:
		entry = {}
		name = student['name']
		ID = student['id']
		avg = computeAverage(student)
		print("%s (id %s) has an average of %f")%(name, ID, avg)
		averages.append({'name' : name, 'id' : ID, 'avg' : avg})
	return averages

displayAverages()