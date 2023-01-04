# Practicing regex
import re
s = "1289890120"
print(re.search("^[1-9][0-9]{9}$", s))