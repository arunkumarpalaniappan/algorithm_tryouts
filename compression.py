def stringCompression(string):
    newString = ''
    index = 0
    tempCount = 1
    while index < len(string):
        tempindex = 1
        while index + tempindex < len(string) and string[index] == string[index + tempindex]:
            tempCount+=1
            tempindex+=1
        newString = newString + string[index]+str(tempCount)
        tempCount = 1
        index = index + tempindex

    if len(string)<=len(newString):
        return string
    else:
        return newString

print stringCompression('test') # test ,O(n)
print stringCompression('aaabbbcccaaa') # a3b3c3a3,O(n)
print stringCompression('compression') # compression,O(n)