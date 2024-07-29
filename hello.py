#numbers.py
# print ("hello world")
#print (5 + 5, "hey", 10.3, "hi")
#print (5 + 5, "hey", 10.3, "hi", end= " ")
# Read, Eval, Print, Loop (REPL)
#age = 5 # variable name (identifier) assigned operator (=) value that we want to assign to the variable (5)
#print (age)
# age = 6
# print (age + 10)
# age = 10/5 +3 * 3
# print (age)
# val = 10/5 + 3 * 3
# print (val)

# val = 10/5 + 3 * 3
# """"
# print (val)
# """
# print (5)


# examples of conventions
#age1 =1 # good
#age_2 = 2 #good
# age-3 = 3 #NOT good
#4age = 4 #NOT good
#Age = 6 #NOT good
#age_of_user = 7 # good
#return = 5 #NOT good

# operators
# import math
# result = 10 / 3
# new_result = math.floor(result)
# print (new_result)

# nesting
# import math
# result = 10 / 3
# print (math.floor(result))

# import math
# result = 10 // 3
# print (result)

# import math
# result = 10/ 3
# print (math.ceil(result)) operator 

# / float division
# // integer division (math.floor)
# import math
# result = 10// 3 
# print (result) 

# modulus operator remainder of an integer %

# pizza = 10
# people = 3
# print (pizza % people)

#hashmap
# number = 345345  
# limit = 10
# print (number % limit)

# raising a number to a power
# print ( 3 * 3 * 3)
# print (3 ** 3)
# print (3 ** 5)

# import math
# result = math.pow(3, 5)
# print (result)

# import math
# result = math.pow(3, 5)
# new_version= (math.floor(result))
# print (new_version)

# strings (series of characters)
# msg= "Hello World" #(string literal type value out directly)
# print (msg)

#Escape characters, single quotes vs.double quotes, slicing strings vs. indexes, strings immutable

# String escape sequences
# msg = "Hello"
# print (msg)

# msg = "Hello    Hey"
# print (msg)

# msg = "Hello    
# Hey"
# print (msg)

# msg = "Hello\nHey" \n (new line)
# print (msg)

# msg = "Hello\tHey" \t (tab)
# print (msg)

#hexidecimal to print characters ascii table 

# msg = "\x41" # (hexidecimal for letter A)
# print (msg)

# msg = "\"" # (double quote)
# print (msg)

# msg = "\\t" # (get backslash quote)
# print (msg)

# single quotes and double quotes
# msg = "Hello"
# print(msg)

# msg = 'Hello'
# print(msg)

# msg = "You're pretty" #(quotes inside quotes)
# print(msg)

# msg = 'You're pretty' #(single quotes inside single quotes ERROR:invalid syntax)
# print(msg)

# msg = 'She said "ewww"' #(double quotes inside single quotes)
# print(msg)
#single quotes inside a string use double quotes
#double quotes inside a string use single quotes

# msg = "She said \"ewww\"" #(escape character with double quote)
# print(msg)

# msg = 'She said \"ewww\"' #(escape character with single quote)
# print(msg)

# msg = 'you\'re cute' #(escape character single quote)
# print(msg)

#concatenation (combining strings into one string)
# msg = "you're cute" 
# msg2 = "hmu"
# print(msg, msg2) -passing arguments

# msg = "you're cute" 
# msg2 = "hmu"
# print(msg + msg2) no spaces

# msg = "you're cute" 
# msg2 = "hmu"
# print(msg + "..." + msg2) building expression and entire thing gets passed as a single entity

# msg = "you're cute" 
# msg2 = "hmu"
# print(msg + "..." + msg2) 
# print (msg, msg2)  # expecting 1 argument ---> concatenation

# msg = "you're cute" 
# msg2 = "hmu"
# full_message = msg + "..." + msg2
# print(full_message) 

#concatentation with string literals

# msg = "you're cute" 
# msg2 = "hmu"
# full_message = msg + "..." + msg2
# print("Hey" " " "there" "!") 

# msg= "This is a long string...."
# "continued"
# print (msg)

# msg= ("This is a long string...."
# "continued")
# print (msg)

# msg= ("This is a long string....\ncontinued")
# print (msg)

# msg = "hello"
# print(msg + " there")

#multi line strings
# poem = ("This is all combined "
# "as one happy string..."
# "what was that sound? "
# "it was a doorbell, ring."
# "When I see you, my heart sings"
# "here please take this diamond ring")
# print(poem)

# poem = """This is all combined
# as one happy string...
# what was that sound? 
# it was a doorbell, ring.
# When I see you, my heart sings
# here please take this diamond ring"""
# print(poem)

# poem = """This is all combined 
# as one happy string...
# what was that sound? 
# it was a doorbell, ring.
# When I see you, my heart sings
# here please take this diamond ring"""
# print(poem)

# poem = """This is all combined \
# as one happy string...
# what was that sound? \
# it was a doorbell, ring. \
# When I see you, my heart sings
# here please take this diamond ring"""
# print(poem)

#indexes
# poem = "Where am I?" # "W" given number 0
# print(poem)

# poem = "Where am I?" # "W" given number 0
# print(poem[0])

# poem = "Where am I?" # "h" given number 1
# print(poem[1])

# poem = "Where am I?" # "space" given number 5
# print(poem[5])

# poem = "Where am I?" # "h" given number 1
# print(poem[50])

#String slicing
# poem = "Where am I?" # "space" given number 5 which includes the space
# print(poem[5])

# poem = "Where am I?" # "space" given number 5   
# print(poem[5:]) # -(inclusive)

# poem = "Where am I?" # "space" given number 5
# print(poem[:4]) # -(exclusive)

