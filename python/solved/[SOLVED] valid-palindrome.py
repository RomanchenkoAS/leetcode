"""A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = 0
        r = len(s) - 1
        s = s.lower()
        
        while l <= r:
            if not s[l].isalnum():
                l = l + 1
                continue
            if not s[r].isalnum():
                r = r - 1
                continue
            
            if s[l] == s[r]:
                l = l + 1
                r = r - 1
            else:
                return False
        
        return True
        
s = Solution()

str = "A man, a plan, a canal: Panama"

print(s.isPalindrome(str))