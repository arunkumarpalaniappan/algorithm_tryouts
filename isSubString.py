def isSubString(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        hashMap = [0] * 128
        for character in string1:
            hashMap[ord(character)%128] = hashMap[ord(character)%128] + 1
        for character in string2:
            hashMap[ord(character)%128] = hashMap[ord(character)%128] - 1
        for hashes in hashMap:
            if hashes != 0:
                return False
        return True

print isSubString('abcd','dcca')
print isSubString('waterbottle','erbottlewat')