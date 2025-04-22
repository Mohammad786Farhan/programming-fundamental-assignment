# #  PROGRAMMING FUNDAMENTALS
# * The tasks are described in comments below.
# * Solve the tasks by writing your program directly after the task description.
# * Upload your solution on Felix within the given time.


# Task 1: (2 Points)
# Create a list "my_list" with all even numbers from 0 to 100










my_list = []

for i in range(0,101):
    if (i%2 == 0):
        my_list.append(i)

print(my_list)











# Task 2: (2 Points)
# Ask the user for a number.
# State as an output if the number is negative, positive or zero. 







user_number = int(input("Please enter a number: "))
if user_number < 0:
    print("Your number is Negative")
elif user_number > 0:
    print("Your number is Positive")
else:
    print("Your number is ZERO")

















# Task 3: (2 Points)
# Create a line graph using Matplotlib to visualize the monthly average 
# temperature in a city for a year. You are given the following data:





import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
temperatures = [10, 12, 15, 18, 22, 25, 28, 27, 24, 20, 15, 12]
plt.xlabel("Months")
plt.ylabel("Temperatures")
plt.plot(months, temperatures)
plt.show()






















# Task 4: (4 Points) 
# Create a Python class called "BankAccount" that represents a bank account. 
# The class should have the following attributes and methods:
# Attributes:
# - account_number: Represents the account number (a string).
# - balance: Represents the current balance in the account (a floating-point number).
# Methods:
# - Initializes the account and sets the initial balance to 0.
# - deposit(amount): Increases the account balance by the given amount.
# - withdraw(amount): Decreases the account balance by the given amount (if current balance is high enough).
# - get_balance(): Returns the current balance in the account.
# Also test the class by creating an object. 







class BankAccount:
    def __init__(self,ac):
        self.account_number = ac
        self.balance = 0.0
    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance = self.balance - amount
    def get_balance(self):
        return self.balance

bankaccount = BankAccount("12345")
bankaccount.get_balance()
bankaccount.deposit(500)
bankaccount.deposit(500.21)
bankaccount.withdraw(200.46)














# Task 5: (4 Points)
# Write a Python function called "calculate_average" that takes in a list of numbers as 
# an argument and returns the average (mean) of those numbers. 
# The function should handle both positive and negative numbers.
# You are not allowed to use some already predefined mean function.






list_nums = [2,4,6,7,9,11,31,-34,-44]
#list_nums = [1,2,3,4]
def calculate_average(list_nums):
    len_list = len(list_nums)
    total_sum = 0
    for i in list_nums:
        total_sum = total_sum + i
    mean_value = total_sum / len_list
    return mean_value

print(calculate_average(list_nums))






















# Task 6: (4 Points)
# Create a GUI window using Tkinter that displays a "Hello, World!" 
# label and a "Quit" button. 
# When the "Quit" button is clicked, the window should close (hint: destroy()).

import tkinter as tk
w = tk.Tk()
lbl = tk.Label(text = "Hello World!")
lbl.pack()

def Quit():
    w.destroy()
    

btn = tk.Button(text = "Quit", command = Quit)
#btn = tk.Button(text = "Quit", command = quit())
btn.pack() 


w.mainloop()
















