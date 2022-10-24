list1 = [10,20,30,40,50]
list2 = []

# without list comprehension
for x in list1:
    if x > 20:
        x += 100
        list2.append(x)
print(list2)


# with list comprehension
list2 = [x + 100 for x in list1 if x > 20]
print(list2)


# List of numbers to 0 to 9
x = [i for i in range(10)]
print(x)


# FInd the dquare of each numbeer from 0-9
x = [i**2 for i in range(10)]
print(x)


# Multiply each element in a list by 3.
list1 = [3,4,5]
multiplied = [item*3 for item in list1]
print(multiplied)


# Grab the first letter of each word.
listOfWords = ['this', 'is', 'a', 'list', 'of','words']

items = [i[0] for i in listOfWords]
print(items)

# Apply lowercase/uppercase to all letters in list
result = [x.lower() for x in ['A','B','C']]
print(result)
result2 = [x.upper() for x in result]
print(result2)


# Add an if condition

# Find the square of all even numbers from 0 to 4
new_range = [i*i for i in range(5) if i % 2 == 0]
print(new_range)


# Extract the numbeers from the phrase below
string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print(numbers)
letters = [x for x in string if x.isalpha()]
print(letters)



# Find 'line3 in the file test.txt
infile = open('test.txt', 'r')
result = [i.strip('\n') for i in infile if 'line3' in i]
print(result)



# Using a function.
def double(x):
    return x*2

print(double(10))

mylist = [double(x) for x in range(10) if x%2 == 0]
print(mylist)



# 2 arguments in same list
result = [x+y for x in [10,20,30] for y in [20,40,60]]
print(result)