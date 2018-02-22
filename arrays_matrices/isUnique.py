def isUnique(string):
    stringHash = [0]*128
    for character in string:
        if stringHash[ord(character)%128] > 0:
            return False
        else:
            stringHash[ord(character)%128]+=1
    return True

print isUnique('test') # False ,O(n)
print isUnique('aquickboASDFwnfxjmps><verthlzydg')  # True ,O(n)
