import re

pattern="\$a"
input_string="$abc"
result=re.findall(pattern,input_string)
print(result)