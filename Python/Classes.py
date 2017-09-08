"""class school():
	address="Begampet"
	school_name="Saraswathi"	

	def get_name(self):
		return (self.name)

	def get_school_addr(self):
		return (self.address)

	@classmethod 
	def change_school_name(cls, name, addrs):
		cls.school_name=name
		cls.address=addrs
	
	
class student(school):
	def __init__(self, name, Class):
		self.name=name
		self.Class=Class
		
	def get_school_name(self):
		return (self.school_name)

	@staticmethod	
	def say_JanaGanaMana():
		return("Jana Gana Mana")
	
	@classmethod #Alternate contructors
	def from_str(cls, stu_str):
		cls.name, cls.Class=stu_str.split("-")
		return student(cls.name, cls.Class)
		
		
stu_str="Rama-X"

student1=student.from_str(stu_str)

print(student1.get_name())
print(student1.get_school_addr())


exit()
"""
class school():
	address="Begampet"
	school_name="Saraswathi"	

	def get_name(self):
		return (self.name)

	def get_school_addr(self):
		return (self.address)

	@classmethod 
	def change_school_name(cls, name, addrs):
		cls.school_name=name
		cls.address=addrs
		
class student(school):
	def __init__(self, name, Class):
		self.name=name
		self.Class=Class
		
	def get_school_name(self):
		return (self.school_name)

	@staticmethod	
	def say_JanaGanaMana():
		return("Jana Gana Mana")

student1=student("Rama", "X")
#print(student1.say_JanaGanaMana())
print(student1.get_school_name())
print(student1.get_school_addr())
#print(student.__dict__)

#school.change_school_name("Vagedevi","Panjagutta")
#school1=school()
#print(school1.address, school1.school_name )

#Below show effect only student class only but not on  school!
student1.change_school_name("Vagedevi","Panjagutta")
#student.change_school_name("Vagedevi","Panjagutta")

print(student.__dict__)
print("---------------------------------------------")
print("---------------------------------------------")
print(student1.__dict__)
#print(student1.get_school_name())
#print(student1.get_school_addr())

print("School: ",school.address, school.school_name )

exit()
class A_class:
	n=1010

class B_class(A_class):
	m=2020

class C_class(B_class):
	l=3030

class D_class(A_class):
	k=4040
	m=5050
#class myclass(A_class, B_class):
#class myclass(C_class, D_class):
class myclass(D_class, C_class):
	i=5050
	def __init__(self, i):
		self.i=i

	def print_i(self):
		print(self.i)
#overriding
a=myclass(100) #instance creation

print(a.__dict__)
print(a.i)
print(a.k)
print(a.l)
print(a.m)
print(a.n)


exit()
class your_class:
	j=3030
print(your_class.__bases__)
exit()
class your_class:
	j=3030

class other_class:
	k=3030
	
class myclass(your_class, other_class):
	i=2020
	def __init__(self, i):
		self.i=i

	def print_i(self):
		print(self.i)
myclass.__new__
a=myclass(100) #instance creation

b=myclass(200) != myclass.__init__(200)

#print(myclass.__bases__)
print(a.__dict__)
#print(myclass.__dict__)
#print(your_class.j)

exit()
class your_class:
	j=3030

class other_class:
	k=3030
	
class myclass(your_class, other_class):
	j=2020
	def __init__(self, i):
		self.i=i
		
	def print_i(self):
		print(self.i)
 		
a=myclass(100) #instance creation
b=myclass(200)

print(a.__dict__)
print(a.z)
a.j=123123123
print(a.__dict__)
print(a.j)
print(your_class.j)
print(id(a.j))
print(id(your_class.j))
#print(myclass.j)

exit()
class myclass:
	i=2020
	def __init__(self, i):
		self.i=i
		
	def print_i(self):
		print(self.i)

a=myclass(100) #instance creation
b=myclass(200)
c=myclass(300)
a.print_i()
myclass.print_i(c)

