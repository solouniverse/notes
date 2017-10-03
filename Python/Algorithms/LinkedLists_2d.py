class Node_2d:
	def __init__(self, data, Hlink=None, Vlink=None):
		self.data=data
		self.Hlink=Hlink
		self.Vlink=Vlink

Array=[[1,2,3], [4,5,6,7], [8,9,0]]
#print(Array)
def Create2dList(Array):
	self=None
	for x in Array:
		TempVHeadNode = None
		for y in x:
			if(TempVHeadNode == None):
				TempVHeadNode=Node_2d(y)
				TempVList=TempVHeadNode
			else:
				TempVList.Vlink=Node_2d(y)
				TempVList=TempVList.Vlink
		if(self == None):
			self=TempVHeadNode
			TempHList=self
		else:	
			TempHList.Hlink=TempVHeadNode
			TempHList=TempHList.Hlink
	
	return (self)
			
def DisplayList(self):
	TempHNode=self
	while(TempHNode != None):
		TempVNode=TempHNode
		while(TempVNode != None):
			print(TempVNode.data, end=" >")
			TempVNode=TempVNode.Vlink
		print("\nv")
		TempHNode=TempHNode.Hlink

def Flatten2dList(self): 
	#Remove H Links and use Vlinks only
	TempHNode=self
	while(TempHNode != None):
		TempVNode=TempHNode
		while(TempVNode.Vlink != None):
			TempVNode=TempVNode.Vlink
		TempVNode.Vlink=TempHNode.Hlink
		TempHNode.Hlink=None
		TempHNode=TempVNode.Vlink
	
def Flatten2dList_2(self):
	#Unfinished
	TempHNode=self
	while(TempHNode != None):
		TempVNode=TempHNode
		while(TempVNode != None):
			print(TempVNode.data, end=" >")
			#if(TempVNode.Hlink != None):	
			TempVNode.Vlink.Hlink=TempVNode.Hlink
			TempVNode.Hlink=TempVNode.Vlink
			TempVNode.Vlink=None
			TempVNode=TempVNode.Hlink
		print("\nv\n\n")
		TempHNode=TempHNode.Hlink
	
	

head=Create2dList(Array)
#DisplayList(head)
Flatten2dList(head)
DisplayList(head)
