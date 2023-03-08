import re

pattern="hello*"

input_string="hello this is hello"

result=re.findall(pattern,input_string)
print(result)