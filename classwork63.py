# $ - Used to check if string in end of string
# ^ - Used to check if string in start of string
# . - Used to check is anything(except \n) is present
# * - Zero or more occurences

import re
s = "I am in 1st year not in 2nd ohkk"
result = re.search('.am.', s)
print(result)
result = re.search('^I', s)
print(result)
result = re.search('^A', s)
print(result)
result = re.search('ohkk$', s)
print(result)
result = re.search('2nd$', s)
print(result)