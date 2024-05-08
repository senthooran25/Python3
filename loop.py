# list_fruit =['apple', 'pear', 'grape', "kiwi"]
# for fruit in list_fruit:
#     print(fruit)


# two_digit_number = input()
# two_digit_string = str(two_digit_number)
# first_num = int(two_digit_string[0])
# secound_num = int(two_digit_string[1])
# total = first_num + secound_num
# print(total)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
for i in range(nr_letters+1):
    letter = random.choice(letters)
    password.append(letter)

for n in range(nr_numbers+1):
    num = random.choice(letters)
    password.append(num)
for s in range(nr_symbols+1):
    sym = random.choice(letters)
    password.append(sym)
random.shuffle(password)
password = ''.join(password)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P