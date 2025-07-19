print("hello bb")
print(2/3.0)
name = "Eho"
type(name)
print(name)
dead, parrot = 'hey', 'there'
print(dead+'  '+parrot)
def function_name(arg, arg2):
    print (arg  + arg2)
function_name(9, 8)
numbers = [1, 3.24, 2.74, 1.59]
expect = ['spanish', 'inquisitive', 'mayor']
mixed = [10, 8.0, 'spam', 'eggs', 0]
print(numbers[1:3])
print(mixed[0:3])
print(expect[1])
expect[0] = 'nobody'
print(expect)
numbers.append(111111)
print(numbers)
check = numbers + mixed
print(check)
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)
sentence = 'list comprehension is useful'
words = [[word.upper(), word.lower(), \
len(word)] for word in sentence.split()]
print(words)
dictio = {"eggs" :1, "sausage" : 2, "bacon" : 3, "spam" : 4, "spaam" : 5, "babcon" : 6}
print(dictio)
dictio['spaam'] = 'urggh'
print(dictio['spaam'])
print(dictio.keys())
print(dictio.values())
print(dictio.items())
del dictio['spaam']
print(dictio)

#  if/else

age = 40
if (age > 50):
  print("A wise man")
else :
    print("such a youngstre")

    # while loop

    countdown = 50
    while countdown >=0:
        print(countdown)
        countdown -= 5

        # for loop

        countdown_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for x in countdown_list:
            print(x)

            for x in range(25, -5, -5):
              print(x)

            #   try except
try:
    for x in range(3, -1, -1):
      print("the reciprocal of {0} is {1}".format(x, 1.0/x))

except ZeroDivisionError:
    print("Divide by zero?...Nah you can't do that... Sorry!")

# functions

def rec_area(a, b = 1.0):
 #   "Calculating the area of a rectangle"
      return a*b
print(rec_area(2, 22))

def factorial(n):
    f = 1
    if n <= 1:
        return f
    else:
        while(n >=1):
            f *= n
            n -= 1
        return f
print(factorial(-5))
print(factorial(5))

# lambda function

x = [2, 3, 6]
g = lambda n: n**3
[g(item) for item in x]

# printing sqr of a list of numbers from 0-n
def main():
    n = input("Give me a possible number ")
    x = range(int(n)+1)
    y = [item**2 for item in x]

    print(y)
main()

# math module

import math

def area_circ(r):
    return math.pi * r**2
r = 3
Area = area_circ(r)
print("The area of a circle with "\
"radius {0} is {1}".format(r, Area))
from math import pi #another way to import only pi
r = 4
m = math.pi* r**2
print("the area {0} is {1}".format(r, m)) 

# matrix manipulation and linear algebra

a = [1, 2, 3, 4, 5]
b = [20, 30, 40, 50, 60]
print(a + b)#instead of addition, it results to concatenation

# numpy package (numerical python)

import numpy as np
A = np.array([1, 2, 3, 4, 5])
B = np.array([20, 30, 40, 50, 60])
c = A + B
print(c)
print("Multiplied by 2", a*2)

# matrices

m1 = np.matrix([[2, 3], [-1, 5]])

m2 = np.matrix([[1, 2], [-10, 5.4]])
print(m1*m2)

# m3 = np.matrix([1,2], [2, 3], [4, 5]) gives an error bc
# print(m3.T) matrices only support 2D not more nor less use arrays instead

print(m2.transpose())
print(m1.T)
print("what is it's shape", m1.shape)

# scipy library (more advanced than numpy)(scientific python)

from numpy import array, dot
from scipy import linalg

x = array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = array([[1], [2], [3], [4]])

n = linalg.inv(dot(x.T, x))
k = dot(x.T, y)

coef = dot(n, k)
print(coef)

# indexing and slicing

s = np.arange(12)
print(s[1:3])
print(s[0:9:3])

b = np.array([np.arange(4), 2 * np.arange(4)])
print(b.shape)
print(b)
p = np.arange(1, 6, 2)
print(p)
print(b[:2, :2])
print(b[:1, :])# :1 prints the 0th row excluding 1, : all columns

import numpy as np
import pandas as pd

array1 = np.array([14.1, 15.2, 16.3])
series1 = pd.Series(array1)
print(series1)

features = {'limbs':[0, 4, 4, 4, 8], 'herbivores':['No', 'No', 'Yes', 'Yes', 'No']}

animals = ['Python', 'Iberian Lynx', 'Giant Panda', 'Field Mouse', 'Octopus']

df = pd.DataFrame(features, index= animals)
print(df)
print(df.head(3))
f = df['limbs'][2:5]
print(f)
# print(df.loc['python'])

print(df['limbs'].describe())
print(df['herbivores'].describe())