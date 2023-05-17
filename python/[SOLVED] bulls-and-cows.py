'''You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. 
When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are 
located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged 
such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
Note that both secret and guess may contain duplicate digits.'''

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        numbers = {}
        positions = {}
        
        for i, char in enumerate(secret):
            numbers.setdefault(char, 0)
            numbers[char] += 1
            
            positions[i] = char
            
        # print(numbers)
        # print(positions)
        
        a = 0 # Bull - correct number & position
        b = 0 # Cow - correct number & wrong position
        
        cows = {}
        # print(numbers)
        
        for i, char in enumerate(guess):
            
            if numbers.get(char, 0) > 0:
                # b += 1
                cows.setdefault(char, 0)
                cows[char] += 1
                numbers[char] -= 1
            
        # print(cows)
        for i, char in enumerate(guess):
            
            if positions[i] == guess[i]:
                a += 1
                cows[char] -= 1
            
        b = sum(cows.values())
        
        return str(a) + 'A' + str(b) + 'B' 
        
s = Solution()
secret = "18077"
guess = "78107"

print(s.getHint(secret,guess))