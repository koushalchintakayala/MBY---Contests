import re

name = input()
name = re.sub(r'[^a-zA-Z0-9]', '', name).lower()

if (name == name[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")