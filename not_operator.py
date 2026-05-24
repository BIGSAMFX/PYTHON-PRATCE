# EXERCISE 1 #
"""Airport Security System

A passenger should NOT enter the boarding gate if:

they do NOT have a boarding pass
OR they do NOT have a passport
OR they are carrying banned items

Write a Python program that:

prints "Access denied" if any security problem exists
otherwise prints "Access granted" """
from idlelib import window

# SOLUTION #

has_a_bording_pass = True
has_a_passport = False
carrying_banned_items = True

if not has_a_bording_pass or not has_a_passport or carrying_banned_items:
    print("Access denied")
else:
    print("Access granted")




# EXERCISE 2 #
"""Very Complex Exercise — Smart Home Security System

A smart home alarm should turn ON if:

the door is NOT locked
OR the window is NOT closed
OR motion is detected inside the house
OR smoke is detected

Write a Python program that:

prints "Alarm activated" if any danger or security problem exists
otherwise prints "House is safe"

Use:

variables
not
or
if/else

Try to read your condition like normal English while coding."""

# SOLUTION #
door_not_locked = True
window_not_closed = False
motion_detected = True
smoke_detected = False

if  door_not_locked or  window_not_closed or  motion_detected or  smoke_detected:
    print("alarm activated")
else:
    print("House is safe")

# plain english this means the alarn should turn when any of this is true and in my code it:
# the alarm should turn on when he door is not locked or the window is not close or motion is detected inside the house
#or smoke is detected
# from my code the door is not locked but the window is close and motion is detected inside the house but smoke is ot detected




#### EXERCISE 3 ###
"""Very Complex Exercise — University Admission + Scholarship Filter

A student can be admitted AND considered for scholarship if ALL these rules are followed:

🎓 Admission Rules:

A student is eligible for admission if:

they scored 200 or more in JAMB
AND they have at least 5 credits in WAEC
AND they are NOT below 16 years old
💰 Scholarship Rules (extra condition):

A student can still get scholarship if:

they are a sports champion
OR
they won a national competition

BUT:

🚫 A student is NOT eligible for scholarship if:

they have a criminal record
🧠 TASK

Write a Python program that:

Checks if the student is eligible for admission
Checks if the student is eligible for scholarship
Prints:
"Admitted" if eligible for admission
"Admitted but no scholarship" if admitted but no scholarship
"Admitted with scholarship" if both
"Rejected" if not admitted
💻 Given variables
jamb_score = 250
waec_credits = 
age = 18

sports_champion = True
won_competition = False
criminal_record = False"""

### SOLUTION ###

jamb_score = 250
waec_credits = 6
age = 18

sports_champion = True
won_competition = False
criminal_record = False

if jamb_score >= 200 and waec_credits >= 5 and not age < 16 and  sports_champion or not won_competition and  criminal_record:

 print("Admitted with scholarship")
else:
 print("admitted but no scholarship")

# logic behind my code the student has 200 and 6 credit in waec and not less than 16 years old = he is admmitted
# but for him to be admitted and with scholarship he must not has criminal record whether he is a sport champion or not
# or he has won competition or not as fas that he has a criminal record no scholarship for him
# my student is eligible for admission but no scholarship because he has a criminal record though he won competition


####### CORRECTION
jamb_score = 250
waec_credits = 6
age = 18

sports_champion = True
won_competition = False
criminal_record = False

admitted = jamb_score >= 200 and waec_credits >= 5 and age >= 16

scholarship = (sports_champion or won_competition) and not criminal_record

if admitted and scholarship:
    print("Admitted with scholarship")

elif admitted and not scholarship:
    print("Admitted but no scholarship")

else:
    print("Rejected")



### EXERCISE 4 ###

"""Very Complex Exercise — Online Banking Fraud Detection System

A customer can access online banking ONLY if:

✅ Login Requirements
the password is correct
AND the account is verified
AND the customer is NOT banned
🚫 Fraud Detection Rules

The account should be temporarily blocked if:

suspicious activity is detected
OR too many failed login attempts happened
OR the customer is using a blacklisted device
🧠 TASK

Write a Python program that:

Prints "Access granted" if:
login requirements are satisfied
AND there is NO fraud issue
Prints "Account temporarily blocked" if fraud is detected
Prints "Login failed" if login requirements are not satisfied
💻 Use These Variables
correct_password = True
account_verified = True
customer_banned = False

suspicious_activity = False
failed_login_attempts = True
blacklisted_device = False
🔥 IMPORTANT

You MUST use:

and
or
not
brackets ()
💡 Hint

Try breaking the logic into:

login_success = ...
fraud_detected = ..."""

### SOLUTION ###

correct_password = True
account_verified = True
customer_banned = False

suspicious_activity = False
failed_login_attempts = True
blacklisted_device = False

login_success = (correct_password and account_verified) and not customer_banned

fraud_detected = suspicious_activity or failed_login_attempts or blacklisted_device

if login_success and not fraud_detected:
    print("Access granted")

elif  login_success and fraud_detected:
    print("Account temporarily blocked")
else:
    print("Login failed")



member_suspended = False
if not member_suspended:
    print("access allowed")
else:
    print("access denied")



