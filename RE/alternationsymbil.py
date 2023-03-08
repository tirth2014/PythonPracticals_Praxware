import re


pattern="a|b"
input_string="ab pq"
result=re.findall(pattern,input_string)

print(result)
