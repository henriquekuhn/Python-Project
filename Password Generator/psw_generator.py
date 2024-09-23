#Generate random password
import random
import string

password = []

num_letters = int(input(f"How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like in your password?\n"))
num_numbers = int(input(f"How many numbers would you like in your password?\n"))

random_letter = []
for letter in range(num_letters):
    random_letter.append(random.choice(string.ascii_letters))

random_symbols = []
symbol_range = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))
for symbols in range(num_symbols):
    random_symbols.append(chr(random.choice(symbol_range)))


random_number = []
for number in range(num_numbers):
    random_number.append(str(random.randint(0,9)))

print(random_letter)
print(random_symbols)
print(random_number)

password = random_letter + random_symbols + random_number
print(password)
random.shuffle(password)
print(password)

password_char = ""
for char in password:
    password_char += char

print(password_char)

