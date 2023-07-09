'''

Define a class Account with the below attributes:
cardNumber of
pin of type Int
balance of
amour
Note: You need to either Compile or Submit your program to keep it saved. The program will NOT be auto-saved if the window is closed.
float (represents existing account balance0219436238
of type float (represents last withdrawal
of Type String
Define the required method in the Account class which takes all parameters in the above sequence and sets the value of attributes to parameter values while creating an object of the class.
Create a method inside Account class. This method takes a withdrawlAmount value as argument and if this amount is less or equal to the existing account balance then the method
the new balan and updates the balance. The method also,
sets/overw
the withdrawlAmount attribute of Account class
with the new withdrawlAmount value.
If the existing account balance is 60
withdrawlAmount (passed as argument) is 10, then the updated balance should be 50 and updated withdrawlAmount would be 10.
Define another class ATM with the below attributes:
branch_name of type String
accountList of type
1st having Account objects


Define the required method in the ATM class which takes all parameters in the above sequence and sets the value of attributes to
parameter values
Create another 
an object of the class.
inside the ATM class.


This method takes the card number as first argument, second argument and withdrawlAmount as the third method should calculate the updated method created in class Account if the card are valid.
This
and pin entered
If the account with given card number and pin is not found, then the method returns None.
Note: In Python None means NULL Object, Accordingly program will display the message "No account
the quotes)

the card number, pin, balance, withdrawal amount and account type for each account taken after other and is repeated for number of Account objects the first line of input
The next three lines of input refer to the card
withdraw money from the account.

Sample Input:
2
12345
22@DT20219436238
12
30.0
45678
400.0
200.0
salary
45678
98
100.0
salary

Output:
45678 300.0 100.0
12345 30.0 45678 300.0
0219436238

'''

'''
class Account:
    def __init__(self, card_number, pin, balance, withdrawal_amount):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.withdrawal_amount = amount

class ATM:
    def __init__(self, account_list):
        self.account_list = account_list

    def withdraw_amount(self, card_number, pin, withdrawal_amount):
        for account in self.account_list:
            if account.card_number == card_number and account.pin == pin:
                account.withdraw(withdrawal_amount)
                return account

        return None
    def method2(self,t):
        ls=[]
        for a in alsit:
            if a.t.lower()==t.lower():
            ls.append(a)
        ls.sort(key=lambda x:x.b)
        dic={}
        for l in ls:
            dic[l.n]=l.b
        for k,v in dic.items():
            print(k,v)
            

# Main program
if __name__ == "__main__":
    n = int(input("Enter the number of accounts: "))
    account_list = []
    for _ in range(n):
        card_number = input("Enter the card number: ")
        pin = int(input("Enter the pin: "))
        balance = float(input("Enter the balance: "))
        withdrawal_amount = float(input("Enter the withdrawal amount: "))

        account = Account(card_number, pin, balance, withdrawal_amount)
        account_list.append(account)

    atm = ATM(account_list)

    card_number = input("Enter the card number: ")
    pin = int(input("Enter the pin: "))
    withdrawal_amount = float(input("Enter the withdrawal amount: "))

    account = atm.withdraw_amount(card_number, pin, withdrawal_amount)
    if account:
        print(f"{account.card_number} {account.balance} {account.withdrawal_amount}")
    else:
        print("No account found")
    
    t=input()
    atm.method2(t)

'''