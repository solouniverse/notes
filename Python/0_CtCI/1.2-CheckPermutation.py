def using_sorted_string(string1, string2):
	if(len(string1) == len(string2)):
		if(sorted(string1) == sorted(string2)):
			print("They are permutations")
		else:
			print("They are not permutations")
	else:
		print("They are not permutations")

def using_Counter(string1, string2):
	if(len(string1) == len(string2)):
		import collections
		if(collections.Counter(string1) == collections.Counter(string2)):
			print("They are permutations")
		else:
			print("They are not permutations")
	else:
		print("They are not permutations")

"""
Example how to implement "collections.Counter":
for x in range(string1):
	for y in range(string1[x+1:]):
		if (string1[x]==string1[y]):
			try:
				counter(x)+=1
			except:
				counter(x)=1
				
len(string1)*len(string1)+len(string2)*len(string2)

2N^2+2N
"""

"""
The below logic doesn't work
def test_1(string1, string2):
	if(len(string1) == len(string2)):
		for x in string1:
			if x not in string2:
				print("They are not permutations")
				break
		else:
			print("They are permutations")
	else:
		print("They are not permutations")
	
test_1("abbc", "abac")
exit()
"""

def using_character_count(string1, string2):
	if(len(string1) == len(string2)):
		for x in string1:
			if (string2.count(x) != string1.count(x)):
				print("They are not permutations")
				break
		else:
			print("They are permutations")
	else:
		print("They are not permutations")

string1="qwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiop"
string2="zxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiopzxcvbnmasdfghjklqwertyuiop"
import cProfile
cProfile.run("using_sorted_string(string1, string2)")
cProfile.run("using_Counter(string1, string2)")
cProfile.run("using_character_count(string1, string2)")

"""
Sample Output:
They are permutations
         9 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 1.2-CheckPermutation.py:1(using_sorted_string)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        2    0.003    0.002    0.003    0.002 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


They are permutations
         139 function calls (127 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 1.2-CheckPermutation.py:10(using_Counter)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        2    0.000    0.000    0.001    0.001 __init__.py:519(__init__)
        2    0.000    0.000    0.001    0.000 __init__.py:588(update)
        7    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
        7    0.000    0.000    0.000    0.000 _weakrefset.py:16(__init__)
        7    0.000    0.000    0.000    0.000 _weakrefset.py:20(__enter__)
        7    0.000    0.000    0.000    0.000 _weakrefset.py:26(__exit__)
        3    0.000    0.000    0.000    0.000 _weakrefset.py:36(__init__)
        7    0.000    0.000    0.000    0.000 _weakrefset.py:52(_commit_removals)
        9    0.000    0.000    0.000    0.000 _weakrefset.py:58(__iter__)
       14    0.000    0.000    0.000    0.000 _weakrefset.py:70(__contains__)
        7    0.000    0.000    0.000    0.000 _weakrefset.py:81(add)
        2    0.000    0.000    0.000    0.000 abc.py:178(__instancecheck__)
      7/1    0.000    0.000    0.000    0.000 abc.py:194(__subclasscheck__)
        2    0.001    0.000    0.001    0.000 {built-in method _collections._count_elements}
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
      8/2    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        7    0.000    0.000    0.000    0.000 {method '__subclasses__' of 'type' objects}
       14    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        7    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}


They are permutations
         3751 function calls in 0.047 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004    0.047    0.047 1.2-CheckPermutation.py:52(using_character_count)
        1    0.000    0.000    0.047    0.047 <string>:1(<module>)
        1    0.000    0.000    0.047    0.047 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.print}
     3744    0.042    0.000    0.042    0.000 {method 'count' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




"""
