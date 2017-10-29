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

def PrintTree(root):
	temp=root
	myQ=Queue()
	while(1):
		if(temp == None):
			break
		print(temp.data)
		if temp.Left != None:
			myQ.EnQ(temp.Left)
		if temp.Right != None:
			myQ.EnQ(temp.Right)

		temp=myQ.DeQ()
	
	myQ.DelQ()

def InOrder(root):
	if(root != None):
		InOrder(root.Left)
		print(root.data, end=" ")
		InOrder(root.Right)

def InOrderNonRecursive(root):
	if(root == None):
		return
	myStack=Stack()
	while(1):
		while(root != None):
			myStack.Push(root)
			root = root.Left
			
		if(myStack.StackHeight == 0):
			break
		
		root=myStack.Pop()
		print(root.data, end=" ")
		root = root.Right

	print()
	
def PreOrderNonRecursive(root):
	if(root == None):
		return
	myStack=Stack()
	while(1):
		while(root != None):
			print(root.data, end=" ")
			myStack.Push(root)
			root = root.Left
			
		if(myStack.StackHeight == 0):
			break
		
		root=myStack.Pop()
		root = root.Right

	print()

def PreOrder(root):
	if(root != None):
		print(root.data, end=" ")
		PreOrder(root.Left)
		PreOrder(root.Right)

def PostOrder(root):
	if(root != None):
		PostOrder(root.Left)
		PostOrder(root.Right)
		print(root.data, end=" ")

def PrintThroughLevels(root):
	if(root == None):
		return None
	myQ=Queue()
	while(1):
		print(root.data, end=" ")
		if(root.Left != None):
			myQ.EnQ(root.Left)
		if(root.Right != None):
			myQ.EnQ(root.Right)
		root=myQ.DeQ()
		if(not myQ.Qlength):
			break
	print()

def PrintLevelWise(root):
	myQ=Queue()
	myQ.EnQ(root)
	myQ.EnQ(None)	
	while(1):
		temp=myQ.DeQ()
		if(temp != None):
			print(temp.data, end=" ")
			if(temp.Left != None):
				myQ.EnQ(temp.Left)
			if(temp.Right != None):
				myQ.EnQ(temp.Right)
		else:
			print()
			if(myQ.Qlength == 0):
				break
			myQ.EnQ(None)
	myQ.DelQ()

def PrintLevelWiseMirrorTree(root):
	myQ=Queue()
	myQ.EnQ(root)
	myQ.EnQ(None)	
	while(1):
		temp=myQ.DeQ()
		if(temp != None):
			print(temp.data, end=" ")
			if(temp.Right != None):
				myQ.EnQ(temp.Right)
			if(temp.Left != None):
				myQ.EnQ(temp.Left)
		else:
			print()
			if(myQ.Qlength == 0):
				break
			myQ.EnQ(None)
	myQ.DelQ()

def PrintLevelWiseFullNodes(root):
	myQ=Queue()
	myQ.EnQ(root)
	myQ.EnQ(None)	
	while(1):
		temp=myQ.DeQ()
		if(temp != None):
			if(temp.Left != None and temp.Right != None):
				print(temp.data, end=" ")
			if(temp.Left != None):
				myQ.EnQ(temp.Left)
			if(temp.Right != None):
				myQ.EnQ(temp.Right)
		else:
			print()
			if(myQ.Qlength == 0):
				break
			myQ.EnQ(None)
	myQ.DelQ()
	
def PrintSumByLevel(root):
	if(root == None):
		return None
	myQ=Queue()
	myQ.EnQ(root)
	myQ.EnQ(None)
	mysum=0
	while(1):
		root=myQ.DeQ()
		if(not myQ.Qlength):
			break
		if(root == None):
			print(" = ",mysum)
			mysum=0
			myQ.EnQ(None)			
			continue			

		print(root.data, end=" ")
		mysum+=root.data
		if(root.Left != None):
			myQ.EnQ(root.Left)
		if(root.Right != None):
			myQ.EnQ(root.Right)

	print(" = ",mysum)

def PrintTreeSumNonRecursive(root):
	if(root == None):
		return None
	myQ=Queue()
	myQ.EnQ(root)
	myQ.EnQ(None)
	mysum=0
	while(1):
		root=myQ.DeQ()
		if(not myQ.Qlength):
			break
		if(root == None):
			myQ.EnQ(None)			
			continue			

		mysum+=root.data
		if(root.Left != None):
			myQ.EnQ(root.Left)
		if(root.Right != None):
			myQ.EnQ(root.Right)

	print("Tree Total = ",mysum)

def PrintTreeSum(root):
	if(root != None):
		return(PrintTreeSum(root.Left) + root.data + PrintTreeSum(root.Right))
	return 0

