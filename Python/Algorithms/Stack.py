#SriMatreNamah\
class Node():
	def __init__(self, item):
		self.data=item
		self.Next=None
	
class Stack(Node):
	def __init__(self):
		self.Top=None
		self.StackHeight=0

	def Push(self, item):
		if(None == self.Top):
			self.Top=Node(item)
		else:
			temp=Node(item)
			temp.Next=self.Top
			self.Top=temp

		self.StackHeight+=1
	
	def Pop(self):
		if(None == self.Top):
			return None
		else:
			data=self.Top.data
			self.Top=self.Top.Next
		self.StackHeight-=1
		return data
	

myQ=Stack()
myQ.Push(10)
myQ.Push(11)
myQ.Push(12)
print(myQ.Pop())
print(myQ.Pop())
myQ.Push(21)
myQ.Push(22)
print(myQ.Pop())
print(myQ.Pop())
print(myQ.Pop())
print(myQ.Pop())
