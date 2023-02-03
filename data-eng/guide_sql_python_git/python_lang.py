age = 36
state = "relaxed"
txt = "My name is John, and I am {} and i like to be very {}"
# print(txt.format(age, state))

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")

# thislist.append("orange")
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)

# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)

# print(thistuple)
# print(thislist)


# # RESULT
# ['apple', 'banana', 'watermelon', 'cherry', 'orange', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange']


# thislist.remove("banana")

# LIST COMPREHENSSION

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# INSTEAD WE CAN DO

# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# # OUTPUT
# ['apple', 'banana', 'mango']
# ['apple', 'banana', 'mango']


# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.filter(key = myfunc)
# print(thislist)

# UPPERCASE AND LOWERCASE SORTING CAN BE A PROBLEM
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# # print(thislist)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# Print all key names in the dictionary, one by one:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# # Print all key names in the dictionary, one by one:
# for x in thisdict:
#   print(x)
# # Print all values in the dictionary, one by one:
# for x in thisdict:
#   print(thisdict[x])
# # You can also use the values() method to return values of a dictionary:
# for x in thisdict.values():
#   print(x)
# # You can use the keys() method to return the keys of a dictionary:
# for x in thisdict.keys():
#   print(x)
# # Loop through both keys and values, by using the items() method:
# for x in thisdict.items():
#   print(x)
# # make a copy
# mydict = thisdict.copy()
# print(mydict)
# # Make a copy of a dictionary with the dict() function:
# mydict = dict(thisdict)


# while loop
# i = 0
# while i < 6:
#   print(i)
#   i += 1
#   if i == 5:
#     break
#   if i == 3:
#     continue

# for loop
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# for x in range(0, 10, 3):
#   print(x)


# recursion
# https://www.youtube.com/watch?v=RXGyeWy1Mvw

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


# def substract_to_zero(n):
#     n -= 1
#     if n > 0:
#         substract_to_zero(n)
#         print(n)
#     else:
#         print("done")
#     # print(f"run order {n}")

# substract_to_zero(5)


# def show_list(list):
#     if len(list) != 0:
#        print(list)
#        show_list(list[1:])

# show_list([1,2,3,4])

# output
# [4]
# [3, 4]
# [2, 3, 4]
# [1, 2, 3, 4]

# def show_list2(list, i=0):
#     if i < len(list):
#        show_list2(list, i+1)
#        print(list[i:])

# show_list2([1,2,3,4])

# output
# [4]
# [3, 4]
# [2, 3, 4]
# [1, 2, 3, 4]

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# Or, use the same function definition to make TWO functions a DOUBLER & TRIPLER, in the same program:
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))


class Person:
    # All classes have a function called __init__(),
    # which is always executed when the class is being initiated.

    # Use the __init__() function to assign values to object properties, or other
    # operations that are necessary to do when the object is being created:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# The string representation of an object WITH the __str__() function:

    def __str__(self):
        return f"{self.name}({self.age})"
# Objects can also contain methods. Methods in objects are functions that belong to the object.
    def myfunc(self):
        print(f"Hello my name is {self.name} and i'm {self.age}")

p1 = Person("John", 36)

# print(p1)
# p1.myfunc()

# delete properties
del p1.age
# delete objects
del p1
# declare an empty class
class some:
    pass






# import json


# # Convert from JSON to Python:
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])

# # Convert from Python to JSON:
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)


# try:
#   print(x)
# except:
#   print("An exception occurred")
  
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")


# username = input("Enter username:")
# print("Username is: " + username)


import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
