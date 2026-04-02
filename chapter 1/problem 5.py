# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

# dictionary = {
#     "banana": "kela",
#     "mango": "aam",
#     "where": "kaha",
#     "mobile": "phone",
#     "voice": "aawaz",
#     "buisness": "karobaar"
# }
# print(dictionary)
# print(type(dictionary))

# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

# store = set()
# store.add(int(input("enter number")))
# store.add(int(input("enter number")))
# store.add(int(input("enter number")))
# store.add(int(input("enter number")))
# store.add(int(input("enter number")))
# store.add(int(input("enter number")))
# store.add(int(input("enter number")))
# store.add(int(input("enter number")))

# print(store, '\n', type(store))

# Can we have a set with 18 (int) and '18' (str) as a value in it?

# store2 = {18, '18'}
# print(store2, '\n\n' , type(store2)) # yes, definately

# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# print(len(s))   # 2 is length


# s = {}
# # What is the type of 's'?
# # this is dictionary
# print(type(s))


# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

# empty = {

# }

# empty.update({
# input("enter you name\t\t") : input("enter your favourite language\t\t"),
# input("enter you name\t\t") : input("enter your favourite language\t\t"),
# input("enter you name\t\t") : input("enter your favourite language\t\t"),
# input("enter you name\t\t") : input("enter your favourite language\t\t"),

# })

# print(empty, type(empty))

# If the names of 2 friends are same; what will happen to the program in problem
# 6?

# answer - it overwrite value to the last latest one

# If languages of two friends are same; what will happen to the program in problem
# 6?

# answer - nothing happens, because value can be same


# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

# answer - no we can not change the value inside a set