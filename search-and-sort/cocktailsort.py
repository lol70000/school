from random import *
array = []
for i in range(20):
    array.append(randint(1, 100))

print (array)

#https://www.javatpoint.com/cocktail-sort#:~:text=Cocktail%20sort%20is%20the%20variation,backward%20direction%20in%20one%20iteration.

def cocktailsort(array):
    sorted = False
    start = 0 
    end = len(array)-1
    while sorted == False :
        sorted = True
        for i in range(start,end):
            if(array[i] > array[i+1]):
                array[i],array[i+1] = array[i+1], array[i]
                sorted = False
        
        if sorted == True :
            break

        sorted = True
        end -= 1

        for i in range(end-1,start-1,-1):
            if(array[i] > array[i+1]):
                array[i],array[i+1] = array[i+1], array[i]
                sorted = False
        
        start += 1
    return array

print(cocktailsort(array))