class student:
	school_addrs="Begampet"
		
	def __init__(self, Name="asd", ClaSS=0, last_yearMarks=0):
		self.name=Name
		self.Class=ClaSS
		self.total_marks=last_yearMarks
		self.email=self.name+"."+self.Class+"@school.com"
		self.addr=""

	def update_addr(self, addr):
		self.addr=addr

	def getname(self):
		return (self.name)
	
var=student("Rama","VII",67)
print(student.school_addrs)
print(var.school_addrs)
print(var.name)
print(var.email)
var.addr="Sbad"
print(var.addr)
var.update_addr("Hyd")
print(var.addr)

print("--------")
exit()

class student:
	name="NoName"
	Class=""
	total_marks=0
	def __init__(self, Name="asd", ClaSS=0, last_yearMarks=0):
		self.name=Name
		self.Class=ClaSS
		self.total_marks=last_yearMarks

	def getname(self):
		return (self.name)
		
		
var=student("Rama","VII",67)
print(var.name)
print(id(var.name))
print(id(student.name))

print("--------")
exit()
class student:
	name="NoName"
	Class=""
	total_marks=0
	def __init__(self, Name="asd", ClaSS=0, last_yearMarks=0):
		self.name=Name
		self.Class=ClaSS
		self.total_marks=last_yearMarks

	def getname(self):
		return (self.name)
		
		
var=student("Rama","VII",67)
var2=student()

print(var.name)
print(var.Class)
print(var.total_marks)
print("--------")
exit()
var.name=123
var.Class="VII"
var.total_marks=67
print(var.name)
print(var.Class)
print(var.total_marks)


exit()
class student:
	name="NoName"
	Class=""
	total_marks=0
	
	def getname(self):
		return (self.name)
var=student()
print(var.name)
var.name="Rama"
var.Class="VII"
var.total_marks=67
print(var.name)
print(var.Class)
print(var.total_marks)



exit()

"""
class myclass:
	mynumber=0
	
	def getmynumber(self):
		return (self.mynumber)
"""
class student:
	name="NoName"
	def __init__(self, name="NoName"):
		self.name=name
	def getname(self):
		return (self.name)


		
		
var=student()
print("var.name: "+var.name)
print("student.name: "+student.name)

exit()

class student:
	name="NoName"
	Class=""
	total_marks=0
	
	def getname(self):
		return (self.name)

var=student()
print(var.name)
print(student.name)
var.name=1212
student.name="SriRama"
print(var.name)
print(student.name)
var2=student()
print(var2.name)
print(var.getname())



"""
class student:
	name=""
	def getname(self):
		print(self.name)

var=student()
var.name="Srirama"
print(id(var.getname()))
var2=student()
var2.name="SriSitarama"
print(id(var2.getname()))
"""
