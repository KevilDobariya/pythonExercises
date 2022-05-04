"""
Write a program to do Sum of N series. N value should be entered by user.
Input: Please enter number to get sum of N Series Output: 5 Sum of 1 to 5: 15
"""

print("Please enter number to get sum of N series")
num = int(input())
total = 0
n = 1

# Using While Loop
# while n <= num:
#     total = total + n
#     n = n+1

# Using For Loop
for n in range(num+1):
    total = total + n
    n = n+1

print("Sum of num is", total)