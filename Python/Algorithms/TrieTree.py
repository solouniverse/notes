class TrieTreeNode():
	def __init__(self, data):
		self.data=data
		self.isStringEnd=0
		#26 if we consider all words are only lowercase letters.
		self.links=[None for x in range(ord('a'), ord('z')+1)]

def addWord(root, word):
	if(word == "" or word == None):
		return
	if(root == None):
		return
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
#-1 I have deleted my node please check yours.

	if(word == None):
		return True

	if(root == None):
		return False

	if(root.data == ""):
		print("Deleting \"%s\" from the Trie tree.." %word)

	if(word == "" and root.data != ""):
		if(root.isStringEnd==0):
			return False
					
		for i in range(26):
			if(root.links[i] != None):
				root.isStringEnd=0
				return True
		else:
			del (root)
			return -1

	if(root.links[ord(word[0])-ord('a')] != None ):
			status = deleteWordTrieTree(root.links[ord(word[0])-ord('a')], word[1:])
			if(status == -1):
				root.links[ord(word[0])-ord('a')]=None
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
		return 0

	count=0
	prevWord=prevWord+root.data
	if(root.isStringEnd):
		print(prevWord)
		count+=1

	for i in range(26):
		count+=printWordsTrieTree(root.links[i], prevWord)

	return count

def getWordsTrieTree(root, prevWord):
	if(root==None):
		return [0,[]]

	count=0
	myList=[]
	prevWord=prevWord+root.data
	if(root.isStringEnd):
		myList.append(prevWord)
		count+=1

	for i in range(26):
		[tempCount,tempList]=getWordsTrieTree(root.links[i], prevWord)
		myList.extend(tempList)
		count+=tempCount

	return [count,myList]

def printPreFixMatchingWordsTrieTree(root, preFix):

	if(root==None):
		return
	for _ in preFix:
		if(root.links[ord(_)-ord('a')] != None):
			root=root.links[ord(_)-ord('a')]
		else:
			print("No Matching words found!")
			return False
	print("Printing matching words:")
	
	printWordsTrieTree(root, preFix[:-1])

def printMatchingWordsTrieTree(root, pattern, prevWord):
#See if the traversal of tree matches with the given pattern. Then
#Print all the words after matching nodes prefixing string upto now

	if(root==None):
		return 0
	if(root.data == ""): #Check if its root node
		print("Searching for pattern \"%s\" in the Trie tree.." %pattern)

	count=0
	prevWord=prevWord+root.data
	temp=root
	tempPrevWord=prevWord
	for _ in pattern:
		if(temp.links[ord(_)-ord('a')] != None):
			temp=temp.links[ord(_)-ord('a')]
			tempPrevWord+=temp.data
		else:
			break
	else:
		count+=printWordsTrieTree(temp, tempPrevWord[:-1])
	
	for i in range(26):
		count+=printMatchingWordsTrieTree(root.links[i],pattern, prevWord)

	if(root.data == ""): #Check if its root node
		if(count==0):
			print("No matches found for pattern: \"%s\"" %pattern)
		else:
			print("Total matches found for pattern: \"%d\"" %count)

	return count
	
def getMatchingWordsTrieTree(root, pattern, prevWord):
#See if the traversal of tree matches with the given pattern. Then
#Collect all the words after matching nodes and pass them to the caller
	if(root==None):
		return [0,[]]
	if(root.data == ""):#Check if its root node
		print("Searching for pattern \"%s\" in the Trie tree.." %pattern)

	count=0
	myList=[]
	prevWord=prevWord+root.data
	temp=root
	tempPrevWord=prevWord
	for _ in pattern:
		if(temp.links[ord(_)-ord('a')] != None):
			temp=temp.links[ord(_)-ord('a')]
			tempPrevWord+=temp.data
		else:
			break
	else:
		[tempCount,tempList]=getWordsTrieTree(temp, tempPrevWord[:-1])
		myList.extend(tempList)
		count+=tempCount		
	
	for i in range(26):
		[tempCount,tempList]=getMatchingWordsTrieTree(root.links[i],pattern, prevWord)
		myList.extend(tempList)
		count+=tempCount		

	if(root.data == ""):#Check if its root node
		if(count==0):
			print("No matches found for pattern: \"%s\"" %pattern)
		else:
			print("Total matches found for pattern: \"%d\"" %count)

	return [count,myList]
	
def countNumberOfWordsTrieTree(root):
	if(root==None):
		return [0,0]

	countWords=root.isStringEnd
	countNodes=1
	count=0
	for i in range(26):
		[TempNodeC,TempWordC]=countNumberOfWordsTrieTree(root.links[i])
		countNodes+=TempNodeC
		countWords+=TempWordC

	if(root.data == ""):#Check if its root node
		print("Total number of words and nodes in tree are: %d %d" %(countWords, countNodes))

	return [countNodes, countWords]

def countNumberOfNodesTrieTree(root):
	if(root==None):
		return 0
	
	count=1
	for i in range(26):
		count+=countNumberOfNodesTrieTree(root.links[i])
	if(root.data == ""):#Check if its root node
		print("Total number of *nodes* in tree are: %d" %count)

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

def testTrieTreeWithDictionary(root):
	text_file = open("words.txt", "r")
	words = text_file.read().split('\n')
	#print(len(words))
	for _ in words:
		addWord(root, _)
	return root

