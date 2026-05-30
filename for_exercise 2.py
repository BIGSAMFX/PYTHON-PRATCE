# EXERCISE 1

for number in range(1, 16) :
    print(number)

# EXERCISE 2

colors = ["Red", "Blue", "Green", "Yellow"]

for color in colors:
    print(color)

# EXERCISE 3
prices = [12, 18, 25, 10, 15]

total = 0
for price in prices:
    total += price
print(f"Total price is: {total}")

# EXERCISE 4
for odd_number in range(1, 20, 2) :
    print(odd_number)

# EXERCISE 5
numbers = [45, 12, 67, 3, 89, 22]

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print(smallest)

# EXERCISE 6
correct_username = "admin"
correct_password = "python123"

for attempt in range(1,4) :
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Login successful")
        break
else:
    print("account locked")

# EXERCISE 7
prices = [100, 250, 75, 300, 150]

total = 0
count = 0
highest = prices[0]
lowest = prices[0]

for price in prices:
    total += price
    count += 1

    if price > highest:
        highest = price
    if price < lowest:
        lowest = price

average = total / count

print(f"Total: {total}")
print(f"Items: {count}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average}")




