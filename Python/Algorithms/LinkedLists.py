class Node(object):

	NodeCount=0
	def __init__(self, data=None, Link=None):
		self.data = data
		self.Link = Link
		Node.NodeCount+=1

	def ListLinkedList(self):
		TempNode=self
		while(TempNode != None):
			#for x in range(9):	
			print("{} @ {}, {}".format(TempNode.data, id(TempNode), id(TempNode.Link)))
			#print(TempNode.data)
			TempNode=TempNode.Link

	def ListLinkedListReversed(self):
		if(self.Link != None):
			self.Link.ListLinkedListReversed()
		print(self.data)

	def ListLinkedListRecursive(self):
		print(self.data)
		if(self.Link != None):
			self.Link.ListLinkedListRecursive()

	def CountLinkedList(self):
		count=0
		TempNode=self
		while(TempNode != None):
			TempNode=TempNode.Link
			count+=1
		return count

	def InsertNodeIndex(self, Index, Value):
		if(self != None):
			current=self
			for x in range(Index-2):
				current=current.Link

			TempNodePrev = Node(Value)
			TempNodePrev.Link=current.Link
			current.Link=TempNodePrev

	def InsertNodeIndexReverse(self, Index, Value):
		if(self != None):
			current=self
			for x in range(Node.NodeCount-Index):
				current=current.Link

			TempNodePrev = Node(Value)
			TempNodePrev.Link=current.Link
			current.Link=TempNodePrev

	def RemoveNode(self, value=None):
		if(None != self):
			TempNode=self
			if(value != None):
				while((TempNode.data != value) and (TempNode != None )):
					TempNodePrev=TempNode
					TempNode=TempNode.Link
			else:
				while(TempNode.Link != None ):
					TempNodePrev=TempNode
					TempNode=TempNode.Link
					
			if ((value !=None and TempNode != None) or (value==None and TempNode.Link == None ) ):
				print("%d Deleted" %TempNode.data)
				TempNodePrev.Link=TempNode.Link
				del(TempNode)
				Node.NodeCount-=1
			else:
				print("Given value not found in link!")
		else:
			print("Cannot delete items from None list")

	def SortList(self):
		if(None != self):
			count=0
			for x in range(self.NodeCount):
				TempNode=self
				itemsChanged=0
				while(TempNode.Link !=None):
					if(TempNode.data > TempNode.Link.data):
						TempNode.data, TempNode.Link.data=TempNode.Link.data,TempNode.data
						itemsChanged=1
					TempNode=TempNode.Link
					count+=1
				if(itemsChanged==0):
					break
			print("Loop repeated %d times" %count)
		else:
			print("Cannot sort items from None list")

	def SortListFirstHalf(self):
		if(None != self):
			count=0
			for x in range(self.NodeCount):
				TempNode=self
				TempNode2=self
				itemsChanged=0
				try:
					while(TempNode2.Link.Link !=None):
						if(TempNode.data > TempNode.Link.data):
							TempNode.data, TempNode.Link.data=TempNode.Link.data,TempNode.data
							itemsChanged=1
							
						TempNode=TempNode.Link
						if(TempNode2.Link.Link !=None):
							TempNode2=TempNode2.Link.Link
						else:
							break

						count+=1
					if(itemsChanged==0):
						break
				except:
					pass
			print("Loop repeated %d times" %count)
		else:
			print("Cannot sort items from None list")

	def SortListSecondHalf(self):
		if(None != self):
			count=0
			for x in range(self.NodeCount):
				TempNode=self
				TempNode2=self
				itemsChanged=0
				try:
					while(TempNode2.Link.Link !=None):						
						TempNode=TempNode.Link
						count+=1
						if(TempNode2.Link.Link !=None):
							TempNode2=TempNode2.Link.Link
						else:
							break
				except:
					pass
					
				while(TempNode.Link != None):
					if(TempNode.data > TempNode.Link.data):
						TempNode.data, TempNode.Link.data=TempNode.Link.data,TempNode.data
						itemsChanged=1
					TempNode=TempNode.Link
												
					count+=1
				if(itemsChanged==0):
					break

			print("Loop repeated %d times" %count)
		else:
			print("Cannot sort items from None list")

	def SortListSecondHalf_2(self):
		if(None != self):
			count=0
			for x in range(self.NodeCount):
				TempNode=self
				itemsChanged=0
				for y in range(self.NodeCount//2):
					TempNode=TempNode.Link
					count+=1
					
				while(TempNode.Link != None):
					if(TempNode.data > TempNode.Link.data):
						TempNode.data, TempNode.Link.data=TempNode.Link.data,TempNode.data
						itemsChanged=1
					TempNode=TempNode.Link
												
					count+=1
				if(itemsChanged==0):
					break

			print("Loop repeated %d times" %count)
		else:
			print("Cannot sort items from None list")

	def SortListSecondHalf_3(self):
		if(None != self):
			count=0
			TempNode1=self
			for y in range(self.NodeCount//2):
				TempNode1=TempNode1.Link

			for x in range(self.NodeCount//2):
				TempNode=TempNode1
				itemsChanged=0
					
				while(TempNode.Link != None):
					if(TempNode.data > TempNode.Link.data):
						TempNode.data, TempNode.Link.data=TempNode.Link.data,TempNode.data
						itemsChanged=1
					TempNode=TempNode.Link
												
					count+=1
				if(itemsChanged==0):
					break

			print("Loop repeated %d times" %count)
		else:
			print("Cannot sort items from None list")

	def ListReverse(self, Prev):
		if(self.Link != None):
			head=self.Link.ListReverse(self)# All remaining nodes accepts and passes the head new head
			self.Link=Prev
			return(head)
		else:
			self.Link=Prev
			return (self) #The last node declares it self as head!

	def ReverseNonRecursive(self):
		NewHead=None
		for x in range(self.NodeCount):
			TempNode=self
			while(TempNode.Link != None):
				TempNodePrev=TempNode
				TempNode = TempNode.Link
			
			TempNodePrev.Link=None
			
			if(NewHead == None):
				NewHead=TempNode
				TempNode2 = NewHead
			else:
	#			TempNode2 = NewHead # As this line is added in above if it skips this while loop
	#			while(TempNode2.Link != None):
	#				TempNode2 = TempNode2.Link
				TempNode2.Link=TempNode
				TempNode2=TempNode2.Link

		return(NewHead)

	def ReverseNonRecursive_2(self):
		currentNode=self
		nextNode,prevNode = None,None
		while(currentNode != None):
			nextNode = currentNode.Link
			currentNode.Link = prevNode
			prevNode = currentNode
			currentNode = nextNode

		return(prevNode)

	@classmethod
	def PrepareList(cls, InputList):
		cls.head=None
		for x in InputList:
			if(cls.head == None):
				cls.head=Node(x)
				TempNodePrev=cls.head
			else:
				TempNodePrev.Link=Node(x)
				TempNodePrev=TempNodePrev.Link
		
		return cls.head
	
"""
head.ListLinkedList()
print(head.NodeCount)


print("---------------------------\n Inserting node\n")
head.InsertNodeIndex(6,-5555)
head.ListLinkedList()
print(head.NodeCount)
exit()

print("---------------------------\n")
head.InsertNodeIndexReverse(6,-5555)
head.ListLinkedList()
print(head.NodeCount)
exit()
"""

"""			
			TempNode=head
			while(TempNode.Link !=None):
				TempNodePrev=TempNode
				TempNode=TempNode.Link
				if(TempNode.data < TempNodePrev.data):
					TempNode.data, TempNodePrev.data=TempNodePrev.data,TempNode.data

"""					


head=Node.PrepareList([x for x in range(6,-1,-1)])
head.ListLinkedList()
print("---------------------------\n")
head.SortListSecondHalf_3()
#head=head.ReverseNonRecursive()
#head=head.ReverseNonRecursive_2()
head.ListLinkedList()
print("---------------------------\n")
exit()
head.ListLinkedListReversed()
print("---------------------------\n")
head.ListLinkedListRecursive()
exit()
#head.SortListHalf()
head.SortListSecondHalf_2()
head.ListLinkedList()

head.RemoveNode(15)
head.RemoveNode()
print("---------------------------\n")
head.InsertNodeIndex(3, -234)
head.InsertNodeIndex(6, 0)
head.InsertNodeIndexReverse( 1, -167)
head.InsertNodeIndexReverse(1, -189)
head.ListLinkedList()
print("---------------------------\n")
Node.SortListHalf(head)
Node.ListLinkedList(head)
print(head.NodeCount)
