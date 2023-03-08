import re

pattern="[0-9]"
input_string="abc12345"
result=re.findall(pattern,input_string)
print(result)