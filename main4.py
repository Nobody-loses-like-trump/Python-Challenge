import re
import requests
pattern = re.compile(r"next nothing is (\d+)")

nothing = 12345
url2 = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

print("http://www.pythonchallenge.com/pc/def/peak.html")

for i in range(400):
    content = requests.get(url2, params={"nothing": nothing}).text
    print(f"""{i+1}) {content}""")
    try:
        nothing = int(pattern.search(content).group(1))
        if content in ["""There maybe misleading numbers in the 
text. One example is 82683. Look only for the next nothing and the next nothing is 63579""", "<font color=red>Your hands are getting tired </font>and the next nothing is 94485"]:
            print(nothing)
    except AttributeError:
        if content == "Yes. Divide by two and keep going.":
            nothing //= 2
            print(nothing)
        else:
            raise SystemExit
