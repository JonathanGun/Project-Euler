from math import sqrt, floor
import re

i = floor(sqrt(1121314151617181910))
while True:
    if re.compile(r'1.2.3.4.5.6.7.8.9.0').match(str(i**2)) != None:
        print(i)
        break
    i += 10
