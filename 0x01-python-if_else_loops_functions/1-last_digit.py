#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit
last_digit = abs(number) % 10 if number >= 0 else -(abs(number) % 10)

# Print the initial part of the message
print("Last digit of", number, "is", last_digit, end=" ")

# Determine the message based on the last digit's value
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")