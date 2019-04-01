import re

patterns = ["term1" ,"term2"]

text = "This is the text with term1"

for pattern in patterns:
    print("Searching  for term {}".format(pattern))

    if re.search(pattern,text):
        print("Match")
        match = re.search(pattern,text)
    else:
        print("No Match")
print(type(match))

print(match.start()) #Its not just a boolean it keeps info


print(re.findall('match',"it finds total match in text of this match"))
