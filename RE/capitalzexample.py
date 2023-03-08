import re

pattern="python\Z"
input_string="this is python practical"
result=re.findall(pattern,input_string)
print(result)

