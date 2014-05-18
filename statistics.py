#!/usr/bin/python
import enrol
# class Enrol:
# 	__init__(self, dirName)
# 	subjects(self)
# 	subjectName(self, subjectCode)
# 	classes(self, subjectCode)
# 	classesInfo(self, classId)
# 	checkStudent(self, studentId, subjectCode=None)
# 	enrol(self, studentId, classId)
# 	capacity(self, room)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--student', nargs=1, help='student ID')
# parser.set_defaults(func=sayhello)
args = parser.parse_args()
# args.func(args)

def noArg():
	e = enrol.Enrol("/Users/yhf/Dropbox/code/slp")
	subjects = e.subjects()
	for subject in subjects:
		classesNum = len(e.classes(subject))
		studentsNum = 0
		for aClass in e.classes(subject):
			studentsNum += len(e.classesInfo(aClass)[4])
		print "%10s %-30s classes: %-2d  students: %-4d" % (subject, e.subjectName(subject), classesNum, studentsNum)

def hasArg(studentId):
	e = enrol.Enrol("/Users/yhf/Dropbox/code/slp")
	classesId = e.checkStudent(studentId)
	for classId in classesId:
		classInfo = e.classesInfo(classId)
		subjectCode = classInfo[0]
		subjectName = e.subjectName(subjectCode)
		time = classInfo[1]
		room = classInfo[2]
		print "%s (%s), %s, in %s" % (subjectCode, subjectName, time, room)

import sys
try:
	studentId = sys.argv[2]
	hasArg(studentId)
except:
	noArg()








