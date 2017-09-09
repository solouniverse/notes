import sys
n=212312
#partners="123"
partners=0
try:
	print("Percandidate",n/partners)

except ZeroDivisionError as z :
	print(z) # prints only the exception message in this case "division by zero"
else:
	print("Hurray no exceptions today!!!")

exit()
#Writing Exception Classes

import sys
class myexcep(Exception):
	pass	# No need to terminate program from inside exception class it 
			#will automatcally terminates once it finds a exception

try:
	raise myexcep
except myexcep:
	print("Got execption",sys.exc_info()[0])
	print(".. and handled safely...")
	
print("can you reach here?")

exit()
"""
In [5]: help(sys.exc_info)
Help on built-in function exc_info in module sys:

exc_info(...)
    exc_info() -> (type, value, traceback)

    Return information about the most recent exception caught by an except
    clause in the current stack frame or in an older stack frame.

"""

import sys
n=212312
#partners="123"
partners=0
try:
	print("Percandidate",n/partners)

except :
	execp_t = sys.exc_info()
	#print(execp_t[0],ZeroDivisionError)
	if(execp_t[0] == TypeError):
		print("Found TypeError")
	elif(execp_t[0] == ZeroDivisionError):
		print("Found ZeroDivisionError")
	else:
		print("***Found  "+str(execp_t))
else:
	print("Hurray no exceptions today!!!")

exit()
import sys
n=212312
partners="123"
#partners=0
try:
	#print("Percandidate",n/partners)
	try:
		1/0
	except TypeError:
		#print(sys.exc_info())
		print("Caught from inside!!")
	
	print("Percandidate,n/partners")	

except (TypeError, ZeroDivisionError):
	#print(sys.exc_info())
	print("Caught from ***OUTSIDE***!!")
except :
	print(sys.exc_info())
	print("I dont know what happend exactly :(!")
	raise 
else:
	print("Hurray no exceptions today!!!")

exit()
import sys
n=212312
partners="123"
#partners=0
try:
	print("Percandidate",n/partners)
	#print("Percandidate", partner)
		
except (TypeError, ZeroDivisionError):
	print(sys.exc_info())
except :
	print(sys.exc_info())
	print("I dont know what happend exactly :(!")
	raise 
else:
	print("Hurray no exceptions today!!!")


exit()
import sys
n=212312
partners="123"
#partners=0
try:
	print("Percandidate",n/partners)
	#print("Percandidate", partner)
		
except TypeError:
	print(sys.exc_info())
	print("Got type error!")
	print("Percandidate", int(n)/int(partners))
	
except ZeroDivisionError:
	print(sys.exc_info())
	print("Got ZeroDivisionError error!")
	print("As there are no partners, the amount will not be shared!")
except :
	print(sys.exc_info())
	print("I dont know what happend exactly :(!")
	raise 
else:
	print("Hurray no exceptions today!!!")

