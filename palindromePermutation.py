def isPalindrome(string):
    hashString = [0] * 27
    isPalindromeCount = 0
    for character in string.replace(' ','').lower():
        hashString[ord(character)%96] += 1
        if hashString[ord(character)%96]%2 != 0:
            isPalindromeCount += 1    
        else:
            isPalindromeCount -= 1        
    if(isPalindromeCount>1):
        return False
    else:
        return True

print isPalindrome('Tact Coa') # True, O(n)
print isPalindrome('aaabbcc') # True , O(n)
print isPalindrome('aaaabbbccc') # False , O(n)