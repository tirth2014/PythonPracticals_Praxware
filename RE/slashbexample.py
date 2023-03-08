import re

pattern=r"\bfoo"
input_string="football game"
result=re.findall(pattern,input_string)
print(result)

