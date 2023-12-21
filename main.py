import random
import string
import sys
import time

'''Generates passwords of a given length'''


'''Notes:

-- need to add error handling for when the requested password is not in the file'''
## slow text for command line

def slow_text(text):
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.1)

## password generation function

def generate_password(length):
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

def save_password(password):
    with open('password generator\passwords.txt', 'a') as f:
        f.write(password + '\n')

def read_password(password):
    with open('password generator\passwords.txt', 'r') as f:
        
        if password not in f.read():
            print(f'This password doesn\'t exist.')
        else:
            pass
        
        found_password = False
        for line in f:
            if found_password:
                print(f'The password for {password} is {line.strip()}')  # Print the next line
                found_password = False  # Reset the flag
            if password in line:
                found_password = True  # Set the flag if password is found

def main():
    slow_text("Welcome to the password generator\n")
    slow_text("Would you like to generate a password or read a password? (g/r)\n")
    choice = input('Enter your choice: ')
    if choice.lower() == 'g': 
        slow_text("How long do you want your password to be?\n")
        length = int(input("Enter the length of your password: "))
        password = generate_password(length)
        print(f'Your password is {password}')
        slow_text("Do you want to save this password? (y/n)\n")
        save = input()
        if save.lower() == 'y':
            password_name = input('What name would you like to save it under?: ')
            slow_text("Saving your password...\n")
            slow_text('....\n')
            save_password(f'{password_name}: \n {password} \n')
            slow_text("Your password has been saved.\n")
        else:
            slow_text("Your password has not been saved\n.")
    elif choice.lower() == 'r':
        slow_text("What password would you like to read?\n")
        password = input('Enter the name of the password: ')
        read_password(password)
        
main()
