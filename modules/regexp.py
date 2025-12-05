import re
ph = input("Enter phone number: ")
exp = r'^(\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]?\d{4}$'
if re.match(exp, ph):
    print("Valid number")
else:
    print("Invalid number")
