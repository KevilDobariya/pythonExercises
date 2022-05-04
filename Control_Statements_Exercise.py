"""
Write a program to triples each integer present in list which is even.
Use Continue statement. [55, 22, 77, 44, 58, 90, 30, 72]
"""

numbers = [55, 22, 77, 44, 58, 90, 30, 72]
print(type(numbers))

for n in numbers:
    if n % 2 == 0:
        print(n, " is even number")
        n **= 3
        print("Value of even numbers after triples is:", n)
        continue
