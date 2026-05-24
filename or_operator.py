# EXERCISE 1
"""A customer can use the café Wi-Fi if:

they buy coffee
or they buy snacks

Print:

"Wi-Fi granted"

print:

"Wi-Fi denied" """

# SOLUTION

buy_coffe = True
buy_snacks = False
print(buy_coffe or buy_snacks)

if buy_coffe or buy_snacks:
    print("Wi-Fi granted")
else:
    print("Wi-Fi denied")

# EXERCISE 2
"""A player can join the football team if:

they are fast
or they are skillful

Print:

"Selected"

Otherwise print:

"Not selected" """

# SOLUTION

fast_player = True
skillful_player = False

if fast_player or skillful_player:
    print("Selected")
else:
    print("Not selected")

# EXERCISE 3
"""A phone can unlock if:

the correct PIN is entered
or fingerprint is correct
or facial recognition works

Print:

"Phone unlocked"

Otherwise print:

"Access denied" """

# SOLUTION

pin = True
fingerprint = False
facial_recognition = False

print(pin or fingerprint or facial_recognition)

if pin or fingerprint or facial_recognition:
    print("phone unlocked")
else:
    print("Access denied")

# exercise 4
"""A student can receive a scholarship if:

they scored at least 300 in JAMB
or they are a sports champion
or they won a national academic competition

Write a program that checks whether the student is eligible for the scholarship."""

# SOLUTION
jamb_score = 400
sports_champion = True
national_academic_competition = False

if jamb_score >= 300 or sports_champion or national_academic_competition:
    print("Eligible For Scholarship")
else:
    print("Not Eligible For Scholarship")
