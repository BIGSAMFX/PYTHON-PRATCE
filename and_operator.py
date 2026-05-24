# EXERCISE 1
"""A student can enter the school only if:

they are wearing school uniform
and they have their ID card
Create variables and use the and operator to check if the student can enter.
"""

#  SOLUTION

wearing_school_uniform = True
have_an_id_card =True
print(wearing_school_uniform and have_an_id_card)

# EXERCISE 2
"""A customer can place an order only if:

they are logged in
and they have enough money in their account

Write a program that prints:

"Order successful" if both conditions are true
otherwise print "Order failed" """

# SOLUTION
is_logged_in = True
have_enough_money = True

if is_logged_in and have_enough_money:
    print("Order successful")
else:
    print("Order failed")

# EXERCISE 3
"""A student can gain admission only if:

they scored at least 200 in JAMB
and they have at least 5 credits in WAEC
and they are at least 16 years old

Write a program that checks whether the student is eligible for admission."""

# SOLUTION
jamb_score = 250
waec_result_5_credits = True
age = 20

if jamb_score >= 200 and waec_result_5_credits and age >= 16:
    print("eligible")
else:
    print("not eligible")