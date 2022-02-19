import re

txt = "love regex or hate regex, can't ignore regex"

pattern1 = re.compile("(?<=(love|hate)\s)regex")
pattern2 = re.compile("(?<!(love|hate)\s)regex")



matches = pattern2.finditer(txt)
for match in matches:
    print(match)
