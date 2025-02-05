import random
numbers = ["1","2","3","4","5","6","7","8","9","10"]
symbols = ["!","@","#","$","%","^","&","*","(",")"]

capital = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
capital_alphabets = capital.split(" ")

small = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
small_alphabets = small.split(" ")
password = " "

for i in range(3):
    alphabets_size = len(capital_alphabets)
    choice = random.randint(0,alphabets_size-1)

    numbers_size = len(numbers)
    num_choice = random.randint(0,numbers_size-1)

    sym_size = len(symbols)
    sym_choice = random.randint(0,sym_size-1)

    num = numbers[num_choice]
    sym = symbols[sym_choice]

    l_alphabets = capital_alphabets[choice]
    s_alphabets = small_alphabets[choice]

    password = password + (l_alphabets + s_alphabets + num + sym)

print("The password is: ", password)
print("length of digits: ", len(password))