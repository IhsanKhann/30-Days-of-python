#Create a tuple of 5 colors and print each color using a loop.
colors = ("Yellow" , "Orange", "Green", "Blue", "Purple")
print(colors)

#Find the index of a specific element in a tuple:
list1 = (1,2,3,4,5)
print(list1.index(5))

#Convert a tuple into a list, modify it, and convert it back into a tuple.
colors = ("Yellow", "Orange", "Green", "Blue" , "Purple")
list2 = list(colors) #convert tuple into list 

list2[0] = "Green"
list2[1] = "Yellow"
list2[2] = "Maroon"

newColors = tuple(list2) #empty tuple
print("New Colors: ", newColors)

#count Occurences:
tuple1 = (1,1,2,2,3,2,1,5,6,7)
countList = []

noDuplicates = set(tuple1) #now all the duplicates are removed. 

for i in noDuplicates: #we only iterate once for one element.
    count = tuple1.count(i) #count the number. Its parameter is the number.
    countList.append((i,count))
    
print("The count of each element is: ", countList)

tuple2 = (1,2,3,4,5)
tuple3 = (6,7,8,9,10)
newList = []

list3 = list(tuple2)
for i in list3:
    newList.append(i)
    
list4 = list(tuple3)
for i in list4:
    newList.append(i)
    
newTuple = tuple(newList)

print(f"Join this {tuple2} with {tuple3} ")
print("The Concatenated tuple is: ", newTuple)

#Find the sum of all elements in a tuple.
Sum = 0
for i in newTuple:
    Sum += i
print("The Sum of the tuple is: ", Sum)

#Check if a given element exists in a tuple:
#apply the linear search:
key = 10
isFound = False
for i in newTuple:
    if (key == i):
        isFound = True
    else:
        isFound = False
        
if(isFound):
    print(f"The element {key} is Present.")
else:
    print(f"The element {key} is not Present.")

#Convert a tuple of numbers into a tuple of their squares.
tuple5 = (1,2,3,4,5)
list5 = list(tuple5)
list6 = []
ans = 0

for i in list5:
    ans = i*i 
    list6.append(ans)
    
SquaredTuple = tuple(list6)
print ("The Squared tuple is: ", SquaredTuple)

#Unpack a tuple into separate variables.
tuple7 = (1,2,3,4,5)
list7 = list(tuple7)

var1 = list7[0]
var2 = list7[1]
var3 = list7[2]
var4 = list7[3]
var5 = list7[4]

print (f"{var1} {var2} {var3} {var4} {var5}")

