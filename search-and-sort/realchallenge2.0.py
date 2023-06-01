from random import *
array = []
for i in range(20):
    array.append(randint(1, 20))
array.sort()
print(array)

# You are stupid, that's why
# Have you ever considered the possibility, that the element you search for doens't exist in the array
# You fucking moron, the loop just goes on and on without finding your target
# Like, a 3 year old toddler could have found this trivial bug
# You didn't even do it recursively you dumb fuck
# Jesus would not be proud of you
# Your're going to hell, YOu're going to hell, YOU're going to Hell, YOU'Re going to Hell, YOU'RE going to hell, YOU'RE Going to Hell, YOU'RE GOing to Hell, YOU'RE GOIng to Hell, YOU'RE GOINg to Hell, YOU
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search(array, 6))
