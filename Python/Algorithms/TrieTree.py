class TrieTreeNode():
	def __init__(self, data):
		self.data=data
		self.isStringEnd=0
		#26 if we consider all words are only lowercase letters.
		self.links=[None for x in range(ord('a'), ord('z')+1)]

def addWord(root, word):
	tempRoot=root
	for x in word:
		if(tempRoot.links[(ord(x)-ord('a'))] == None):
			tempRoot.links[(ord(x)-ord('a'))]=TrieTreeNode(x)
		tempRoot=tempRoot.links[(ord(x)-ord('a'))]

	tempRoot.isStringEnd=1

def printTrieTree(root):
	if(root==None):
		return
	print("%s-%d, " %(root.data,root.isStringEnd), end="")
	
	for i in range(26):
		printTrieTree(root.links[i])

def deleteWordTrieTree(root, word):
#True word found and deleted.
#False word not found.
#-1
	if(word == None):
		return True

	if(root == None):
		return False

	if(word == ""):
		for i in range(26):
			if(root.links[i] != None):
				root.isStringEnd=0
				return True
			else:
				del (root)
				return -1

	if(root.links[ord(word[0])-ord('a')] != None ):
			status = deleteWordTrieTree(root.links[ord(word[1])-ord('a')], word[1:])
			if(status == -1):
				root.links[ord(word[1])-ord('a')]=None
				if(root.isStringEnd):
					return True
					
				for i in range(26):
					if(root.links[i] != None):
						return True
				else:
					del(root)
					return -1
			else:
				return status
	else:
		return False


def printWordsTrieTree(root, prevWord):
	if(root==None):
		return
	prevWord=prevWord+root.data
	if(root.isStringEnd):
		print(prevWord)
	for i in range(26):
		printWordsTrieTree(root.links[i], prevWord)

def countNumberOfWordsTrieTree(root):
	if(root==None):
		return 0
	print("%s-%d, " %(root.data,root.isStringEnd), end="")
	count=root.isStringEnd
	for i in range(26):
		count+=countNumberOfWordsTrieTree(root.links[i])
	return count

def searchWordInTrieTree(root, word):
	if(word == None or word == ""):
		return True
	if(root == None):
		return False
	
	if(root.links[ord(word[0])-ord('a')] != None ):
		if(len(word) > 1):
			return(searchWordInTrieTree(root.links[ord(word[0])-ord('a')], word[1:]))
		else:
			if(root.links[ord(word[0])-ord('a')].isStringEnd):
				return True
			else:
				return False
	else:
		return False

	return True

def printTrieTreeSingle(root):
	tempRoot=root
	while(not tempRoot.isStringEnd):
		for i in range(26):
			if(tempRoot.links[i] !=None):
				tempRoot=tempRoot.links[i]
				print("%s (%s), " %(tempRoot.data,tempRoot.isStringEnd), end="")
	print("")

root=TrieTreeNode('')
print("abcde")
addWord(root, "abcde")
#printTrieTree(root)
print("\nxyz")
addWord(root, "xyz")
#printTrieTree(root)
print("\nabc")
addWord(root, "abc")
#printTrieTree(root)
print("\naac")
addWord(root, "aac")
printTrieTree(root)
print("")
print(countNumberOfWordsTrieTree(root))

printWordsTrieTree(root, "")
print(deleteWordTrieTree(root, "abc"))
print("")
printTrieTree(root)

printWordsTrieTree(root, "")
exit()
for x in ["aac","a","ab","abc","abcd","abcde"]:
	print(x,searchWordInTrieTree(root, x))



"""
abcd 26
string="ab"
myTrieTree=TrieTreeNode(string[0])
TempTrieTree=TrieTreeNode(string[1])
myTrieTree.links[(ord(string[1])-ord('a'))]=TempTrieTree

[]

none

myTrieTree.data=string[0]


self.data==string[0]
self.links[(ord(string[1])-ord('a'))] != None
"""

