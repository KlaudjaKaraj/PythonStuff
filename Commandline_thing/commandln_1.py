# python3 -V : version
# python3 -v : verbose
# python3 -h : help

import sys

print("hello world")
arguments = sys.argv[1:]
print(type(arguments))
# the first element is the file name


def help():
    print("this is a description to the code")


print("our code keeps working")


def create_file():
    with open("file.txt", "w") as f:
        data = f.write("welcome")


def create_table(table_name):
    print(f"the table {table_name} was created")


if "help" in arguments or "h" in arguments:
    help()
if "makefile" in arguments or "mfl" in arguments:
    create_file()
if "createtable" in arguments:
    create_table("some cool table")

num_list = []
str_list = []
sum = 0
for item in sys.argv[1:]:
    if item.isdecimal():
        num_list.append(item)
        sum += int(item)
    else:
        str_list.append(item)

print(num_list)
print(sum)
print(str_list)