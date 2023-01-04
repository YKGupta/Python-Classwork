import re
s = "I am in 1st year of college"
isCollegePresent = re.search("college", s)
if isCollegePresent:
    print("College is present in sentence")
else:
    print("College is not present in the sentence")