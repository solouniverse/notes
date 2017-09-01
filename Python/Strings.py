
""" 
**********************************************
	String Objects
**********************************************
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.	
 |
 |  capitalize(...)
 |      S.capitalize() -> str
 |
 |      Return a capitalized version of S, i.e. make the first character
 |      have upper case and the rest lower case.
 |
 |  casefold(...)
 |      S.casefold() -> str
 |
 |      Return a version of S suitable for caseless comparisons.
 |
 |  center(...)
 |      S.center(width[, fillchar]) -> str
 |
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |
 |  encode(...)
 |      S.encode(encoding='utf-8', errors='strict') -> bytes
 |
 |      Encode S using the codec registered for encoding. Default encoding
 |      is 'utf-8'. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that can handle UnicodeEncodeErrors.
 |
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |
 |  expandtabs(...)
 |      S.expandtabs(tabsize=8) -> str
 |
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Return -1 on failure.
 |
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |
 |      Like S.find() but raise ValueError when the substring is not found.
 |
 |  isalnum(...)
 |      S.isalnum() -> bool
 |
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |
 |  isalpha(...)
 |      S.isalpha() -> bool
 |
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |
 |  isdecimal(...)
 |      S.isdecimal() -> bool
 |
 |      Return True if there are only decimal characters in S,
 |      False otherwise.
 |
 |  isdigit(...)
 |      S.isdigit() -> bool
 |
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |
 |  isidentifier(...)
 |      S.isidentifier() -> bool
 |
 |      Return True if S is a valid identifier according
 |      to the language definition.
 |
 |      Use keyword.iskeyword() to test for reserved identifiers
 |      such as "def" and "class".
 |
 |  islower(...)
 |      S.islower() -> bool
 |
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |
 |  isnumeric(...)
 |      S.isnumeric() -> bool
 |
 |      Return True if there are only numeric characters in S,
 |      False otherwise.
 |
 |  isprintable(...)
 |      S.isprintable() -> bool
 |
 |      Return True if all characters in S are considered
 |      printable in repr() or S is empty, False otherwise.
 |
 |  isspace(...)
 |      S.isspace() -> bool
 |
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |
 |  istitle(...)
 |      S.istitle() -> bool
 |
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
 |
 |  isupper(...)
 |      S.isupper() -> bool
 |
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |
 |  join(...)
 |      S.join(iterable) -> str
 |
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> str
 |
 |      Return S left-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).  
 |
 |  lower(...)
 |      S.lower() -> str
 |
 |      Return a copy of the string S converted to lowercase.
 |
 |  lstrip(...)
 |      S.lstrip([chars]) -> str
 |
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |
 |  replace(...)
 |      S.replace(old, new[, count]) -> str
 |
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Return -1 on failure.
 |
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> str
 |
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 | 
 |
 |  lower(...)
 |      S.lower() -> str
 |
 |      Return a copy of the string S converted to lowercase.
 |
 |  lstrip(...)
 |      S.lstrip([chars]) -> str
 |
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |
 |  replace(...)
 |      S.replace(old, new[, count]) -> str
 |
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Return -1 on failure.
 |
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> str
 |
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |
"""
#
# Creating of string object
#
In [1]: strng="Sri Matrenamaha"

In [2]: print(strng)
Sri Matrenamaha

In [3]: strng="12331213"

In [4]: strng
Out[4]: '12331213'

In [5]: number=12311123

In [6]: strng=str(number)

In [7]: strng
Out[7]: '12311123'

#
# str.capitalize() #Return a capitalized version of S, i.e. make the first
#				    character have upper case and the rest lower case
#
strng="sri Matrenamaha"
print(strng.capitalize())
print(strng)

#
In [10]: strng="sRi RAMA"
    ...: print(strng.capitalize())	# Return capilized version
    ...: print(strng)				# Doesn't change the original string variable
    ...:
Sri rama #Only first letter is upper cased all other letters are lower cased
sRi RAMA #String variable is unchanged.

# Input string doesnt have tobe a alphet only string can contain numbers, special chars etc.
In [12]: strng="sRi RAMA1212#@!"
    ...: print(strng.capitalize())
    ...: print(strng)
    ...:
Sri rama1212#@!
sRi RAMA1212#@!

#Notes: 
#1. Doesn't change the given string by doing inplace operation.
#2. first char is uppercased rest lowercased forcefully.
#3. Input string doesnt have tobe a alphabet only string can contain numbers, special chars etc.

#
#	str.casefold() Returns lowercase version of given string usefull in 
# 					caseless comparison
#
In [11]: strng="sRi RAMA1212#@!" #
    ...: print(strng.casefold())
    ...: print(strng)
    ...:
