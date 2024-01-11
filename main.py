import random
import string
import sys
import time
import settings

'''Generates passwords of a given length'''


'''Notes:

-- need to add error handling for when the requested password is not in the file
-- also need to add error handling for if the name is already in the file'''
## slow text for command line

def slow_text(text):
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.1)

## password generation function

def generate_password(length):
    # password characters
    if settings.password_gen_type == 'alphanumeric':
        return settings.alphanumeric(length)
    elif settings.password_gen_type == 'numeric':
        return settings.numeric(length)
    else:
        slow_text('It looks like your settings file is empty. Please set it to either "Numeric" or "Alphanumeric". \n')

def save_password(password_name, password):
    with open('password generator\passwords.txt', 'a+') as f:
        # check if the password is already in the file
        if password in f.read():
            return slow_text("This password already exists. Please enter a different name.\n")
        else:
            f.write(f'{password_name}: \n {password} \n \n')
            return slow_text("Your password has been saved.\n")

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
    slow_text("Welcome to the password generator.\n")
    slow_text("Would you like to generate a password, convert text into a password or read a password? (g/c/r)\n")
    choice = input('Enter your choice: ')
    if choice.lower() == 'g': 
        slow_text("How long do you want your password to be? The recommended length is atleast 8 characters.\n")
        length = int(input("Enter the length of your password: "))
        password = generate_password(length)
        print(f'Your password is {password}')
        slow_text("Do you want to save this password? (y/n)\n")
        save = input()
        if save.lower() == 'y':
            password_name = input('What name would you like to save it under?: ')
            slow_text("Saving your password...\n")
            slow_text('....\n')
            save_password(password_name, password)
        else:
            slow_text("Your password has not been saved.\n")
    elif choice.lower() == 'r':
        slow_text("What password would you like to read?\n")
        password = input('Enter the name of the password: ')
        read_password(password)
    elif choice.lower() == 'c':
        slow_text("What text would you like to convert into a password?\n")
        text = input('Enter your text here: ')
        password = settings.string_replacement(text)
        print(f'Your password is {password}')
        slow_text("Do you want to save this password? (y/n)\n")
        save = input()
        if save.lower() == 'y':
            password_name = input('What name would you like to save it under?: ')
            slow_text("Saving your password...\n")
            slow_text('....\n')
            save_password(password_name, password)
        else:
            slow_text("Your password has not been saved.\n")
            
        
main()
