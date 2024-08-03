# Write a Python program to check if a given substring exists in a string.

char_string = input("Enter any String: ")
char_sub_string = input("Enter any Substring to check out in string: ")

if char_sub_string.lower() in char_string.lower():
    print("Substring Found! ")
else:
    print("Substring not Found...")

print("Please try again...")
