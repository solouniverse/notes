class TreeNode():
	def __init__(self, data):
		self.data=data
		self.Left=None
		self.Right=None

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
	
def PrintTree(root):
	temp=root
	myQ=Queue()
	while(1):
		if(temp == None):
			break
		print(temp.data)
		myQ.EnQ(temp.Left)
		myQ.EnQ(temp.Right)
		if(myQ.LenQ == 0):
			break
		temp=myQ.DeQ()
	
	myQ.DelQ()

def AddNode(root, item):
	temp2=TreeNode(item)
	temp=root
	myQ=Queue()
	while(1):
		if(temp.Left == None):
			temp.Left =temp2
			break
		elif(temp.Right == None):
			temp.Right = temp2
			break
		myQ.EnQ(temp.Left)
		myQ.EnQ(temp.Right)
		if(myQ.LenQ == 0):
			break
		temp=myQ.DeQ()
	myQ.DelQ()

def InOrder(root):
	if(root != None):
		InOrder(root.Left)
		print(root.data)
		InOrder(root.Right)

def PreOrder(root):
	if(root != None):
		print(root.data)
		PreOrder(root.Left)
		PreOrder(root.Right)

def PostOrder(root):
	if(root != None):
		PostOrder(root.Left)
		PostOrder(root.Right)
		print(root.data)

root=TreeNode(0)
for x in range(1,10):
	AddNode(root, x)


PrintTree(root)
print("InOrder------------------------------------>>")
InOrder(root)
print("PreOrder------------------------------------>>")
PreOrder(root)
print("PostOrder------------------------------------>>")
PostOrder(root)
