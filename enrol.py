#-*- encoding: utf-8 -*-
import os, os.path 


def readlines(filename):
	lines = []
	f = open(filename, 'r')
	for line in f.readlines():
		if line[0] == '#':
			continue
		else:
			lines.append(line.strip())
	f.close()
	return lines
# print readlines("SUBJECTS")

def readtable(filename):
	tables = []
	lines = readlines(filename)
	for line in lines:
		items = line.split(':')
		line = []
		for item in items:
			line.append(item)
		tables.append(line)
	return tables
# print readtable("SUBJECTS")

def writelines(filename, lines):
	f = open('temp', 'w')
	try:
		for line in lines:
			f.write(line + '\n')
		f.close()
	except:
		f.close()
		os.remove("temp")
		return 0
	os.remove(filename)
	os.rename("temp", filename)
	return 1
# lines = readlines("SUBJECTS")
# print writelines("new", lines)


class Enrol:
	def __init__(self, dirName):
		os.chdir(dirName)
		self.subjectsTable = readtable("SUBJECTS")
		self.classesTable = readtable("CLASSES")
		self.venuesTable = readtable("VENUES")

	def subjects(self):
		subjectsCode = [subject[0] for subject in self.subjectsTable]
		return subjectsCode

	def subjectName(self, subjectCode):
		subjectsDict = dict()
		for subject in self.subjectsTable:
			subCode = subject[0]
			subName = subject[1]
			subjectsDict[subCode] = subName
		try:
			return subjectsDict.get(subjectCode)
		except:
			return None

	def classes(self, subjectCode):
		classesDict = dict()
		for aClass in self.classesTable:
			classId = aClass[0]
			subCode = aClass[1]
			try:
				classesDict[subCode].append(classId)  
			except:
				classesDict[subCode] = [classId]
		try:
			return classesDict[subjectCode]
		except:
			raise KeyError

	def classesInfo(self, classId):
		classesDict = dict()
		for aClass in self.classesTable:
			aClassId = aClass[0]
			subCode = aClass[1]
			time = aClass[2]
			room = aClass[3]
			tutor = aClass[4]
			studentsId = []
			try:
				filename = aClassId + ".roll"
				studentsId = readlines(filename)
			except:
				pass
			classInfo = (subCode, time, room, tutor, studentsId)
			try:
				classesDict[aClassId].append(classInfo)
			except:
				classesDict[aClassId] = classInfo
		try:
			return classesDict[classId]
		except:
			raise KeyError

	def checkStudent(self, studentId, subjectCode=None):
		if subjectCode:
			classes = self.classes(subjectCode)
			for aClass in classes:
				classInfo = self.classesInfo(aClass)
				if studentId in classInfo[4]:
					return aClass
			return None
		else:
			classesId = []
			for subject in self.subjects():
				try:
					classes = self.classes(subject)
					for aClass in classes:
						classInfo = self.classesInfo(aClass)
						if studentId in classInfo[4]:
							classesId.append(aClass)
				except:
					pass
			return classesId

	def enrol(self, studentId, classId):
		# subjectCode = self.classesInfo(classId)[0] # "bw101"
		classInfo = self.classesInfo(classId)
		if studentId in classInfo[4]:
			return 1
		else:
			roomCapacity = self.capacity(classInfo[2])
			curNum = len(classInfo[4])
			if curNum >= roomCapacity: # no space
				return None
			checkClassId = self.checkStudent(studentId, classInfo[0])
			if checkClassId:
				filename = checkClassId + ".roll"
				studentsId = readlines(filename)
				studentsId.remove(studentId)
				writelines(filename, studentsId)
			filename = classId + ".roll"
			studentsId = readlines(filename)
			studentsId.append(studentId)
			writelines(filename, studentsId)
			return 1

	def capacity(self, room):
		for venue in self.venuesTable:
			if venue[0] == room:
				return int(venue[1])
		return None



		

		
# e = Enrol('/Users/yhf/Dropbox/code/slp')	
# print e.subjects()
# print e.subjectName("bw110")
# print e.classes("bw101")
# print e.classesInfo("bw101.1") # ('bw101', 'Mon 9.30', '2.5.10', 'Alice Chiswick', ['1124395', '1125622', '1109202', '1136607'])
# print e.checkStudent("1124395")
# print e.enrol("1124", "bw101.3")
# print e.enrol("1124", "bw101.1")
# print e.enrol("11242", "bw101.1")
# print e.capacity("2.5.10")
