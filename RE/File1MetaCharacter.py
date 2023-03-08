import re

pattern="^a...s$"
input_string="axyzs"
result=re.findall(pattern,input_string)
print(result)