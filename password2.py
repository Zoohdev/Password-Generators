# Imports
import random # Will be needed to randomly generate the password
import string # Helpful for shortening our code

# Assigning variables to a string with all letters/numbers/special
letters = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation

# User input
letter_num = int(input('How many letters would you like in your password? '))
number_num = int(input('How many numbers would you like in your password? '))
special_num = int(input('How many special characters would you like in your password? '))

# Generating the password
password = ''
for i in range(letter_num):
    password += random.choice(letters)
for i in range(number_num):
    password += random.choice(numbers)
for i in range(special_num):
    password += random.choice(special_chars)

# Mixes the string
password = ''.join(random.sample(password, len(password)))

# Printing out the final password
print('Password: ' + password)
