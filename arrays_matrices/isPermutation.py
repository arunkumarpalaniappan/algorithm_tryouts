def isPermutation(string,SubString):
    hashMapforString = [0] * 128
    for character in string:
        hashMapforString[ord(character)%128] = hashMapforString[ord(character)%128] + 1
    for character in SubString:
        if hashMapforString[ord(character)%128] <= 0:
            return False
        else:
            hashMapforString[ord(character)%128] = hashMapforString[ord(character)%128] - 1
    return True

print isPermutation('hello','lleho')
print isPermutation('arun','run')
print isPermutation('test','tex')
# o(n) + o(n) = 2o(n) = ~ o(n)