#variations of slicing (negative indexes)

# poem = "Where am I?"
# print(poem[1])   
# 
# poem = "Where am I?"
# print(poem[-1])   # first character on right is -1
# print (0 == -0)
# print (1 == -1)

# poem = "Where am I?"
# print(poem[5])  # includes space ONLY"

# poem = "Where am I?"
# print(poem[5:])  # includes space and am I?"

# poem = "Where am I?"
# print(poem[-5:]) #starting with 5th index on the right (inclusive) ONLY "am I?" without the space

# poem = "Where am I?"
# print(poem[:7])  # includes "Where a" starting with 7th index on the left 
# #exclusive and doesn't include the "m" and stops before index 7 and excludes 7th index

# poem = "Where am I?"
# print(poem[:-7])  # includes "Wher starting with 7th index on the right and 
# #exclusive and doesn't include the "e" in "Where"

# slicing - starting point and stopping point (include ranges for substrings)
# poem = "Where am I?"
# print(poem[6:8]) #prints "am" selects index 6 and stops after index 7 on the left

# poem = "Where am I?"
# print(poem[6:-3])# prints "am" starts on left up to index 6 and counts to index 3 from the
# #with same answer as "am"

# poem = "Where am I?"
# start = 6
# print (poem[start:start+2]) prints "am"

# name = "Caleb Curry"
# start_of_last = 6
# print (name[start_of_last:start_of_last+3]) # prints "Cur"

#-----------------------------
#  P | y |  t |  h |  o |  n |
#-----------------------------
# 0  1   2    3    4    5    6
# -6 -5 -4   -3   -2   -1

# function (id) (stored in computers ram) strings are immutable
# task = "Subscribe"
# print(id(task))

# task = "like"
# print(id(task))
#------------------------
# task = "Subscribe"
# print(id(task))

# task = task[0]
# print(id(task))

#--------------------

# task = "Subscribe"
# print(id(task))

# task[0] = "s" #   ERROR : 'str' object does not support item assignment
# print(id(task))

#Immutability
# task = "Subscribe"
# print(id(task))
# task = task + "!"
# print(id(task))

# task = "Subscribe"
# print(id(task))
# different = task
# different = "hey"
# print(task)

# task = ["Subscribe"]
# different = task
# different[0] = "hey"
# print(task)

# get length of string (len) function
# msg = "please subscribe"
# print (msg[6])
#get length of string (len) function
# msg = "please subscribe"
# print(len(msg)) # length is index +1

# msg = "please subscribe"
# print(msg[15]) # index is always length -1

# msg = "please subscribe"
# print (msg[len(msg)-1]) # length of message 16-1 = index of 15

#convert a number to a string
# msg = "please subscribe"
# print (len(msg))

# msg = "please subscribe"
# print (len(msg))

# msg = "please subscribe"
# print("Your message was" + len(msg) +" characters long") # TypeError: can only concatenate str (not "int") to str

# msg = "please subscribe"
# print("Your message was " + str(len(msg)) +" characters long")

# msg = "please subscribe"
# print("Your message was",len(msg),"characters long") # separate with commas no need for spaces
#or conversion of len function to string (separate arguments)

#Nested function calls
# import math
# age = 15
# age_str = str(age)
# id_age_str = id(age_str)
# other = math.floor(2.6)
# added = id_age_str + other
# added_str = str(added)
# length = len(added_str)
# print(length)
# print(len(str(id(str(age)) + math.floor(2.6))))

#-------------------LISTS--------------------------------#
# ages = [12, 18, 28]
# people = ["Caleb", "Sabrina", "emily"]
# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# print (my_favorite_things)

#mutablity of lists changing them without creating new ones.
# ages = [12, 18, 28]
# people = ["Caleb", "Sabrina", "emily"]
# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# print(id(my_favorite_things))
# my_favorite_things[0] = "Walking"
# print(id(my_favorite_things))
# print (my_favorite_things)


# ages = [12, 18, 28]
# people = ["Caleb", "Sabrina", "emily"]
# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# my_favorite_things[0] = "Walking"
# print (my_favorite_things)

# ages = [12, 18, 28]
# people = ["Caleb", "Sabrina", "emily"]
# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# print(id(my_favorite_things))
# my_favorite_things[0] = "Walking"
# print(id(my_favorite_things)) # confirms that no new data is created in memory but, number stays the same points to the same object
# print (my_favorite_things) 

#get length of the list
# ages = [12, 18, 28]
# people = ["Caleb", "Sabrina", "emily"]
# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# print(id(my_favorite_things))
# my_favorite_things[0] = "Walking"
# print (my_favorite_things)
# print(len(my_favorite_things)) # length is 3 because length of the list is 3 elements, amazon prime and netflix combined into 1 element

# Copy a list
# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# print(my_favorite_things[1:2]) # returns the 2nd element [7] in the list

# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# print(my_favorite_things[:]) # creates a copy of the list

# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# copy = my_favorite_things[:] # creates a copy of the list by assigning it to a variable
# print (copy)

# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# copy = my_favorite_things[:]
# print(copy)
# copy[0] = "walking" 
# print(my_favorite_things, copy)

# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# copy = my_favorite_things # alias is creating same object in memory and updates both lists
# copy[0] = "walking" # this will update both lists to include "walking" which is not desired, since only want to update 1 of the lists to include "walking"
# print(my_favorite_things, copy) 

# my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
# copy = my_favorite_things.copy() # function attached to object with "."" operator another way to create 2 separate lists updated with 1 having "walking"
# copy[0] = "walking" 
# print(my_favorite_things, copy)
