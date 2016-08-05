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