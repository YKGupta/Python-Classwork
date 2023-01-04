# Finding Pincodes
# Pincodes don't have letters, don't start with 0, only have 0-9, always 6 digits

# [] - should have anything from what is specified
# {} - it should have exactly the specified number of occurences

import re
s = "208010"
matchFound = re.search('^[1-9][0-9]{5}$', s)
print(matchFound)