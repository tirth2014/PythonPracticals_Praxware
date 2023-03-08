import re

pattern="\S"
input_string="Python Example play xyz "
#result=re.match(pattern,input_string)
result=re.findall(pattern,input_string)
print(result)

