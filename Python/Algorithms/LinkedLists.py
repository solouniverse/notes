class Node(object):

	NodeCount=0
	def __init__(self, data=None, Link=None):
		self.data = data
		self.Link = Link
		Node.NodeCount+=1

	def getNthNode(self, N):
		TempNode=self
		for x in range(N):
			TempNode=TempNode.Link
		return (TempNode)

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

	def PrintMiddleNode(self):
		if(None != self):
			TempNode=self
			TempNode2=self

			try:
				while(TempNode2.Link.Link !=None):
					if(TempNode2.Link !=None):
						TempNode2=TempNode2.Link.Link
					else:
						break
					TempNode=TempNode.Link
					
			except:
				pass
			
			print("Value of middle node is: ",TempNode.data)
			
		else:
			print("Cannot find middle item from a 'None' list")

	def PrintMiddleNode_2(self):
		if(None != self):
			TempNode=self
			TempNode2=self
			count=0
			while(TempNode2.Link !=None):
				TempNode2=TempNode2.Link
				count+=1
				if(count%2==0):
					TempNode=TempNode.Link
			
			print("Value of middle node is: ",TempNode.data)
			
		else:
			print("Cannot find middle item from a 'None' list")

	def PrintByNthNode(self, N):
		if(None != self):
			TempNode=self
			TempNode2=self
			count=0
			while(TempNode2.Link !=None):
				TempNode2=TempNode2.Link
				count+=1
				if(count%N==0):
					TempNode=TempNode.Link
			
			print("Value of middle node is: ",TempNode.data)
			
		else:
			print("Cannot find middle item from a 'None' list")

	def PrintMiddle3rd(self, N):
	# Using a 2nd counter to find the length of 1/3rd elements.
		TempNode=self
		TempNode2=self
		TempNodeNext=None
		
		if(None != self):
			count=0
			count2=0
			while(TempNode2.Link !=None):
				TempNode2=TempNode2.Link
				count+=1
				if(count%N==0):
					count2+=1
					TempNode=TempNode.Link

			while(count2):
				print(TempNode.data)
				TempNode=TempNode.Link
				count2-=1

		else:
			print("Cannot find middle item from a 'None' list")

	def PrintMiddle3rd_2(self, N):
	#Using count itself
		TempNode=self
		TempNode2=self
		
		if(None != self):
			count=0
			while(TempNode2.Link !=None):
				TempNode2=TempNode2.Link
				count+=1
				if(count%N==0):
					TempNode=TempNode.Link

			while(count>0):
				print(TempNode.data)
				TempNode=TempNode.Link
				count-=N #It should be reduced by 'N' but not '1'

		else:
			print("Cannot find middle item from a 'None' list")

	def PrintMiddle3rd_3(self, N):
	#Using 1/3rd Pointer and 2/3rd pointers
		TempNode=self
		TempNode2=self
		TempNode3=self
		
		if(None != self):
			count=0
			while(TempNode2.Link !=None):
				TempNode2=TempNode2.Link
				count+=1
				if(count%N==0):
					TempNode=TempNode.Link
					TempNode3=TempNode3.Link.Link 
					
			while(TempNode != TempNode3):
				print(TempNode.data)
				TempNode=TempNode.Link

		else:
			print("Cannot find middle item from a 'None' list")

	def SplitByNthNode(self, N):
		TempNode=self
		TempNode2=self
		TempNodeNext=None
		
		if(None != self):
			count=0
			while(TempNode2.Link !=None):
				TempNode2=TempNode2.Link
				count+=1
				if(count%N==0):
					TempNode=TempNode.Link

			TempNodeNext=TempNode.Link
			TempNode.Link=None
		else:
			print("Cannot find middle item from a 'None' list")
		return (TempNodeNext)

	def SplitIntoNlists(self, N):
	#Using a 2nd counter(count2) to find the length of 1/nth elements.

		TempNode=self
		TempNode2=self
		TempNodeNext=None
		headList=[]
		if(None != self):
			count=0
			count2=0
			headList.append(self)
			while(TempNode2.Link !=None):
				TempNode2=TempNode2.Link
				count+=1
				if(count%N==0):
					count2+=1
					TempNode=TempNode.Link
			
			TempNodeNext=TempNode.Link
			TempNode.Link=None
			headList.append(TempNodeNext)
			TempNode=TempNodeNext
	# Using count2 we are splitting the list into N-1
	#as we already created first list above
			for y in range(N-1):			
				for x in range(count2):
					if(TempNode == None):
						break
					TempNode=TempNode.Link
					
				if(TempNode != None):
					TempNodeNext=TempNode.Link
					TempNode.Link=None
					if(TempNodeNext != None):
						headList.append(TempNodeNext)
					TempNode=TempNodeNext
				else:
					break
				
		else:
			print("Cannot find middle item from a 'None' list")
		return(headList)

	def GetNthNode(self, N):
		TempNode=self
		if N == -1: # for Last node
			while(TempNode.Link != None):
				TempNode=TempNode.Link
			return TempNode
			
		N-=1
		while(N and TempNode != None):
			TempNode=TempNode.Link
			N-=1
		if N!=0:
			return None
		return TempNode

	def GetPreviousNode(self, CurrentNode):
		TempNode=self
		while(TempNode.Link != CurrentNode and TempNode.Link != None):
			TempNode=TempNode.Link

		if TempNode.Link == CurrentNode:
			return TempNode
		return None

	def isListLooped(self):
		#Start two pointers at 1X & 2X speeds and see it they meet any where
		TempNode=self
		TempNode2=self	
		
		while(TempNode2.Link != None and TempNode2 != None):
			if(TempNode2.Link.Link == None):
				break
			TempNode2 = TempNode2.Link.Link
			TempNode = TempNode.Link
			if(TempNode == TempNode2):
				return (True)
				
		return(False)
			
	def CreateLoopAtIndex(self, N):
		Tempnode=GetNthNode(self, -1) # get last Node
		Tempnode2=GetNthNode(head, N) # get Nth Node
		if(Tempnode != None and Tempnode2 != None): #if both of them are valid
			Tempnode.Link=Tempnode2 # Point last to Nth node
			return (True)
		return (False)

	def GetLoopingNode(self):
		if(self != None):
			TempNode=self
			while(TempNode.Link != None):
				TempNode2=self
				while(TempNode2 != TempNode):
					if(TempNode2 == TempNode.Link):
						return (TempNode2)
					TempNode2 = TempNode2.Link
					
				TempNode = TempNode.Link
		return (None)

	def FixLoopingNode(self):
		if(self != None):
			TempNode=self
			while(TempNode.Link != None):
				TempNode2=self
				while(TempNode2 != TempNode):
					if(TempNode2 == TempNode.Link):
						TempNode.Link=None
						return (TempNode2)
					TempNode2 = TempNode2.Link
					
				TempNode = TempNode.Link
		return (None)

	def GetNthNodeFromLast(self, N):
		if(N < 0 or self == None):
			return (None)

		TempNode=self
		TempNode2=self
		count=0
		while(TempNode!=None):
			TempNode=TempNode.Link
			count+=1
			
			if(count > N): #Start this traverse delayed by N iterations
				TempNode2=TempNode2.Link

		if(count < N): #If Total length of List is < N
			return None
			
		return(TempNode2)

	def IsListIntersectingWith(self, self2):
	# Last Node of 2 intersected lists will be same
		TempNode=self
		TempNode2=self2
		while(TempNode.Link != None):
			TempNode = TempNode.Link

		while(TempNode2.Link != None):
			TempNode2 = TempNode2.Link
		
		return (TempNode2 == TempNode)
		
	def FindIntersectionWith(self, self2):
		TempNode=self
		while(TempNode != None):
			TempNode2=self2
			while(TempNode2 != None):
				if(TempNode == TempNode2):
					return TempNode2
				TempNode2=TempNode2.Link
			TempNode=TempNode.Link
			
		return None

	def FixIntersectionWith(self, self2):
		TempNode=self
		while(TempNode != None):
			TempNode2=self2
			while(TempNode2 != None):
				if(TempNode.Link == TempNode2):
					TempNode.Link=None
					return True
				TempNode2=TempNode2.Link
			TempNode=TempNode.Link

		return False
		
	@staticmethod
	def DeleteNodeWithoutHeader(NodeToBedeleted):
		#Copy contents of next node to given node and del next node
		NextNode=NodeToBedeleted.Link
		NodeToBedeleted.data = NextNode.data
		NodeToBedeleted.Link = NextNode.Link
		del(NextNode)

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