def SeachTreeNonRecursive(root,item):
	if(root == None):
		return
	myStack=Stack()
	count=0
	while(1):
		while(root != None):
			count+=1
			if(root.data == item):
				print("Iterated %d times" %count)
				return True
			myStack.Push(root)
			root = root.Left
			
		if(myStack.StackHeight == 0):
			break
		
		root=myStack.Pop()

		root = root.Right
	print("Iterated %d times" %count)
	return False

def SearchTree(root, item):
	if(root != None):
		if(root.data == item):
			#print("Found ", root.data)
			return True
#Skip further searching if one of the decendants are matched		
		if(SearchTree(root.Left, item)):
			return True

		if(SearchTree(root.Right, item)):
			return True

def SearchTree2(root, item):
#This logic doesnt work effectively(Skips right childs) so dont use it***
	if(root != None):
		if(root.data == item):
			#print("Found ", root.data)
			return True
#Skip further searching **always**		
		return(SearchTree2(root.Left, item))
#This line never gets executed as above line always returns first
		return(SearchTree2(root.Right, item))
			
def FindTreeSizeNonRecursive(root):
	if(root == None):
		return 0
	myQ=Queue()
	myQ.EnQ(root)
	myQ.EnQ(None)
	size=0
	while(1):
		temp=myQ.DeQ()
		if(temp != None):
			size+=1
			if(temp.Left != None):
				myQ.EnQ(temp.Left)
			if(temp.Right != None):
				myQ.EnQ(temp.Right)
		else:
			if(myQ.Qlength == 0):
				break
			myQ.EnQ(None)
	myQ.DelQ()
	return size

def FindTreeSize(root):
	if(root == None):
		return 0
	return(1+FindTreeSize(root.Left)+FindTreeSize(root.Right))

def FindTreeFullNodesCount(root):
	if(root == None):
		return 0
		
	if(root.Left != None and root.Right != None):
		mysize=1
	else:
		mysize=0

	return(mysize+FindTreeFullNodesCount(root.Left)+FindTreeFullNodesCount(root.Right))
	
def FindTreeHalfNodesCount(root):
	if(root == None):
		return 0

	mysize=0
		
	if(root.Left != None or root.Right != None):
		mysize=1
	if(root.Left != None and root.Right != None):
		mysize=0
		
	return(mysize+FindTreeHalfNodesCount(root.Left)+FindTreeHalfNodesCount(root.Right))

def FindTreeHeightNonRecursive(root):
	myQ=Queue()
	myQ.EnQ(root)
	myQ.EnQ(None)
	TreeHeight=0
	while(1):
		temp=myQ.DeQ()
		if(temp!=None):
			if(temp.Left != None):
				myQ.EnQ(temp.Left)
			if(temp.Right != None):
				myQ.EnQ(temp.Right)
		else:
			TreeHeight+=1
			if(myQ.Qlength == 0):
				break
			myQ.EnQ(None)
			
	return(TreeHeight)
			
def FindTreeHeight(root):
	if(root != None):
		lHeight=FindTreeHeight(root.Left)
		rHeight=FindTreeHeight(root.Right)
		if(lHeight > rHeight):
			return lHeight+1
		else:
			return rHeight+1
	else:
		return 0

def FindTreeWidthNonRecursive(root):
	myQ=Queue()
	myQ.EnQ(root)
	myQ.EnQ(None)
	tempCount=0
	MaxWidth=0
	while(1):
		temp=myQ.DeQ()
		if(temp != None):
			if(temp.Left != None):
				myQ.EnQ(temp.Left)
			if(temp.Right != None):
				myQ.EnQ(temp.Right)
			tempCount+=1
		else:
			if(tempCount > MaxWidth):
				MaxWidth=tempCount
			tempCount=0
			if(myQ.Qlength == 0):
				break
			myQ.EnQ(None)

	return(MaxWidth)

def FindDeepestNodeNonRecursive(root):
	if(root == None):
		return
	myQ=Queue()
	myQ.EnQ(root)
	myQ.EnQ(None)	
	while(1):
		temp=myQ.DeQ()
		if(temp != None):
			Prev=temp
			if(temp.Left != None):
				myQ.EnQ(temp.Left)
			if(temp.Right != None):
				myQ.EnQ(temp.Right)
		else:
			if(myQ.Qlength == 0):
				break
			myQ.EnQ(None)
			
	print("Deepest node: ",Prev.data)
	myQ.DelQ()

def FindDeepestNode(root, depth):
	deepestNode=root

	if(root!=None):
		if(root.Left != None):
			[tempDeepestNode, tempDepth]=FindDeepestNode(root.Left,  depth+1)
			if(tempDepth > depth):
				deepestNode=root
				depth=tempDepth

		if(root.Right != None):
			[tempDeepestNode, tempDepth]=FindDeepestNode(root.Right,  depth+1)
			if(tempDepth > depth):
				deepestNode=tempDeepestNode
				depth=tempDepth

	return (deepestNode, depth)

