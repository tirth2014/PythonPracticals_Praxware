import re

pattern="\w"
input_string='12&":;c_'
result=re.findall(pattern,input_string)
print(result)