sri rama1212#@!   
sRi RAMA1212#@!
#Note: Input string doesnt have tobe a alphabet only string can contain numbers, special chars etc.

#
# str.center(width[, fillchar]) #Centers the given string within given width
# str.ljust(width[, fillchar]) -> str
# str.rjust(width[, fillchar]) -> str
#

In [13]: strng="sRi RAMA1212#@!"
    ...: print('|%s|' %strng.center(25))
    ...: print('|'+('----^'*5)+'|')
    ...: print('|%s|' %strng)
    ...:
|     sRi RAMA1212#@!     |
|----^----^----^----^----^|
|sRi RAMA1212#@!|
#
In [34]: print('|'+"Asdas".ljust(20)+'|')
    ...: print('|'+"Asdas".rjust(20)+'|')
    ...: print('|'+"Asdas".center(20)+'|')
    ...:
|Asdas               |
|               Asdas|
|       Asdas        |

#
#str.count(sub[, start[, end]]) 
#	Return the number of non-overlapping occurrences of substring.
#
In [14]: strng="Sri Rama Sri Sita"
    ...: print(strng.count('Sri')) 
    ...: strng="sri Rama Sri Sita" #Both 'sri's are of different case
    ...: print(strng.count('Sri'))
    ...: print((strng.casefold()).count('Sri'.casefold())) #finding no. of occurances of 'sri' of all cases.
    ...:
2
1
2
#	Counts only non overlapping occurances.
In [15]: "adadadada".count('ada')
Out[15]: 2
#Notes: 1. Counts only non overlapping occurances.
#2. canbe used with casefold() to find all occurences of different cases.

#
#	S.endswith(suffix[, start[, end]]) -> bool
#	Return True if S ends with the specified suffix, False otherwise.
#
In [16]: strng="Sri Rama Sri Sita"
    ...: print(strng.endswith('Sita'))
    ...: strng="Sri Rama Sri Sita."
    ...: print(strng.endswith('.'))
    ...:
True
True

#
#S.expandtabs(tabsize=8) -> str
#	Return a copy of S where all tab characters are expanded using spaces.
#
In [18]: strng="Sri\tRama\tSri\tSita"
    ...: print(strng)
    ...: print(strng.expandtabs(1))
    ...: print(strng.expandtabs(4))
    ...:
Sri     Rama    Sri     Sita
Sri Rama Sri Sita
Sri Rama    Sri Sita

#
# S.find(sub[, start[, end]]) -> int
#	Return the lowest index in S where substring sub is found
# S.rfind(sub[, start[, end]]) -> int
#	Return the highest index in S where substring sub is found
#
#
#	S.index(sub[, start[, end]]) -> int #returns lowest index of given substring
#	S.rindex(sub[, start[, end]]) -> int # returns highest index of given substring
#


In [19]: strng="Jai Sri Rama Sri Sita"
    ...: print(strng)
    ...: print(strng.find('Sri'))
    ...: print(strng.find('Sri', 7))
    ...:
Jai Sri Rama Sri Sita
4
13
In [40]: strng="Jai Sri Rama Sri Sita"
    ...: print(strng)
    ...: print(strng.rfind('Sri'))
    ...: print(strng.rfind('Sri', 7))
    ...:
    ...:
Jai Sri Rama Sri Sita
13
13
#Notes:
#1. rfind() & find() returns -1 if substring isnt found.
#2. rindex() & index() will raise "ValueError" if substring isnt found.
#

#
#S.format(*args, **kwargs) -> str
#	Return a formatted version of S, using substitutions from args and kwargs.
#
In [21]: print("Art: {},  Price: {}".format(453, 59.058)) # use {} for replacements
    ...: print("Art: {:5d},  Price: {:8.2f}".format(453, 59.058))# can mention the precision
    ...: print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058)) # can be passed using variable names.
    ...: print("Price: {p:8.2f},  Art: {a:5d}".format(a=453, p=59.058)) # using variable names we can pass args out pf sequence too.
    ...:
Art: 453,  Price: 59.058
Art:   453,  Price:    59.06
Art:   453,  Price:    59.06
Price:    59.06,  Art:   453
#Notes: http://www.python-course.eu/python3_formatted_output.php

#
# S.format_map(mapping) -> str
# 	Return a formatted version of S, using substitutions from mapping.
#
In [22]: my_map={'a':453, 'p':59.058}
    ...: print("Price: {p:8.2f},  Art: {a:5d}".format_map(my_map))
    ...: print('Price: {p},  Art: {a}'.format_map(my_map))
    ...:
Price:    59.06,  Art:   453
Price: 59.058,  Art: 453
#Note: Useful when multiple  lines are to be printed in different formats and dicts


