# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num == 6:
        return 0
    elif num < 6:
        return 1
    elif num > 6:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        g = None
        top = n
        low = 0
        mid = n // 2
        while g != 0:
            g = guess(mid)

            if g < 0:
                mid, top = low + ((top - mid) // 2), mid
            elif g > 0:
                mid, low =  top - ((top - mid) // 2), mid
        return mid

s = Solution()
res = s.guessNumber(10)
print(res)