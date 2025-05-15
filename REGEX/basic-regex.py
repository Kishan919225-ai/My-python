import re

name="ram"
pattern = "^[A-Za-z]+$"

if re.match(pattern,name):
    print(name)
else:
    print("INVALID NAME")



