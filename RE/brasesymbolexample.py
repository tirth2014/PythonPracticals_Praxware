import re


pattern="[0-9]{2,4}"
input_string="12 this 13 is string 4567"
result=re.findall(pattern,input_string)

print(result)
