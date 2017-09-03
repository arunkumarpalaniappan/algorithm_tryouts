def isPermutation(fullString,subString):
    stringHash = [0] * 128
    for character in fullString:
        stringHash[ord(character)%128] = stringHash[ord(character)%128]+1
    for character in subString:
        if stringHash[ord(character)%128] <= 0:
            return False
        else:
            stringHash[ord(character)%128] = stringHash[ord(character)%128]-1
    return True


print isPermutation('hello','lloe') # True, O(a + b)
print isPermutation('hello','zlloe') # False, O(a + b)
print isPermutation('hello','elhol') # True, O(a + b)
