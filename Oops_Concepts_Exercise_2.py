"""
2.	Create banking application using OOPs concept and perform following operations:-
    1. Account holder can deposit amount.
    2. Account holder can with amount.
    3. Account holder can view total available balance.
"""


class Banking_Application:

    global total_balance
    total_balance = 0

    def deposit(self, total_balance):
        amt_deposit = float(input("Enter the amount you would like to deposit in your account:"))
        total_balance = total_balance + amt_deposit
        print("Your {} has been deposited successfully in your account".format(total_balance))
```````
    def withdrwl(self):
        withdwl = float(input("Enter the amount you would like to withdraw from your account: "))


ba = Banking_Application()
ba.deposit(total_balance)









#     def withdrawal(self, balance):
#         withdwl = float(input("Enter the amount you would like to withdraw from your account: "))
#         ba.total_balance = ba.total_balance - withdwl
#         print("{} has been withdrawn from your account, remaining balance is: {}".format(withdwl, ba.total_balance))
#

# ba.withdrawal(total_balance)


