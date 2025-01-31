# Create a dictionary
mydict = {"a": 1, "b": 2, "c": 3, "d": 4}
new = { "e":5 }
mydict.update(new)
print(mydict)

#access an element from the dictionary:
ans = mydict.get("a") #stores the value of a 
print(ans)

ans = mydict.get("c") #store value of c
print(ans) 

ans = mydict.get("e") #store the value of e
print(ans)

#Check If a Key Exists:
if("a" in mydict.keys()): #checks if a is a key or not
    print("Key is present, value is: ", mydict.get("a"))
else:
    print("Key is not present.")
    
for key,value in mydict.items(): #you have to specify.
    print(f"Key {key}, Value {value}")
    

#Count Word Frequency in a String
sentence = "apple orange apple banana orange mango"
list1 = sentence.split(" ") #split when you find a whitespace
countList = []
NoDuplicates = set(list1) #duplicates removed.

for i in NoDuplicates:
    count = list1.count(i)
    countList.append(count)
    
#create a Dictinory:
key = list1
value = countList
myDict = dict(zip(key,value)) #pairs created.

#print the count of each word
for key,value in myDict.items():
    print(f"Key {key}, Value {value} ")
    
#From 2 lists to Dictinory:
names  = ["Ihsan", "Lala", "Usman", "Saboor", "Nosheen"]
age = [19 , 23 , 21 , 53 , 51]

NewDict = dict(zip(names,age))

for key,value in NewDict.items():
    print(f"Key {key} , Value {value} ")
    
#Merge two Dictionries:
Dict1 = {"a":1 , "b":2, "c":3, "d":4}
Dict2 = {"e":5 , "f":6, "g":7, "h":8}
Dict3 = {}

Dict3.update(Dict1)
Dict3.update(Dict2)
    
for key,value in Dict3.items():
    print(f"Keys {key} , value {value} ")
    
