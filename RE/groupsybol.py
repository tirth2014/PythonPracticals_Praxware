import re


pattern="(a|b|c)xz"
input_string="axz bxz"
result=re.findall(pattern,input_string)

print(result)