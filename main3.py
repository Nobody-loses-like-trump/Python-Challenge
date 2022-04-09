import re
import string
with open("asdf2.txt") as f:
    text = f.read()

# text2 = ""
# for i in text:
#     if i not in string.ascii_lowercase + string.ascii_uppercase + string.whitespace:
#         text2 += i
# print(text2)

pattern = re.compile(r"[a-z]([A-Z]{3}[a-z][A-Z]{3})[a-z]")
matches = pattern.finditer(text)
for match in matches:
    print(match.group(1))

# print(len(matches))
