#9346462859,9849149829
#Total 100
#Hash function
def mod_99(x):
	return int(x)%100
	
def hash_into_2digits(x):
	index=0
	while(x>0):
		index+=x%100
		x=x//100
	if index >= 100:
		index= hash_into_2digits(index)
	return index
	
def hash_into_2digitsV2(x):
	index=1
	while(x>0):
		index*=x%100
		x=x//100
	if index >= 100:
		index= hash_into_2digitsV2(index)
	return index
	
def hash_into_log2(x):
	index=0
	while((2**index) < x):
		index+=1
	
	if index >= 100:
		index= hash_into_log2(index)
	return index

def load_factor(hased_entries):
	total=100
	print("load_factor: (%d)/(%d), %f" %(hased_entries,total, hased_entries/total))
import collections 
inputs="7871006001 7871006002 7871006003 7871006004 7871006005 7871006006 7871006007 7871006008 7871006009 7871006010 7871006011 7871006012 7871006013 7871006014 7871006015 7871006016 7871006017 7871006018 9986182001 9986182002 9986182003 9986182004 9986182005 9986182006 9986182007 9986182008 9986182009 9986182010 9986182011 9986182012 9986182013 9986182014 9986182015 9986182016 9986182017 9986182018 9986182019 9986182020 9986182021 8658136001 8658136002 8658136003 8658136004 8658136005 8658136006 8658136007 8658136008 8658136009 8658136010 8658136011 8658136012 8658136013 8658136014 8658136015 8658136016 8658136017 8658136018 8658136019 8658136020 8658136021 8658136022 8658136023 8658136024 8658136025 8658136026 8658136027 8658136028 8658136029 8658136030 8658136031 8658136032 8658136033 8658136034 8658136035 8658136036 8658136037 8658136038 8658136039 8658136040 8658136041 8658136042"
inputs_list=inputs.split(" ")
print("Total Items: ",len(inputs_list))
print("\nUsing mod_99*****")
hashed_inputs=[mod_99(_) for _ in inputs_list]
print(collections.Counter(hashed_inputs).most_common(10))
load_factor(len(set(hashed_inputs)))
print("\nUsing hash_into_2digits")
hashed_inputs=[hash_into_2digits(int(_)) for _ in inputs_list]
print(collections.Counter(hashed_inputs).most_common(10))
load_factor(len(set(hashed_inputs)))

print("\nUsing hash_into_2digitsV2")
hashed_inputs=[hash_into_2digitsV2(int(_)) for _ in inputs_list]
print(collections.Counter(hashed_inputs).most_common(10))
load_factor(len(set(hashed_inputs)))

print("\nUsing hash_into_log2")
hashed_inputs=[hash_into_log2(int(_)) for _ in inputs_list]
print(collections.Counter(hashed_inputs).most_common(10))
load_factor(len(set(hashed_inputs)))

