import re

pattern="thi+"

input_string="thi is game this"

result=re.findall(pattern,input_string)
print(result)