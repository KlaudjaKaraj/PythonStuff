import pwinput
import sys
from pathlib import Path
from os import system

commands = sys.argv[1:]
if 'createuser' in commands :
    print('Creating the user')
    username = input('Enter your username : ')
    password = pwinput.pwinput('Enter your password : ', '*')
    with open('file.txt','a') as f:
        f.write(f'\nUsername : {username} \nPaswword : {password}')
    print('user created !')
if 'login' in commands:
    print('Login')
    username = input('Enter your username : ')
    password = pwinput.pwinput('Enter your password : ', '*')
    with open('file.txt','r') as f:
        data = f.read()
    if username in data and password in data :
        print('access granted')
    else : 
        print('you are not allowed')
if 'runserver' in commands :
    print('server is running on localhost')
    
if 'destroydatabase' in commands:
    username = input('Enter your username : ')
    password = pwinput.pwinput('Enter your password : ', '*')
    if username =='admin' and password == 'admin':
        file = 'file.txt'
        system(f'rm {file}')
    print('data was removed, what did you did !!!!')