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

        # SLIDING WINDOW!!

        # We take first symbol (A) and start to build a string of a same character from it
        # If next is A we add it to length
        # If next is B we decrease k (k = k - 1) and add it to length
        # If next is B and we have no more k, we save current length and start counting a new sliding string from FIRST B
        # Stop at the last character in a string

        i = 1
        length = 1
        length_based = 0
        current = s[0]
        k_left = k
        first_different = None

        while i < len(s):
            if s[i] == current:
                length += 1
            else:
                # Remember where the first different letter was
                if not first_different:
                    first_different = i

                k_left -= 1
                if k_left >= 0:
                    length += 1
                else:
                    if length > length_based:
                        length_based = length
                    length = 1
                    current = s[first_different]
                    i = first_different + 1
                    first_different = None
                    k_left = k
                    continue
            i += 1

        if length > length_based:
            length_based = length

        l1 = length_based
        
        s = s[::-1]
        i = 1
        length = 1
        length_based = 0
        current = s[0]
        k_left = k
        first_different = None

        while i < len(s):
            if s[i] == current:
                length += 1
            else:
                # Remember where the first different letter was
                if not first_different:
                    first_different = i

                k_left -= 1
                if k_left >= 0:
                    length += 1
                else:
                    if length > length_based:
                        length_based = length
                    length = 1
                    current = s[first_different]
                    i = first_different + 1
                    first_different = None
                    k_left = k
                    continue
            i += 1

        if length > length_based:
            length_based = length
            
        l2 = length_based
        
        return max(l1, l2)


s = Solution()

# input = 'AABABBA'
input = 'ABBB'

print(s.characterReplacement(input, 2))
