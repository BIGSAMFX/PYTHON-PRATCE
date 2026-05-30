for number in range(1,11) :
    print(number)

# EXECISE 2 #

items = ["bread","milk", "eggs", "rice"]
for item in items:
    print(item)

# EXERCISE 3 #

prices = [15, 25, 30, 10]
total = 0
for price in prices:
    total += price
print(f"total price is {total}")

# EXERCISE 4 #
for even_number in range(2, 21, 2):
    print(even_number)

# EXERCISE 5
numbers = [23, 8, 56, 12, 90, 34]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"Largest number is {largest}")


# EXERCISE 6
correct_password = "python123"

for attempt in range(1,4) :
    user_password = input("enter your password: ")

    if user_password == correct_password :
       print("Access granted")
else:
    print("account locked")

# EXERCISE 7
prices = [50, 120, 75, 200, 30]

total = 0
count = 0
highest = prices[0]

for price in prices:
    total += price
    count += 1

    if price > highest:
        highest = price

print(f"Total Cost: {total}")
print(f"Number of Items: {count}")
print(f"Most Expensive Item: {highest}")