def validateTrieWithDictionary(root):
	text_file = open("words.txt", "r")
	words = text_file.read().split('\n')
	text_file.close()
	wordsMissing=0
	for x in words:
		if(not searchWordInTrieTree(root, x)):
			print("%s not found!" %x)
			wordsMissing+=1

	if(wordsMissing):
		print("%d words are missing" %wordsMissing)
	else:
		print("All the words are found in the Trie Tree!")

def searchNormal(pattern):
	text_file = open("words.txt", "r")
	words = text_file.read().split('\n')
	text_file.close()
	wordsFound=0
	for x in words:
		if(pattern in x):
			#print(x)
			wordsFound+=1

	if(wordsFound):
		print("Words found: %d " %wordsFound)
	else:
		print("No matching found in the Trie Tree!")
		
def searchDictionary():
	text_file = open("words.txt", "r")
	words = text_file.read().split('\n')
	text_file.close()
	wordsFound=0
	for x in words:
		for x in words:
			if(pattern in x):
				#print(x)
				wordsFound+=1

	if(wordsFound):
		print("Words found: %d " %wordsFound)
	else:
		print("No matching found in the Trie Tree!")

def CompareSearches(root, pattern):
	import cProfile
	cProfile.run("searchNormal(pattern)")
	cProfile.run("validateTrieWithDictionary(root)")

root=TrieTreeNode('')

print("Building Trie Tree...")
root=testTrieTreeWithDictionary(root)
print("...done!")
import cProfile
pattern="ab"
cProfile.run("validateTrieWithDictionary(root)")
cProfile.run("searchDictionary()")

#CompareSearches(root, "ab")
#printPreFixMatchingWordsTrieTree(root, "abc")
#printMatchingWordsTrieTree(root, "cd", "")
#print(getMatchingWordsTrieTree(root, "cd", ""))



exit()
countNumberOfWordsTrieTree(root)

string="zymotechny,zymotic,zymotically,zymotize"

for _ in string.split(","):
	deleteWordTrieTree(root, _)


countNumberOfWordsTrieTree(root)
validateTrieWithDictionary(root)

exit()

for x in ["aac","a","ab","abc","abcd","abcde","xyz","pqrs"]:
	addWord(root, x)

printWordsTrieTree(root, "")
#print(getWordsTrieTree(root, ""))
print(getMatchingWordsTrieTree(root, "cd", ""))
#countNumberOfWordsTrieTree(root)
#printPreFixMatchingWordsTrieTree(root, "abc")
#printMatchingWordsTrieTree(root, "cdf", "")
exit()

print(countNumberOfNodesTrieTree(root))
print(deleteWordTrieTree(root, "abc"))
print("")
printWordsTrieTree(root, "")
print(countNumberOfWordsTrieTree(root))
print(countNumberOfNodesTrieTree(root))
exit()
printWordsTrieTree(root, "")
print(deleteWordTrieTree(root, "abc"))
print("")
printTrieTree(root)

printWordsTrieTree(root, "")
exit()
for x in ["aac","a","ab","abc","abcd","abcde"]:
	print(x,searchWordInTrieTree(root, x))

"""
#Running each word indictionary against it using regular and Trie tree methods

cProfile.run("validateTrieWithDictionary(root)")
cProfile.run("searchDictionary()")


Building Trie Tree...
...done!
All the words are found in the Trie Tree!
         25526169 function calls (21727057 primitive calls) in 7.064 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.009    0.009    7.064    7.064 <string>:1(<module>)
4254360/455248    5.696    0.000    6.896    0.000 TrieTree.py:219(searchWordInTrieTree)
        1    0.102    0.102    7.055    7.055 TrieTree.py:255(validateTrieWithDictionary)
        1    0.000    0.000    0.000    0.000 _bootlocale.py:11(getpreferredencoding)
        1    0.000    0.000    0.000    0.000 codecs.py:259(__init__)
        1    0.000    0.000    0.011    0.011 cp1252.py:22(decode)
        1    0.011    0.011    0.011    0.011 {built-in method _codecs.charmap_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _locale._getdefaultlocale}
        1    0.000    0.000    7.064    7.064 {built-in method builtins.exec}
  4254359    0.255    0.000    0.255    0.000 {built-in method builtins.len}
 17017436    0.945    0.000    0.945    0.000 {built-in method builtins.ord}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {method 'close' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.005    0.005    0.016    0.016 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.041    0.041    0.041    0.041 {method 'split' of 'str' objects}


Words found: 6585617568
         13 function calls in 12395.065 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008 12395.065 12395.065 <string>:1(<module>)
        1 12395.000 12395.000 12395.056 12395.056 TrieTree.py:284(searchDictionary)
        1    0.000    0.000    0.000    0.000 _bootlocale.py:11(getpreferredencoding)
        1    0.000    0.000    0.000    0.000 codecs.py:259(__init__)
        1    0.000    0.000    0.011    0.011 cp1252.py:22(decode)
        1    0.011    0.011    0.011    0.011 {built-in method _codecs.charmap_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _locale._getdefaultlocale}
        1    0.000    0.000 12395.065 12395.065 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.004    0.004    0.016    0.016 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.041    0.041    0.041    0.041 {method 'split' of 'str' objects}




------------------
(program exited with code: 0)

Press any key to continue . . .
"""