def FindDeepestNodeV2(root, depth):
	if(root!=None):
		if(root.Left != None):
			[lTempDeepestNode, lTempDepth]=FindDeepestNode(root.Left,  depth+1)

		if(root.Right != None):
			[rTempDeepestNode, rTempDepth]=FindDeepestNode(root.Right,  depth+1)
			
		if (root.Left == None and root.Right == None):
			return [root, depth]
		
		print(root.data, depth)
			
		if(lTempDepth >= rTempDepth):
			return [lTempDeepestNode, lTempDepth]
		else:
			return [rTempDeepestNode, rTempDepth]
	else:
		return [None, 0]
	
def FindTreeMax(root, TreeMax):
	if(root != None):
		if(root.data > TreeMax):
			TreeMax=root.data
		temp=FindTreeMax(root.Left, TreeMax)
		if(temp > TreeMax):
			TreeMax=temp
		temp=FindTreeMax(root.Right, TreeMax)
		if(temp > TreeMax):
			TreeMax=temp
	return(TreeMax)

def DeleteTree(root):
	if(root != None):
		DeleteTree(root.Left)
		DeleteTree(root.Right)
		del(root)

def DeleteLeafNodes(root):
	if(root != None):
		if(root.Left !=None):
			if(root.Left.Left == None and root.Left.Right == None):
				del(root.Left)
				root.Left=None
		if(root.Right !=None):			
			if(root.Right.Left == None and root.Right.Right == None):
				del(root.Right)
				root.Right=None
		DeleteLeafNodes(root.Left)
		DeleteLeafNodes(root.Right)

def CompareTrees(root1, root2):
	if (root1==None and root2==None):
		return True
	if (root1==None or root2==None):
		return False
	if (root1.data != root2.data):
		return False
	
	return(CompareTrees(root1.Left, root2.Left) and CompareTrees(root1.Right, root2.Right))

def CompareMirrorTrees(root1, root2):
	if (root1==None and root2==None):
		return True
	if (root1==None or root2==None):
		return False
	if (root1.data != root2.data):
		return False
	
	return(CompareMirrorTrees(root1.Left, root2.Right) and CompareMirrorTrees(root1.Right, root2.Left))

def MirrorTree(root):
	if(root != None):
		root.Left,root.Right=root.Right,root.Left
		MirrorTree(root.Left)
		MirrorTree(root.Right)

def PrintPaths(root, path):
	if(root != None):
		path.append(root.data)
#path is updated in left travesal as path is considered as a global 
# variable so we are sending a unmodified copy to right section 
		path1=path.copy()
		print(root.data," : ",*path)
		PrintPaths(root.Left, path)
		PrintPaths(root.Right, path1)


root=TreeNode(0)
for x in range(1,100):
	AddNode(root, x)

root2=TreeNode(0)
for x in range(1,36):
	AddNode(root2, x)

#PrintTree(root)
PrintLevelWise(root)
print(FindTreeFullNodesCount(root))
print(FindTreeHalfNodesCount(root))
#print(FindTreeSizeNonRecursive(root))
#print(FindTreeSize(root))
#DeleteLeafNodes(root)
#PrintLevelWise(root)
#PrintPaths(root, [])
#MirrorTree(root2)
#PrintLevelWise(root2)
#print(CompareMirrorTrees(root, root2))
#print(CompareTrees(root, root2))
#PrintLevelWiseFullNodes(root)
#PrintLevelWiseMirrorTree(root)
#print(FindTreeMax(root, root.data))
#FindDeepestNodeNonRecursive(root)
#print(FindDeepestNode(root, 0)[0].data)
#print(FindDeepestNodeV2(root, 0)[0].data)
#for x in range(1,15):
#	print(x, SearchTree(root, x))
#PrintSumByLevel(root)
#PrintTreeSumNonRecursive(root)
#print(PrintTreeSum(root))
#print(SeachTreeNonRecursive(root, 0,0))
#print("TreeWidth: ",FindTreeWidth(root))
#print("FindTreeHeightNonRecursive: ",FindTreeHeightNonRecursive(root))
#print("FindTreeHeight: ",FindTreeHeight(root))
#for x in range(1,15):
#	print(x,SearchTree(root, x))
#print("\nInOrderNonRecursive------------------------------------>>")
#InOrderNonRecursive(root)
#print("\nInOrder------------------------------------>>")
#InOrder(root)
#print("\nPreOrderNonRecursive------------------------------------>>")
#PreOrderNonRecursive(root)
#print("\nPreOrder------------------------------------>>")
#PreOrder(root)
#print("\nPostOrder------------------------------------>>")
#PostOrder(root)
