'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

#There are 3 parts to list comprehension:

#*result*  = [*transform/expression*    *iteration*         *filter*     ]

#The filter part answers the question if the item should be transformed.



## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

newlist = [int(x) for x in numbers if x > 0]
print(newlist)




## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()

# Length = [len(x) for x in words if x != 'the']
# print(Length)

word_lengths = [len(word) for word in sentence.split(' ') if word != "the"]
print(word_lengths)



## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

list = [key.upper() for key in dict if dict[key] < 5000]
print(list)


## Find all the numbers from 1 to 1000 that have a 4 in them
new_range = [i for i in range(1000) if '4' in str(i)]
print(new_range)


## count how many times the word 'the' appears in the text file - 'sometext.txt'
infile = open('sometext.txt', 'r')
result = [i.count('the') for i in infile]
print(sum(result))

# result = len([x for x in infile.split(' ') if x in ['the','The']])
# print(result)


## Extract the numbers from the following phrase ##

phrase = "In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each event, with about 3 or 4 that were classifled as serious per event."

numbers = [int(x) for x in phrase.split() if x.isdigit()]
print(numbers)






