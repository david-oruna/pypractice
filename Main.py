
import re
x = open("s.txt")
for i in x:
    i.rstrip()
    stf = re.findall('[0-9]+', i)
