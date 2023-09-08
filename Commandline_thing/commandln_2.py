# calculator command 

import sys
print(sys.argv[1:])
n = int(sys.argv[1])
op = str(sys.argv[2])
m = int(sys.argv[3])

if op =='+' :
    print("the result is ", n + m)
elif op =='-' :
    print("the result is ", n - m)
elif op =='x' :
    print("the result is ", n * m)
elif op =='/' :
    try :
        print("the result is ", n / m)
    except ZeroDivisionError:
        print('you cannot divide by zero')
else :
    print('please enter a valid input')