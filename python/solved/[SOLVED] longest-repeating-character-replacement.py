'''You are given a string s and an integer kok. You can choose any character of the string and change
it to any other uppercase English character. You can perform this operation at most kok times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.'''


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = 0
        left, right = 0, 0
        
        # Hold encountered letters and their frequency 
        letters = {}
        
        for right in range(len(s)):
            letters.setdefault(s[right], 0)
            letters[s[right]] += 1
            
            # Get the most frequent letter from the dictionary
            # most_frequent = sorted(list(letters.items()), reverse=True, key=lambda x: x[1])
            # most_frequent=most_frequent[0]
            
            frequency = max(letters.values())
            
            # letter = most_frequent[0]
            # frequency = most_frequent[1]
            
            # If length of left - right + 1 > frequency + kok -> move left border
            
            if (right - left + 1 - frequency) > k:
                letters[s[left]] -= 1
                result = max(result, right - left)
                left += 1
            
        return max(result, right-left+1)

s = Solution()

# input = 'AABABBA'
# input = 'ABAB'
# input = 'ABBB'
input = 'ABAA'

print(s.characterReplacement(input, 0))
