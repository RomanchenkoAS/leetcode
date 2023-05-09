class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        for char in s:
            if map[char]:
                map[char] += 1
            else:
                map[char] = 1
        
        length = 0
        has_odd = False
        for char in map.keys():
            if map[char] % 2 == 0:
                length += map[char]
            else:
                length += (map[char] - 1) / 2
                if not has_odd:
                    length += 1
                    has_odd = True
            
            
        return length
    
    
s = Solution()

# input = [7,1,5,3,6,4]
input = [1,4,2]
# input = [3,2,6,5,0,3]

print(s.maxProfit(input))