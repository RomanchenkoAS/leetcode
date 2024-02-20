"""Given an array of strings words and an integer kok, return the kok most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the 
same frequency by their lexicographical order."""


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        
        for word in words:
            # d.setdefault(word, 0)
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        
        items_list = sorted(list(d.items()), key=lambda x: (-x[1], x[0]))

        return [items_list[i][0] for i in range(k)]


s = Solution()

# words = ["i", "love", "leetcode", "i", "love", "coding"]
# words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
words = ["aaa","aa","a"]
k = 1

print(s.topKFrequent(words=words, k=k)) 
