def Max(a,b):
    if a > b:
        return a
    if b > a:
        return b
    
    
def Even_Odd(num):
    if(num % 2 == 0):
        return "Even"
    
    return "Odd"
    
    
def factorial(num):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial*i
        
    return factorial


def check_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    counts = [0]*5
    # Convert the input string to lowercase
    for char in string.lower():
        if char in vowels:
            index = vowels.index(char)
            counts[index] += 1

#Task 1: Write a Function to Find the Maximum of Two Numbers:
a = int(input("Enter a:"))
b = int(input("Enter b:"))

    if(a > b):
    Max_Num = Max(a,b)
    print("A is greater.")
    if(a < b):
    Max_Num = Max(a,b)
    print("B is greater.")
    
#Task 2: Check if a Number is Even or Odd
x = int(input("Enter a number:"))
answer = Even_Odd(x)
print ("Number is:", answer)

#Task3: Calculate the Factorial of a Number:
y = int(input("Enter a number: "))
Factorial = factorial(y)
print("Factorial is: ", Factorial)

#Task4: Count Vowels in a String
#string = input("Enter a word:")
#Count =  check_vowels(string)

#Vowels= ["a","e","i","o","u"]
#Combine = dict(zip(Vowels,Count))

#for key,value in Combine.items():
 #   print(f"Vowel: {key}, Count: {value}")

#Task5: Reverse a String Using a Function
string = "bob"
rev_string = string[::-1]
    
if(string == rev_string):
    print("Palindrome")
else:
    print("Not Palindrome")

def Sum(nums): #(*nums):
    Sum = 0
    for i in nums:
        Sum = Sum + i
        
    return Sum


def Max_inList (nums):
    Max = nums[0]
    for i in nums:
        if(Max < i):
            Max = i
            
    return Max
    
    
list1 = [1,2,3,4,5] 
Answer = Sum(list1) # Sum(1,2,3,4,5)
print("Answer: ", Answer)

#Find the Largest Number in a List:
list2 = [10,20,30,40,50]
Max = Max_inList(list2)
print ("Max number is: ", Max)

