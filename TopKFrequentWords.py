class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_hash = {}
        for word in words:
            if word in word_hash:
                word_hash[word] += 1
            else:
                word_hash[word] = 1
        
        freq = {}
        for key,value in word_hash.items():
            if value in freq:
                freq[value].append(key)
            else:
                freq[value] = [key]
        
        res = []
        for i in range(len(words),0,-1):
            if i in freq:
                res.extend(sorted(freq[i]))
        
        return res[:k]