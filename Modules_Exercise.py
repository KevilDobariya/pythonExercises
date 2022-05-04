"""
Write a program to take directory name as input and print files name which are present inside directory.
Note: Program should able to locate and print the files of Child directories as well.
"""


directory_name = input("Enter the directory name you would like to get locate and print the files:")
x = dir(directory_name)
print(x)