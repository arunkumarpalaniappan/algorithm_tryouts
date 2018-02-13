def compressString(string):
    newString = ''
    index = 0
    tempCount = 1
    while index < len(string):
        tempIndex = 1
        while index+tempIndex < len(string) and string[index] == string[index+tempIndex]:
            tempCount+=1
            tempIndex+=1
        newString = newString + string[index]+str(tempCount)
        tempCount = 1
        index = index + tempIndex
    if len(string) <= len(newString):
        return string
    else:
        return newString

print compressString('test') # test ,O(n)
print compressString('thissusssssss') # a3b3c3a3,O(n)
print compressString('compression') # compression,O(n)