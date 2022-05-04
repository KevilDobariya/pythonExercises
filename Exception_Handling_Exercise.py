"""
Write a program to verify offer is applicable for user Or not based on below criteria. If any of the criteria doesn't
meet then offer is not applicable for user. Use custom exception and let user know about all criteria in case user
doesn't fall back under. Use custom exception and let user know about result.
  1. If user is >= 25 year old.
  2. If user us Male.
  3. If user family member is less than 5.
"""


class Error(Exception):
    """Created base class for other Exceptions"""
    pass


class InvalidValueErrorException(Error):
    """Raised when Invalid value entered"""
    pass


class InvalidGenderException(Error):
    """Raised when Invalid gender input provided"""
    pass


class InvalidFamilyCountException(Error):
    """Raised when Family count less than 0 and greater than 5"""


def age():
    while True:
        try:
            age = int(input("Enter user's age: "))
            if age < 25 :
                raise InvalidValueErrorException
            break
        except InvalidValueErrorException:
            print("Enter age which can be consider for offer")


def gender():
    while True:
        try:
            gender = input("Enter user's gender: ")
            if gender != "Male":
                raise InvalidGenderException
            break
        except InvalidGenderException:
            print("Enter Male Gender in order to be consider for offer")


def family_count():
    while True:
        try:
            family_member_count = int(input("Enter user's family member count: "))
            if family_member_count not in range(0,5):
                raise InvalidFamilyCountException
            break
        except InvalidFamilyCountException:
            print("Enter family count greater than 0 and less than 5 in order to be consider for offer")


age()
gender()
family_count()
print("Congratulations!!! You are applicable for an offer..")