#
#S.isalnum() -> bool
#	Return True if all characters in S are alphanumeric
#
In [25]: print("01203812369123".isalnum())
    ...: print("ABC123".isalnum())
    ...: print("ASBasdas".isalnum())
    ...: print("@#@!@".isalnum())  # Contains non alphanumerics
    ...: print("ABC123@#@!@".isalnum()) # Contains non alphanumerics
    ...:
    ...:
True
True
True
False
False

#
# S.isalpha() -> bool
#		Return True if all characters in S are alphabetic
#

In [26]: print("ASBasdas".isalpha()) 
    ...: print("01203812369123".isalpha()) # Contains non alphabets
    ...: print("ABC123".isalpha())# Contains non alphabets
    ...: print("@#@!@".isalpha())# Contains non alphabets
    ...: print("ABC123@#@!@".isalpha())# Contains non alphabets
    ...:
True
False
False
False
False

#
# S.isdecimal() -> bool
#
In [27]: print("ASBasdas".isdecimal()) # Contains non decimal
    ...: print("01203812369123".isdecimal())
    ...: print("01203812369123.123123".isdecimal())# Contains non decimal
    ...: print("ABC123".isdecimal())# Contains non decimal
    ...: print("@#@!@".isdecimal())# Contains non decimal
    ...: print("ABC123@#@!@".isdecimal())# Contains non decimal
    ...:
False
True
False
False
False
False

#
#S.isdigit() -> bool
#      Return True if all characters in S are digits
#      and there is at least one character in S, False otherwise.
#
In [28]: print("ASBasdas".isdigit())
    ...: print("01203812369123".isdigit())
    ...: print("".isdigit())
    ...: print("01203812369123.123123".isdigit())
    ...: print("ABC123".isdigit())
    ...: print("@#@!@".isdigit())
    ...: print("ABC123@#@!@".isdigit())
    ...:
False
True
False
False
False
False
False

#
#S.isidentifier() -> bool
#      Return True if S is a valid identifier according
#      to the language definition.
#
#       Use keyword.iskeyword() to test for reserved identifiers
#       such as "def" and "class".
# 
""" 
	isidentifier is a Python function that simply tests whether a string
 contains only certain characters (underscore, digits, and alphas) and 
 starts with an alpha or an underscore, so the string can be used for 
 a valid Python identifier. Other functions that test for character 
 classes are isalpha, isalnum, isdigit, and others.
"""
In [29]: ss = (
    ...:     'varABC123',
    ...:     '123ABCvar',
    ...:     '_123ABCvar',
    ...:     'var_ABC_123',
    ...:     'var-ABC-123',
    ...:     'var.ABC.123',
    ...: )
    ...:
    ...: fmt = '%-15s%-10s%-10s%-10s%-10s'
    ...: print(fmt % ('', 'isalpha', 'isalnum', 'isdigit', 'isidentifier'))
    ...: for s in ss:
    ...:     print(fmt % (s, s.isalpha(), s.isalnum(), s.isdigit(), s.isidentifier()))
    ...:
               isalpha   isalnum   isdigit   isidentifier
varABC123      False     True      False     True
123ABCvar      False     True      False     False
_123ABCvar     False     False     False     True
var_ABC_123    False     False     False     True
var-ABC-123    False     False     False     False
var.ABC.123    False     False     False     False

#
#	S.islower() -> bool
#
In [30]: print("asdas".islower())
    ...: print("ASBasdas".islower())
    ...: print("01203812369123".islower())
    ...: print("ABC123".islower())
    ...: print("ABC123@#@!@".islower())
    ...:
True
False
False
False
False
#
# S.isnumeric() -> bool
#
In [31]: print("01203812369123".isnumeric())
    ...: print("0120.3812369123".isnumeric())
    ...: print("ABC123".isnumeric())
    ...: print("ABC123@#@!@".isnumeric())
    ...: print("asdas".isnumeric())
    ...: print("ASBasdas".isnumeric())
    ...:
True
False
False
False
False
False
#
# S.isprintable() -> bool
# S.isspace() -> bool
# S.isupper() -> bool
#

#
#S.istitle() -> bool
'''
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
'''
#
In [32]: print("Asdas".istitle())
    ...: print("Mr.Asdas".istitle())
    ...: print("Mrs.Asdas".istitle())
    ...: print("Lt.Asdas".istitle())
    ...: print("01203812369123".istitle())
    ...: print("0120.3812369123".istitle())
    ...: print("ABC123".istitle())
    ...: print("ABC123@#@!@".istitle())
    ...: print("asdas".istitle())
    ...: print("ASBasdas".istitle())
    ...:
