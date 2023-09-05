''' Notes:

options to select: 
- alphanumeric
- symbols
- capitals

password storage system
"would you like to assign a software to this?"

error handling

true randomisation?

'''

import time
import random as random
import string

# define slow text function
def slow_text(text): 
    # splitting the string into individual letters i.e.['h', 'i']
    lst = list(text)
    
    num = 0
    # loop through created list
    for i in range(0, len(lst)):
        print(text[num], end='')
        num += 1
        time.sleep(0)
        
    

choice = input('''Welcome to the password generator!
Please choose whether you would like to generate a new password or view an existing one.

| Generate new password | View an existing one | \n''')

if choice.lower() == 'generate new password' or choice.lower() == 'generate new':
    length = int(input('How long would you like your password to be? Enter an integer. \n'))
    file = open('Password Generator\passwords.txt', 'a+')
    # password = ''
    # for i in range(0, length):
        # password += str(random.randint(0, 9))

    password = ''.join(random.choices(string.ascii_lowercase, k=length))
    
    slow_text(f'Your password is: {password} \n')
    name_choice = input('Would you like to assign a name to your password? Y | N \n')
    
    if name_choice.lower() =='y':
        name = input('Choose a name \n')
        
        L = [f'{name}: \n', f'{password} \n \n']
        file.writelines(L)
        file.close()
    elif name_choice.lower() == 'n':
        file.write(f'{password} \n')
        file.close()
    slow_text('..... \n')
    slow_text('Password saved!')
    
    
elif choice.lower() == 'view an existing one' or choice.lower() == 'view':
    file = open('Password Generator\passwords.txt', 'r+')
    
    password_choice = input('What password would you like to view? \n')
    
    for line in file:
        if password_choice.lower() in line.lower():
            print(f'The password for {password_choice} is {file.readline()}')
            break
        elif password_choice.lower() not in line.lower():
            print('invalid choice')
            break
