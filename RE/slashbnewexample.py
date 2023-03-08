import re

pattern="\Bfoo"
input_string="afootball"
result=re.findall(pattern,input_string)
print(result)

