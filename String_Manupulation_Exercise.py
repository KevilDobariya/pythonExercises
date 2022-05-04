"""
1. Write a program to take string from user and find duplicate characters in string with its count.
"""

print("Enter the name:")
name = input()

for i in range(0, len(name)):
    count = 1
    for j in range(i+1, len(name)):
        if name[i] == name[j]:
            count = count + 1

    if count > 1:
        print(name[i], "is duplicate and it exists", count, "times")



"""
2. Write a program to find duplicate words and remove it from string. Output should have unique words in string.
"""

# print("Enter the name:")
# name = input()
#
# for i in range(0, len(name)):
#     count = 1
#     for j in range(i+1, len(name)):
#         if name[i] == name[j]:
#             count = count + 1
#
# result = "".join(sorted(set(name), key= name.index))
# print(result)
