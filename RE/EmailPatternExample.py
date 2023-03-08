import re
regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

input_string="kachhelahitesh@gmail.com"

if re.fullmatch(regex,input_string):
    print("Valid Email")
else:
    print("Invalid Email")