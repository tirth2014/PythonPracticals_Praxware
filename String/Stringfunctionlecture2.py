str1="hello i am python expert"

print(str1.capitalize())

str2="THIS IS EXAMPLE FROM CAPITAL TO LOWER"
print(str2.casefold())

str3="This is My Mobile,ThisMobile is Very  nice Mobile"
print(str3.count("Mobile"))

str4="This is Dummey Example From Python Demo.and This Done@"
print(str4.endswith("@"))

str5="This is Math fun and it is really good"
print(str5.find("is"))

str6="abcd111234"
print(str6.isalnum())

str7="kshkjh"
print(str7.isalpha())

str8="10\u00B2"
print(str8.isdigit())

str9="this is my first python title example"
print(str9.title())

str10="This is Python Demo"
strfetch="Demo1"

print(strfetch in str10)


import re

str11="1111 Hello Python demo"
print(re.findall('\d',str11))

str12="pythön"
b=bytes('pythön',encoding="utf-8")
print(str(b,encoding='ascii',errors='ignore'))


str13="Hello this is Python"

print(str13.center(50,'*'))







