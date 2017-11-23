s1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

s2 = "map"

def maketrans(s):
    s2 = ""
    for i in range(len(s)):
        c = s[i]
        if not c.isalnum():
            o = ord(c)
        elif c == 'y' or c == 'z':
            o = ord(c) - 26 + 2
        else :
            o = ord(c) + 2
        c2 = chr(o)
        s2 += c2
    return s2

print(maketrans(s1))
print(maketrans(s2))