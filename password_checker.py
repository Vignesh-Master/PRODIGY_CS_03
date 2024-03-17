import string

print("                         Password complexity checker..\n".upper())
password = input("Enter your password:\n")

upper_count = sum(1 for char in password if char in string.ascii_uppercase)
lower_count = sum(1 for char in password if char in string.ascii_lowercase)
special_count = sum(1 for char in password if char in string.punctuation)
digit_count = sum(1 for char in password if char in string.digits)

length = len(password)

char_types = [upper_count, lower_count, special_count, digit_count]

score = 0

with open('10-million-password-list-top-1000000.txt', 'r') as f:
    check = f.read().splitlines()

if password in check:
    print("\nPassword was found in a common list. " + str(score))
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 15:
    score += 1
if length > 20:
    score += 1
print("\npassword length is " + str(length) + ", adding " + str(score) + " points!")

if sum(1 for count in char_types if count > 0) > 1:
    score += 1

if sum(1 for count in char_types if count > 0) > 2:
    score += 1

if sum(1 for count in char_types if count > 0) > 3:
    score += 1

print("\nPassword has " + str(sum(1 for count in char_types if count > 0)) +
      " different character types, adding " + str(sum(1 for count in char_types if count > 0) - 1) + " points")

print("\nNumber of uppercase characters: ", upper_count)
print("Number of lowercase characters: ", lower_count)
print("Number of special characters: ", special_count)
print("Number of digits: ", digit_count)

if score < 4:
    print("\nThe password is quite weak! Score: " + str(score))
elif score == 4:
    print("\nThe password is ok! Score: " + str(score))
elif 4 < score < 6:
    print("\nThe password is good! Score: " + str(score))
elif score > 6:
    print("\nThe password is strong! Score: " + str(score))
