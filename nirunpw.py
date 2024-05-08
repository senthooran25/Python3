import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to password gen")
NR_letters = int(input('how many letters you want in your pass? '))
NR_numbers = int(input('how many numbers you want in your pass? '))
NR_symbols = int(input('how many symbols you want in your pass? '))
length=NR_letters+NR_numbers+NR_symbols

password=[]

for i in range(NR_letters):
    letter = random.choice(letters)
    password.append(letter)
   # print(password)

for i in range(NR_numbers):
    number = random.choice(numbers)
    password.append(number)
   # print(password)
#
for i in range(NR_symbols):
    symbol=random.choice(symbols)
    password.append(symbol)


# password = (random.choice(password) for i in range(len(password) +1))
# password = ''.join(password)

# for i in range(password):
#  password=random.choice(letter+number+symbol)
# password = ''.join(random.choice(password) for i in range(length))
random.shuffle(password)
password = ''.join(password)

print(password)

# import random
# import string
#
# def generate_password(length=12):
#     all_characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(all_characters) for i in range(length))
#     return password
#
# # Example usage: generate a password with length 16
# password = generate_password(16)
# print(password)
# passwordgen.py
# Displaying passwordgen.py.