import string

text1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text2 = "http://www.pythonchallenge.com/pc/def/map.html"

def trans(string1111):
    text2 = ""
    for i in string1111:
        if i in string.punctuation + string.whitespace:
            text2 += i
        elif i not in "yz":
            text2 += string.ascii_lowercase[string.ascii_lowercase.index(i) + 2]
        elif i == "y":
            text2 += "a"
        else:
            text2 += "b"
    return text2

print(trans(text1))
print(trans(text2))
