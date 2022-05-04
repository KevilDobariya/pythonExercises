"""
Write a program to find different aggregates (min, max, mean and median) value for existing list of numbers by using
function.
[5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]
Note: Program should not have usage of built in function to calculate respective aggregates.
"""


def minimum_value(numbers=[5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]):
    mini = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < mini:
            mini = numbers[i]
    print("Minimun value is:", mini)


def maximum_value(numbers):
    maxi = numbers[0]
    for i in range(1, len(numbers)):
        if maxi < numbers[i]:
            maxi = numbers[i]
    print("Maximum value is:", maxi)


def mean_value(numbers):
    total = 0
    for i in range(0, len(numbers)):
        total = total + numbers[i]
    avg = total/len(numbers)
    print("Mean value is:", avg)


def median_value(numbers):
    numbers.sort()
    num = int(len(numbers)/2)
    if len(numbers) % 2 == 0:
        total = numbers[num-1] + numbers[num]
        num = total/2
        print("Median is:", num)
    else:
        print("Median is: ", numbers[num])


minimum_value([5, 10, 15, 12, 500, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000])
minimum_value()
# maximum_value([5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7])
maximum_value([5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000])
mean_value([5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000])
# median_value([3, 5, 7, 12, 13, 14, 21, 23, 23, 23, 23, 29, 39, 40, 56])
# median_value([3, 5, 7, 12, 13, 14, 21, 23, 23, 23, 23, 29, 40, 56])
median_value([5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000])
