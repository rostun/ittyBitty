"""
Using Python 3.4.0
"""

#python intro101.py
print("Hello")
my_int = 7
my_float = 1.23
my_bool = True
my_int = 3
print (my_int)

#function
def spam():
    eggs = 12
    return eggs    
print (spam())

#adding
count_to = 100 + 10
print (count_to)

#exponent
eggs = 10 ** 2
print (eggs)

#modulo
spam = 101%100
print (spam)

#reassigning variables
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal*tip
#display precision 2
print("%.2f" % total)

#backslash any apostrphes
'This isn\'t flying!'

#finding positions of strings
fifth_letter = "MONTY"[4]

#length, case, strings
parrot = "Blah"
print(len(parrot))
print(parrot.lower())
print(parrot.upper())
pi = 3.14
print(str(pi))

#string formatting
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." %(name, quest, color)

#datetime library
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print '%s/%s/%s' % (now.year, now.month, now.day)
print '%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)

#can directly compare to set boolean values
#not is evaluated first, and and then or 
bool_one = 3 < 5  # True
bool_one = not False and True
bool_one = 3 < 5 or 3 < 1
if len(name) and name.isalpha(): 

#pyglatin translator
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)] + first + pyg
    print new_word
else:
    print 'empty'
	
# math library
import math 
print math.sqrt(25)
# or can just do 
from math import sqrt
#import everything from the math module
from math import * # now we can just use sqrt by itself

import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

maximum = max(1, 2, 3, 4) # max function 
minimum = min(1, 2, 3, 4) # min function
absolute = abs(-3) # absolute value

print type("string")

#overall example 
def distance_from_zero(number):
    if type(number) == int or type(number) == float:
        return abs(number)
    else:
        return "Nope"
		
#lists
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
#first include second excluded
first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]# The last two items (index four and five)

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # Use index() to find "duck"
animals.insert(duck_index, "cobra")
print animals 

#for loop
my_list = [1,9,3,8,5,7]
for number in my_list:
    print 2 * number
	
#sort
start_list = [5, 3, 1, 2, 4]
square_list = []
start_list.remove(5) # remove

for number in start_list:
    square_list.append(number**2)

square_list.sort()
print square_list

#dictionaries
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number
residents['owl'] = 130
del residents['owl']
print residents['Sloth'] # can reassign as well 
print residents['Burmese Python']

#combingin everything
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

#looping throuhg dictionary
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for web in webster:
    print webster[web]
	
#two things 
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3  
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15   
}

for fruit in prices:
    print fruit
    print "price: %s" % prices[fruit]
    print "stock: %s" % stock[fruit]
	
total = 0

for key in prices:
    total += prices[key]*stock[key]

print total

#more dictionaries (classroom edition)
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]
	
def average(numbers):
    total = float(sum(numbers))
    total = total/len(numbers)
    return total

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    
    sum = .10*homework + .3*quizzes + .6*tests
    return sum

def get_letter_grade(score):
if score >= 90:
	return "A"
elif score >= 80:
	return "B"
elif score >= 70:
	return "C"
elif score >= 60:
	return "D"
else:
	return "F"
	
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
        
    return average(results)
	
print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))