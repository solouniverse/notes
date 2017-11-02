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
	print("%s (%s), " %(root.data,root.isStringEnd), end="")
	for i in range(26):
		printTrieTree(root.links[i])
	
def searchWordInTrieTree(root, word):
	if(word == None):
		return True
	if(root == None):
		return False
	
	if(root.links[ord(word[0])-ord('a')] != None ):
		if(len(word) > 1):
			return(searchWordInTrieTree(root.links[ord(word[0])-ord('a')], word[1:]))
		else:
			if(not root.isStringEnd):
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
addWord(root, "abcde")
printTrieTree(root)
print("")
addWord(root, "xyz")
printTrieTree(root)
print("")
addWord(root, "abc")
printTrieTree(root)
print("")
addWord(root, "aac")
printTrieTree(root)
print("")
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

