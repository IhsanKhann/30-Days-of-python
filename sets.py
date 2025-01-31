#Create a set with numbers 1 to 10. Remove even numbers from it.
set1 = {1,2,3,4,5,6,7,8,9,10}
size = len(set1)
for i in range(size+1):
    if(i % 2 == 0):
        set1.discard(i)
        
print("Set without even numbers: ", set1)

#Find common elements between two sets.
set1 = {1,3,5,7,9}
set2 = {1,2,3,4,5,6,7,8,9,10}

#Union between set1 and set2:
Answer = (set1.union(set2))

#Intersect two sets:
print(set2.intersection(set1))

#Create two sets of student names and find out which students are in both classes.
name1 = {"Ihsan", "Usman", "Ahmad", "Talha", "Parsa"}
name2 = {"Ihsan", "Yahya", "Talha", "Parsa", "Ehsan", "Ommar"}

#Check if one set is a subset of another set.
print(name1.issubset(name2))

#Intersection b/w these 2:
print(name1.intersection(name2))

set3 = {1,2,3,4,5,6,7,8,9,10}
print("A random element is removed: ", set3.pop())
print(set3) #set3 sae 1 removed.

ans = set() #empty set
list4 = {1,2,2,2,2,6,7,8,9,10}

for i in list4:
    ans.add(i)
    
print("The answer with no duplicates: ", ans)

set5 = {1,2,3,4,5}
set6 = {3,4,5}

#Difference b/w 2 sets:
print(set5.difference(set6))



