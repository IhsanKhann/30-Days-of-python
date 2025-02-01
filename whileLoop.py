import random

factorial = 1
x = int(input("Enter a Number: "))
i = 1

while i <= x:
    factorial = factorial * i
    i = i+1
    
print("Factorial is: ", factorial)

num = int(input("Enter the num you want table for: "))
times = int(input(f"How many times do you want {num} table for: "))
i = 1
while (i<= times):
    print(f"{num} x {i} = {num*i}")
    i += 1
    
#prime checker:
ans = int(input("Enter a number: "))
isnotPrime = False
i = 2

while(ans > i):
    if(ans % i == 0):
        isnotPrime = True
    i += 1
    
if(isnotPrime and ans >1 ):
    print("Number is not Prime")
else:
    print("Number is Prime")
    
    
#Palindrome Checker:
num = int(input("Number :"))
reversed_num = 0

while(num > 0):
    remaindar = num % 10
    reversed_num = reversed_num * 10 + remaindar
    num = num // 10
    
if(reversed_num != num):
    print("Number is Palindrome.")
else:
    print("Number is not Palindrome.")
    
#10. Guess the Number Game
#Write a simple guess the number game where the user has to guess a number between 1 and 100. The program should give feedback if the guess is too low or too high, and end when the user guesses the correct number.

ans = random.randint(0,101) 
print (ans)
yourChoice =  int(input("Enter a number between 1-100: "))
while(True):
    if(yourChoice == ans):
        print("Correct Guess.")
        break
    else:
        if(ans != yourChoice and ans > yourChoice):
            print("Choice too low.")
            break
        elif(ans != yourChoice and ans < yourChoice):
            print("Choice too high.")
            break


