"""
Write a program to differentiate number from existing list based on its digit.
  Input:
  [2, 3, 44, 55, 33, 111, 1010, 1, 4, 66, 8080, 121, 2020]
"""

list_1 = [2, 3, 44, 55, 33, 111, 1010, 1, 4, 66, 8080, 121, 2020]
digit1 = []
digit2 = []
digit3 = []
digit4 = []

for i in list_1:
    if len(str(i)) == 1:
        digit1.append(i)
    elif len(str(i)) == 2:
        digit2.append(i)
    elif len(str(i)) == 3:
        digit3.append(i)
    elif len(str(i)) == 4:
        digit4.append(i)
    else:
        print("Not able to identify digit")

print("1 number digit: ", digit1)
print("2 number digit: ", digit2)
print("3 number digit: ", digit3)
print("4 number digit: ", digit4)
