import re

pattern="mn?n"
input_string="mn mnnnnn"

#result=re.match(pattern,input_string)
result=re.findall(pattern,input_string)
print(result)