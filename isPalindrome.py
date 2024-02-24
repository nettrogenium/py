from math import floor
def isPalindrome(str, i=0):
    
    # if char[index] == middle char, return True
    if i == floor(len(str)/2): return True 
    
    # if char != opposite char, return False
    if str[i] != str[len(str)-1-i]: return False
    
    # if string is a palindrome with even amount of chars, return itself (thus going to the first function line and returning True)
    return isPalindrome(str, i+1)
