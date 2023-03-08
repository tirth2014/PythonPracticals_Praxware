import re

patter="^p...t$"
input_string="playt"
result=re.findall(patter,input_string)
print(result)