.insert() first give position, add this element.
.remove() remove the first element
.pop() remove the element at specified position.
.append()
.copy()
.count()

these are left: 
.sort()
.reverse()

list = [1,2,3,4,5,6,7,8,9,10]
print(list[1::2])
# this is prinitng even numbers in a list using "Splicing"

#method2:
for i in list:
    if(i%2 == 0):
        print(i)

#Ask the user for 5 names and store them in a list. Sort the list and print it.
names = []
for i in range(5):
    x = input("Enter a name: ")
    names.append(x)
    
names.sort(reverse=False) #sorted out.
print (names)

#Remove duplicates from a list.
mylist = [1,2,3,1,2,3,4,5,6]
# myset = {} - this is wrong you make an empty dicitionary using this.
myset = set() # this is the correct way to declare an empty set.

for i in mylist:
    myset.add(i)
    
print(myset) # all the dupicates removed. Only one single copy of one single element.

#Find the maximum and minimum number in a list without using max() and min().
#Find the second-largest number in a list.
ihsan = [1,2,3,4,5,6]
max = ihsan[0]
min = ihsan[0]

for i in ihsan:
    if(i > max):
        max = i
        
for i in ihsan:
    if(i < min):
        min = i
        
print(f"Max number is: {max}")
print(f"Min number is: {min}")

second_Max = ihsan[0]
for i in ihsan:
    if(i < max and i > second_Max):
        second_Max = i
        
print("The Second max element is: ", second_Max )
#ihsan[1,2,3,4,5,6]
#mylist -----------
newlist = []
sizeIhsan = len(ihsan)
sizemyList = len(mylist)

totalSize = sizeIhsan + sizemyList 
for i in ihsan:
    newlist.append(i)
    
for i in mylist:
    newlist.append(i)
    
print("Merged list is: ", newlist)
print("Size of newlist is: ", len(newlist))

x = set() #empty set
for i in ihsan:
    x.add(i)
    
print(i)

#Reverse a list without using reverse() or [::-1].
list1 = [1,2,3,4,5,6]
temp = 0
start = 0
end = len(list1) - 1

while(start <= end):
    temp = list1[start]
    list1[start] = list1[end]
    list1[end] = temp
    
    start += 1
    end -= 1

print("The Original list is: ", list1)
print("The reversed list is: ", list1)

#Create a list of 10 numbers and find their sum and average:
list2 = [1,2,3,4,5,6,7,8,9,10]
Sum = 0
average = 0
for i in list2:
    Sum += i

average = Sum/len(list2)
print("Sum is: ", Sum)
print("Average is: ", average )


