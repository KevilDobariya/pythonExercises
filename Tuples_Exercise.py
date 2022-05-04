"""
Write a program to take string input from user and convert it into tuple.
"""

new_list = []
string = int(input("Enter a value of string you would like to enter:"))

for i in range(0, string):
    value = input("Enter the strings:")
    new_list.append(value)
# print(new_list)

new_tuple = tuple(new_list)
# print(new_tuple.count("Kevil"))
# print(new_tuple.index("Kevil"))
print(new_tuple)