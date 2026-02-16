def hammingDistance(s1,s2):
    if len(s1) != len(s2):
        return ("Invalid - Len should be same!")
    else:
        count = 0
        for i in range(len(s1)):
           if s1[i] != s2[i]:
                count = count + 1
        return count
print(hammingDistance("Helloo", "Helium"))
print(hammingDistance("abcd","adcb"))
print(hammingDistance("ab","c"))
print(hammingDistance("ab","a"))

def is_palindrome(palindrome):
    return palindrome == palindrome[::-1]
print(is_palindrome("madam"))