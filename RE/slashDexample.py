import re

pattern="\d"
input_string="1ab34xyz4567"
result=re.findall(pattern,input_string)
print(result)

