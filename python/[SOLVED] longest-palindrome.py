class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
        
        length = 0
        has_odd = False
        for char in map.keys():
            if map[char] % 2 == 0:
                length += map[char]
            else:
                length += map[char] - 1
                if not has_odd:
                    length += 1
                    has_odd = True
            
            
        return length
    
    
s = Solution()

# input = "abccccdd"
input = "ccc"

print(s.longestPalindrome(input))