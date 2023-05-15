'''You are given a string s and an integer k. You can choose any character of the string and change 
it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # We can just take the most repeated letter
        # Add k to it if len(char) < len(s) - k
        
        # Find the most repeated character
        letters = dict()
        
        for char in s:
            if letters.get(char):
                letters[char] += 1
            else:
                letters[char] = 1
                
        
        
        