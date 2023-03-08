import re

pattern="\Athe"
input_string="the Python is good"
result=re.findall(pattern,input_string)
print(result)

