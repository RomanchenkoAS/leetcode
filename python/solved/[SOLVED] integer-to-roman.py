class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]

        t = num // 1000
        h = (num - 1000 * (num // 1000)) // 100
        d = (num - 100 * (num // 100)) // 10
        o = num % 10
        return thousands[t] + hundreds[h] + tens[d] + ones[o]

num = 1994
s = Solution()
print(s.intToRoman(num))