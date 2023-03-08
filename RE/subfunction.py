import re

pattern="\s+"
input_string="i like python this"
replace=''
result=re.subn(pattern,replace,input_string)
print(result)

