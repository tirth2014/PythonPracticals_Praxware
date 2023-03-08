import re
reg = r"^[0-9]{8,}(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

inputstring=r"12345678A$khkhkj1nn"

if re.fullmatch(reg,inputstring):
    print("Valid")
else:
    print("Invalid")