def isEditedOnce(stringOne,stringTwo):
    stringOneLength = len(stringOne)
    stringTwoLength = len(stringTwo)
    totalChanges = 0
    if stringOneLength - stringTwoLength > 1 or stringOneLength - stringTwoLength < -1:
        return False
    else:
        if stringOneLength == stringTwoLength:
            for index in range(0,stringOneLength):
                if stringOne[index] != stringTwo[index]:
                    totalChanges += 1
        else:
            hashMap = [0] * 27
            for character in stringOne.lower():
                hashMap[ord(character)%96] += 1
            for character in stringTwo.lower():
                hashMap[ord(character)%96] -= 1
            for index in range(0,27):
                if hashMap[index] != 0:
                    totalChanges += 1
        if totalChanges == 1:
            return True
        else:
            return False

print isEditedOnce('ple','ple') # True ,O(n)
print isEditedOnce('pale','pales') # True ,O(n)
print isEditedOnce('pale','bale') # True ,O(n)
print isEditedOnce('pale','bake') # False ,O(n)