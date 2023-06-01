from random import *
array = []
for i in range(2000):
    array.append(randint(1, 10000))

array.sort()
print(array)

def primitive_sort(array,target):
    found = False
    x=0
    while found == False:
        if array[x] == target :
            print("Target",target,"found at index",x,"or position",x+1,"in the array")
            found = True
        elif x == len(array)-1:
            print("Element",target," couldn't be found, Element is not in this list")
            break
        else:
            x+=1

primitive_sort(array,randint(0,10000))