list = [2,5,6,7,33,44,45,6,12,33,0,3,5]

list1 = []

for i in list:
    if i % 2 == 0:
        list1.append(i)
print(list1)

# A list comprehension is a concise way to create lists in Python by iterating over an existing iterable 
# and applying an expression to each element to generate a new list.

# same example but turned into list Comprehension:
list1 = [i for i in list if i % 2 == 0]

print(list1)



squares = [x**2 for x in range(1, 11)]  # Generates squares of numbers from 1 to 10

even_numbers = [x for x in range(20) if x % 2 == 0]  # Generates a list of even numbers from 0 to 19

words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = [(x, y) for x in list1 for y in list2] #Creating a List of Tuples from Two Lists:
print (combined_list)