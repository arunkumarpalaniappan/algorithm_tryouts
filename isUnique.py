def verifyUnique(string):
    if len(string) > 128:
        return False
    characterHash = [0] * 128
    for character in string:
        hashKey = ord(character)%128
        if(characterHash[hashKey] > 0):
            return False
        else:
            characterHash[hashKey] = characterHash[hashKey]+1
    return True


print verifyUnique('test') # False ,O(n)
print verifyUnique('aquickboASDFwnfxjmps><verthlzydg')  # True ,O(n)
