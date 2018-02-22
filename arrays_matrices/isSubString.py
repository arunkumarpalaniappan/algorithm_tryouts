def isSubString(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        hashMap = [0] * 128
        for character in string1:
            hashMap[ord(character)] = hashMap[ord(character)] + 1
        for character in string2:
            if hashMap[ord(character)] <= 0:
                return False
            else:
                hashMap[ord(character)] = hashMap[ord(character)] - 1
        return True

print isSubString('abcd','dbca')
print isSubString('waterbottle','erbottlewat')
# o(n) + o(n) = 2o(n) = ~ o(n)