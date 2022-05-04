"""
1.	Write a program to take Employee Id, Name, Salary and Designation from user then perform below operations.
    1. Write Json data in json file.
    2. Read Json data from the json file.
"""


# employeeID = input("Enter Employee ID:")
# name = input("Enter Employee Name:")
# salary = input("Enter Employee Salary:")
# designation = input("Enter Employee Designation:")

# filename = open("employeedata.json", 'w')
# filename.write("Employee ID is: " + employeeID)
# filename.write("\nEmployee name is:" + name)
# filename.write("\nEmployee salary is:" + salary)
# filename.write("\nEmployee Designation is:" + designation)

# filename = open("employeedata.json", 'r')
# print(filename.read())

# filename.close()


"""
2. Write a program to perform below operations from existing json file.
     1. Print the list of employee name and salary whose name being started from "S"
     2. Print the list of employee name whose salary is less than 30000.
     3. Print the list of employees (all details) whose age is between 25-45.
     4. Print the list of employee name who are have knowledge of Python and Java.
"""
import json


def fileopen():
    global filename
    filename = open("Employee.json", "r")
    global data
    data = json.load(filename)


def fileclose():
    filename.close()


def employee_name_starts_with_s():
    fileopen()
    for i in data["Employees"]:
        if "S" in i["Employee Name"][0]:
            print("Employee name starts with S is {} and salary is {}".format(i["Employee Name"], i["Employee Salary"]))
    fileclose()


def employee_salary_less_than_30000():
    fileopen()
    for i in data["Employees"]:
        if i["Employee Salary"] < 30000:
            print("Salary of {} is less than 30000".format(i["Employee Name"]))
    fileclose()


def employee_age_between_25_45():
    fileopen()
    for i in data["Employees"]:
        if 25 < i["Employee Age"] < 45:
            print("Employee age > 25 and < 45 are:\n", i)
    fileclose()


def employee_programming_lang_python_java():
    fileopen()
    for i in data["Employees"]:
        if "Java" in i["Programming Languages"] and "Python" in i["Programming Languages"]:
            print("Employee who is having knowledge of Java and Python are:", i["Employee Name"])
    fileclose()


employee_name_starts_with_s()
employee_salary_less_than_30000()
employee_age_between_25_45()
employee_programming_lang_python_java()
