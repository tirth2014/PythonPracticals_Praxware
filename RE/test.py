import re
reg="^[a-z]{8,18}"

inputstring=r"asdfghjk"

if re.fullmatch(reg,inputstring):
    print("Valid")
else:
    print("Invalid")