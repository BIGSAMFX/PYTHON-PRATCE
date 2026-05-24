### EXERCISE 1 ###
"""
 if the name is less than 3 character long
   name must be at least  3 character long
 otherwise if is more than 50 character long
   name must be a maximum of 50 character long
 otherwise
   name looks good

"""
### SOLUTION ###

name = len(input("What is your name? "))
if name < 3:
    print("name must be at least 3 characters long")

elif name > 50:
    print("name must be less than 50 characters long")
else:
    print("name looks good ")



## CORRECTION ##
name = input("What is your name? ")

if len(name) < 3:
    print("name must be at least 3 characters long")

elif len(name) > 50:
    print("name must be a maximum of 50 characters long")

else:
    print("name looks good")


### EXERCISE 2 ###

"""Complex Beginner Exercise

This exercise combines:

variables
input()
int()
comparison operators
logical operators
if, elif, else
STUDENT ADMISSION CHECKER
Question

Write a program that asks the user for:

their age
their exam score

Rules:

If age is less than 18
→ print "You are too young for admission"
Otherwise if score is less than 50
→ print "You did not pass the exam"
Otherwise if score is greater than or equal to 90
→ print "Excellent performance"
Otherwise
→ print "Admission granted" """

### SOLUTION ###
age = int(input("enter your age?: "))
exam_score = int(input("enter your exam score?: "))

if age < 18:
    print("You are too young for admission")

elif exam_score < 50:
    print("You did not pass the exam")

elif exam_score >= 90:
    print("Excellent performance")

else:
    print("Admission granted")

###   EXERCISE 4 ###
""" EXERCISE: MOVIE TICKET PRICE SYSTEM
Question

Write a program that asks the user for their age and prints ticket price based on rules below:

🎬 Rules
If age is 0 to 5
→ print "Free ticket"
If age is 6 to 12
→ print "Child ticket: $5"
If age is 13 to 17
→ print "Teen ticket: $8"
If age is 18 to 59
→ print "Adult ticket: $12"
If age is 60 or above
→ print "Senior ticket: $6".

🚀 EXTRA CHALLENGE (Optional)
Add this rule at the top:
If age is less than 0
→ print "Invalid age" """

### SOLUTION ###
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")

elif age <= 5:
    print("Free ticket")

elif age <= 12:
    print("Child ticket: $5")

elif age <= 17:
    print("Teen ticket: $8")

elif age <= 59:
    print("Adult ticket: $12")

else:
    print("Senior ticket: $6")
"""Elimination logic

Each failed condition reduces the remaining possibilities.

This is how programmers simplify conditions instead of writing long checks every time."""

### EXERCISE 5 ###
"""ATM WITHDRAWAL SYSTEM
Question

Write a program that asks the user for:

account balance
withdrawal amount
🧾 Rules
If withdrawal amount is less than or equal to 0
→ print "Invalid withdrawal amount"
If withdrawal amount is greater than balance
→ print "Insufficient funds"
If withdrawal amount is exactly equal to balance
→ print "You have emptied your account"
If withdrawal amount is less than balance
→ print "Transaction successful"
After successful withdrawal, print the remaining balance.
"""
### SOLUTION ###
account_balance = int(input("enter your account balance: "))
withdrawal_amount = int(input("enter your withdrawal amount: "))

remaining_balance = account_balance - withdrawal_amount

if withdrawal_amount <= 0:
    print("invalid withdrawal amount")

elif withdrawal_amount > account_balance:
    print("insufficient funds")

elif withdrawal_amount == account_balance:
    print("you have emptied your account")

else:
    print("Transaction successful")
    print("Remaining balance:", remaining_balance)

### EXERCISE 6 ###
