try :
    a = int(input('give a first number '))
    b = int(input('give another number '))
    #a= 1
    #b=0
    c = a/b
    print(c)
except ZeroDivisionError:
    print('You cant divide by zero !!')
    
except ValueError:
    print('inputs must be numeric')
     
print('it works')

list_of_items = ['a',3.14,1,2]
try:
    print(list_of_items[1])
    print(list_of_items[5])
    print(list_of_items[2])
except IndexError: #or LookUpError
    print('Index must be less than the list length')
    
my_dict = {'a' : 1 , 'b' : 2 , 'c' : 3}

try :
    print(my_dict['a'])
    print(my_dict['d'])
except KeyError:
    print('we dont have that key yet please update it')
    
try :
    with open('my_text.txt','r') as f :
        data = f.read()
        print(data)

except FileNotFoundError:
    print('we tried but we didnt find it ')
    
try : 
    a = 'hello '
    b ='python'
    c = a + b
except TypeError:
    print('you cant add a string to an integer')
else :
    # execute this code if no exception was raised
    print(c)
    
class Person:
    def eat(self):
        pass
    
person1=Person()
try :
    person1.sleep()
except AttributeError:
    print('person cant sleep')
else: 
    print('person is eating now')
    
    
my_dict_1 = {'a' : 1 , 'b' : 2 , 'c' : 3}

try :
    print(my_dict_1['a'])
    print(my_dict_1['d'])
except IndexError: #or LookUpError
    print('we dont have that key yet please update it')    
finally :
# code that is always executed, whether an exception is raised or not
    my_dict_1['e'] = 4
    print(my_dict_1)