True
True
True
True
False
False
False
False
False
False
#
# S.join(iterable) -> str 
# Join elements of given "iterable" sperating with 'S'
#
In [33]: print("-".join([chr(x) for x in range(ord('a'),ord('z')+1)])) #chr(int) returns "char" equivalent to given ASCII 'int'
    ...: print("-".join([str(x) for x in range(ord('a'),ord('z')+1)])) #str(int) returns "string" equivalent to given 'int' number
    ...:
a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z
97-98-99-100-101-102-103-104-105-106-107-108-109-110-111-112-113-114-115-116-117-118-119-120-121-122

#
# S.lower() -> str
# S.upper() -> str
#

In [36]: print("ASBasdaS".lower())
    ...: print("ASBasdaS".upper())
    ...:
asbasdas
ASBASDAS

#
#	S.lstrip([chars]) -> str # remove given chars or whitespaces from left side
#	S.rstrip([chars]) -> str # remove given chars or whitespaces from right side
#	S.strip([chars]) -> str  # remove given chars or whitespaces from both left and right sides
#

In [37]: print('|'+"  ASBasdaS  ".lstrip()+'|')
    ...: print('|'+"  ASBasdaS  ".rstrip()+'|')
    ...: print('|'+"  ASBasdaS  ".strip()+'|')
    ...:
|ASBasdaS  |
|  ASBasdaS|
|ASBasdaS|

#
#	S.partition(sep) -> (head, sep, tail)
'''
 Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
'''
#	S.rpartition(sep) -> (head, sep, tail)
#
In [38]: print("Mr.Asdas".partition('sd'))
    ...:
('Mr.A', 'sd', 'as')
In [39]: print("Mr.Asdas".partition('ad'))
    ...:
('Mr.Asdas', '', '')
#
In [42]: print(strng.partition('Sri'))
    ...: print(strng.rpartition('Sri'))
    ...:
('Jai ', 'Sri', ' Rama Sri Sita')
('Jai Sri Rama ', 'Sri', ' Sita')

#
#	S.rsplit(sep=None, maxsplit=-1) -> list of strings
#
In [43]: print('OmRama JaiRama SriRama'.rsplit())
    ...: print('OmRama JaiRama SriRama'.split())
    ...:
['OmRama', 'JaiRama', 'SriRama']
['OmRama', 'JaiRama', 'SriRama']

In [44]: print('OmRama JaiRama SriRama JaiJaiRama'.rsplit(" ",1))
    ...: print('OmRama JaiRama SriRama JaiJaiRama'.split(" ",1))
    ...:
['OmRama JaiRama SriRama', 'JaiJaiRama']
['OmRama', 'JaiRama SriRama JaiJaiRama']
# Notes: In the absence of "maxsplit" split&rsplit works same

#
# S.splitlines([keepends]) -> list of strings
#
In [45]: print("""OmRama JaiRama SriRama JaiJaiRama
    ...: Sri Sita JaiSita JaiJai Sita
    ...: Sri Hanuman JaiHanuman JaiJaiHanuman""".splitlines())
    ...:
['OmRama JaiRama SriRama JaiJaiRama', 'Sri Sita JaiSita JaiJai Sita', 'Sri Hanuman JaiHanuman JaiJaiHanuman']

#
# S.swapcase() -> str
#
In [46]: print('OmRama JaiRama SriRama JaiJaiRama'.swapcase())
oMrAMA jAIrAMA sRIrAMA jAIjAIrAMA

#
# S.title() -> str
#
In [47]: print('omRama JaiRama SriRama JaiJaiRama'.title())
Omrama Jairama Srirama Jaijairama

#
# S.startswith(prefix[, start[, end]]) -> bool
#
In [48]: print('OmRama JaiRama SriRama JaiJaiRama'.startswith('Om'))
    ...: print('OmRama JaiRama SriRama JaiJaiRama'.startswith('Jai',7))
    ...: print('OmRama JaiRama SriRama JaiJaiRama'.startswith(('Om','Jai','Sri')))
    ...:
True
True
True
#Note: Prefix can be a string or tuple of trings to try with

#
#  S.translate(table) -> str
#	Return a copy of the string S in which each character has been mapped
#   through the given translation table.
#

#creation of translation Table
In [54]: str.maketrans('Rama','Sita')
Out[54]: {82: 83, 97: 97, 109: 116}

#
In [53]: print('OmRama JaiRama SriRama JaiJaiRama'.translate(str.maketrans('Rama','Sita')))
    ...:
OtSata JaiSata SriSata JaiJaiSata

#
#  S.zfill(width) -> str #Pad a numeric string S with zeros on the left,
#
In [56]: print("omrama".zfill(10))
    ...: print("omrama".zfill(1)) #Doesnt truncate the word
    ...:
0000omrama
omrama
