def isEditedOnce(stringOne,stringTwo):
    stringOneLength = len(stringOne)
    stringTwoLength = len(stringTwo)
    totalChanges = 0
    if abs(stringOneLength - stringTwoLength) > 1:
        return False
    else:
        if stringOneLength == stringTwoLength:            
            for index in range(0,stringOneLength):
                if stringOne[index] != stringTwo[index]:
                    totalChanges = totalChanges + 1
        else:
            hashTable = [0] * 27
            for character in stringOne.lower():
                hashTable[ord(character)%96] = hashTable[ord(character)%96] + 1
            for character in stringTwo.lower():
                if hashTable[ord(character)%96] > 0:
                    hashTable[ord(character)%96] = hashTable[ord(character)%96] - 1
                else:
                    hashTable[ord(character)%96] = hashTable[ord(character)%96] + 1
            for index in range(0,27):
                if hashTable[index] > 0:
                    totalChanges = totalChanges +1
    if totalChanges > 1:
        return False
    else:
        return True


print isEditedOnce('pale','ple') # True ,O(n)
print isEditedOnce('pales','pale') # True ,O(n)
print isEditedOnce('pale','bale') # True ,O(n)
print isEditedOnce('pale','bake') # False ,O(n)