"""
1.	Write a program to differentiate even numbers and odd numbers from existing list.
Then Print even number and odd numbers.
"""

a = [1, 3, 4, 5, 6, 2, 10, 12, 55, 66, 99, 111, 180]
even = []
odd = []

for n in a:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Number is even number", even)
print("Number is odd number", odd)

print("-----------------------------Exercise 1 Ends--------------------------------------")

"""
2.	Write a program to do product of specific value(N) given by user in list of string.
Input: ['abcd', '11', 'ff', 'pp', '50', '13', '19', 'hh']
"""

list_value = ['abcd', '11', 'ff', 'pp', '50', '13', '19', 'hh']

print("Please enter N value to do product with list of values:")
value = int(input())
new_list = []

for v in list_value:
    if v.isnumeric():
        # x = int(v) * value
        new_list.append(int(v) * value)
    else:
        new_list.append(v)

print(new_list)

print("-----------------------------Exercise 2 Ends--------------------------------------")


"""
3.	Write a program to sort numbers in descending order from existing list.
 Input:  [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]
 Output:  [2020, 1010, 554, 121, 80, 26, 23, 22, 15, 12, 11, 4, 3]
"""

# Using built in function

number = [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]

# number.sort(reverse=True)
# print(number)

# Without built in function

desc = []

while number:
    maximum = number[0]
    for x in number:
        if x > maximum:
            maximum = x
    desc.append(maximum)
    number.remove(maximum)
print(desc)

print("-----------------------------Exercise 3 Ends--------------------------------------")