exit()
print(a.i)
print(b.i)
print(myclass.i)
#print(id(myclass.i))
#print(id(a.i))
print(a.__dict__)
print(b.__dict__)
print()
print(myclass.__dict__)

exit()

a=myclass()
print(a.__dict__)
a.i=1
print(a.__dict__)
a.j="Sri Rama"
print(a.__dict__)
#print(myclass.__dict__)

exit()
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
#Classes are to associate data with its operations
"""
abc=123
print(abc)
#print(id(abc))
def myfun():
	#print(abc)
	global abc
	abc=999
	bbc=100
	print("myfun: ",abc)
	#print(id(abc))
	def myfun2():
		print("myfun2: ",abc)
	myfun2()
	
myfun()
print(abc)
print(bbc)

"""
"""
def fun_a(qwe):
	a=23
	def fun_b():
		b=34
		def fun_c():
			c=45
			a=10101
			print(a,b,c)
		fun_c()
		print(a,b)		
	fun_b()
fun_a(dfgdf)

abc=123

def myfun():
	print(abc)
	
myfuc()

"""
###############################################

"""
class myclass:
	pass

a=myclass()
a.i=1
a.j="Sri Rama"
print(a.i, a.j)
"""
###############################################
#"""
class myclass:
	pass

a=myclass()
print(a.__dict__)
a.i=1
print(a.__dict__)
a.j="Sri Rama"
print(a.__dict__)
#print(myclass.__dict__)

#"""
###############################################
"""
class myclass:
	pass

a=myclass()
a.i=1
a.j="Sri Rama"
print(a.__class__)
print(type(a))
"""
###############################################
"""
class myclass:
	pass

a=myclass()
a.i=1
a.j="Sri Rama"
print(a.__name__)
#print(myclass.__name__)

"""
###############################################
"""
class yourclass:
	pass
class otherclass:
	pass
class myclass(yourclass, otherclass):
	pass

a=myclass()
a.i=1
a.j="Sri Rama"
print(myclass.__bases__)

"""
###############################################
"""
class yourclass:
	a=1010101
class otherclass:
	x=-23
class myclass(yourclass, otherclass):
	i=1
	j="Sri Rama"

a=myclass()
print(a.__dict__)
print(myclass.__dict__)
a.k=20202
print(a.__dict__)
print(myclass.__dict__)
"""
###############################################
"""
class yourclass:
	a=1010101
class otherclass:
	x=-23
class myclass(yourclass, otherclass):
	i=1
	j="Sri Rama"

a=myclass()
print(a.__dict__)
print(a.x,a.a)
print(a.__dict__)
a.a=3030303
print(a.x,a.a)
print(a.__dict__)
print(yourclass.a)
"""
###############################################
"""
class myclass():
	i=1
	j="Sri Rama"
	def __init__(self,k,l):
		self.K=k
		self.L=l

a=myclass(1,2)
print(a.__dict__)
print()
print(myclass.__dict__)
print(list(myclass.__dict__.items()))
"""
###############################################
"""
class myclass():
	i=1
	j="Sri Rama"

	def __init__(mine,i, k,l):
		mine.i=i
		mine.K=k
		mine.L=l
		print(dir())
		#print(globals())
		#print(locals())
	

a=myclass(0,1,2)
#print(a.__dict__)
print()
#print(myclass.__dict__)
"""
###############################################
"""
class myclass():
	i=1
	j="Sri Rama"

	def __init__(mine,k,l):
		mine.K=k
		mine.L=l

a=myclass(0,1)
b=myclass(10,11)
print(a.__dict__)
print(b.__dict__)
print(a.i,b.i,myclass.i)
print(id(a.i),id(b.i),id(myclass.i))
myclass.i=33
print(a.i,b.i,myclass.i)
print(id(a.i),id(b.i),id(myclass.i))
a.i=22
print(a.i,b.i,myclass.i)
print(id(a.i),id(b.i),id(myclass.i))
"""
###############################################