head=Node.PrepareList([x for x in range(6,3,-1)])
head.ListLinkedList()
print("---------------------------\n")

"""
Intersection of 2 Lists
head2=Node.PrepareList([x for x in range(36,32,-1)])
head2.ListLinkedList()
print("---------------------------\n")
#Intersect Two Lists
TempNode=GetNthNode(head, -1)
TempNode2=GetNthNode(head2, 2)
TempNode.Link=TempNode2

head.ListLinkedList()
print("---------------------------\n")
head2.ListLinkedList()
print("---------------------------\n")
print(FindIntersectionWith(head2, head).data)
print(FindIntersectionWith(head, head2).data)
"""

#print(isListLooped(head))
#if(CreateLoopAtIndex(head, 14)):
#	print(isListLooped(head))
#print(GetLoopingNode(head).data)

#Tempnode=GetPreviousNode(head, Tempnode)
#print(Tempnode.data)

exit()

#SplitIntoN_2(head,4)
print("---------------------------\n")
exit()
#PrintMiddleNode(head)
#PrintMiddleNode_2(head)
#PrintByNthNode(head, 3)
#head2=head.SplitByNthNode( 2)
#head2.ListLinkedList()
#heads=head.SplitIntoNlists(8)
SplitIntoN_2(head,4,1)
#head.ListLinkedList()

exit()
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
