import string
with open("asdf.txt") as f:
    text = f.read()

text2 = ""
for i in text:
    if i not in string.punctuation + string.whitespace:
        text2 += i

print(text2)
