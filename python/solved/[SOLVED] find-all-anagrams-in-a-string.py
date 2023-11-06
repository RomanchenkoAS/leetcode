"""Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        def isanagram(a, b):
            return sorted(a) == sorted(b)
            
        dict_p = {}
        length = len(p)
        for char in p:
            if not dict_p.get(char):
                dict_p[char] = 1
            else:
                dict_p[char] += 1
                
        anagrams_index = []
        
        slide = {}
        
        # Initialize sliding window dict
        for char in s[:length]:
            if not slide.get(char):
                slide[char] = 1
            else:
                slide[char] += 1
        
        if slide == dict_p:
            anagrams_index.append(0)
        
        # Look for p's anagrams in s
        for i in range(1, len(s) - length + 1):
            # Remove skipped letter
            slide[s[i - 1]] -= 1
            if (slide[s[i - 1]]) == 0:
                del slide[s[i - 1]]
            # Add next
            next_letter = s[i + length - 1]
            
            if not slide.get(next_letter):
                slide[next_letter] = 1
            else:
                slide[next_letter] += 1
                
            if slide == dict_p:
                anagrams_index.append(i)
        
        return anagrams_index
        
sol = Solution()
s = 'cbaebabacd'
p = 'abc'

print(sol.findAnagrams(s,p))