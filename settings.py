import string
import random

password_gen_type = 'alphanumeric'

def numeric(length):
    # password characters
    numbers = string.digits
    all = numbers
    # use random
    temp = random.sample(all,length)
    # create the password
    password = "".join(temp)
    # print the password
    return password

def alphanumeric(length):
    # password characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    all = lower + upper + numbers + symbols
    # use random
    temp = random.sample(all,length)
    # create the password
    password = "".join(temp)
    # print the password
    return password

def string_replacement(password):
    letters = {'e': '3', 'a': '4', 'o': '0', 'i': '1', 's': '5', 't': '7'}
    numbers = string.digits
    symbols = string.punctuation
    # iterate through string, replace letters where they match the keys
    for i in password:
        if i in letters.keys():
            password = password.replace(i, letters[i])
    
    for i in range(random.randint(1, 4), random.randint(4, 6)):
        ending = random.randint(1, 4)
        
        if ending <= 2:
            password += random.choice(symbols)
        elif ending >= 3:
            password += random.choice(numbers)
    
    return password
            
