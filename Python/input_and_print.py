""" 
**********************************************
	print() print to screen
**********************************************
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.	
"""

print("Sri MatreNamaha!")	# Simple String
'''Output:
Sri MatreNamaha!
'''
x=1
y='Sri'
z=[1,2,3,4]
a={0:123,1:'qwe'}
print(x,y,z,a)				# A list of variables
'''Output:
1 Sri [1, 2, 3, 4] {0: 123, 1: 'qwe'}  # seprated by spaces
'''
print(x,y,z,a, sep='-')
'''Output:
1-Sri-[1, 2, 3, 4]-{0: 123, 1: 'qwe'}
'''
print(x,y)					#print them in separate lines
print(z,a)					#
'''Output:
1 Sri
[1, 2, 3, 4] {0: 123, 1: 'qwe'}
'''

print(x,y,end=" ")			#print " " instead of '\n' at the end of line
print(z,a)					#keeps both print outputs in a single line
'''Output:
1 Sri [1, 2, 3, 4] {0: 123, 1: 'qwe'}  
'''


# Formatted print()
#Using "str.format()"
In [14]: var=[1,2,3,4,5,1,1,1]
    ...: var2=var.copy()
    ...: print(var,var2,sep='\n')
    ...: print("id(var):{}\nid(var2):{}".format(id(var), id(var2)))
    ...:
[1, 2, 3, 4, 5, 1, 1, 1]
[1, 2, 3, 4, 5, 1, 1, 1]
id(var):2263810057096
id(var2):2263809862344


""" 
**********************************************
	input() Read input from keyboard, strip trailing '\n'
**********************************************
input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
"""

value=input("Enter: ")		# prompts with given string "Enter"
print(value)				
'''Output:
Enter: Srirama
Srirama
'''
