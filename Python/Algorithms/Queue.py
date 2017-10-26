#SriMatreNamah\
class Node():
	def __init__(self, item):
		self.data=item
		self.Next=None
	
class Queue(Node):
	def __init__(self):
		self.Start=None
		self.End=None
		self.Qlength=0
	
	def EnQ(self, item):
		if(None == self.Start):
			self.Start=Node(item)
			self.End=self.Start
		else:
			self.End.Next=Node(item)
			self.End=self.End.Next
		self.Qlength+=1
	
	def DeQ(self):
		if(None == self.Start):
			return None
		else:
			data=self.Start.data
			temp=self.Start
			self.Start=self.Start.Next
			del(temp)
		self.Qlength-=1
		return data

	def DelQ(self):
		while(self.DeQ() != None):
			pass
	def LenQ(self):
		return(self.Qlength)

myQ=Queue()
myQ.EnQ(10)
print(">> ",myQ.LenQ())
myQ.EnQ(11)
print(">> ",myQ.LenQ())
myQ.EnQ(12)
print(">> ",myQ.LenQ())
print(myQ.DeQ())
print(">> ",myQ.LenQ())
print(myQ.DeQ())
print(">> ",myQ.LenQ())
myQ.EnQ(14)
print(">> ",myQ.LenQ())
myQ.EnQ(16)
print(">> ",myQ.LenQ())
myQ.EnQ(17)
print(">> ",myQ.LenQ())
#myQ.DelQ()
print(">> ",myQ.LenQ())
print(myQ.DeQ())
print(">> ",myQ.LenQ())
print(myQ.DeQ())
print(">> ",myQ.LenQ())
print(myQ.DeQ())
print(">> ",myQ.LenQ())
print(myQ.DeQ())
print(">> ",myQ.LenQ())
print(myQ.DeQ())
print(">> ",myQ.LenQ())
