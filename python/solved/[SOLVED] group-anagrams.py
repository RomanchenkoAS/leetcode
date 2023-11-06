"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once."""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # # List of lists with strings
        # result = []
        
        # # List of dictionaries
        # maps = []
        # for str in strs:
        #     charmap = {}
        #     for char in str:
        #         if char in charmap:
        #             charmap[char] += 1
        #         else:
        #             charmap[char] = 1
                
        #     if charmap in maps:
        #         index = maps.index(charmap)
        #         result[index].append(str)
        #     else:
        #         maps.append(charmap)
        #         result.append([str])
                
        # return result
        
        # Better hasmap method
        dict = {}
        
        for string in strs:
            s = str(sorted(string))
            if s in dict:
                dict[s].append(string)
            else:
                dict[s] = [string]
            
        return dict.values()