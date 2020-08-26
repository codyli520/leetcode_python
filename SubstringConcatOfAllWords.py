class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        res = []

        if not words or not s:
            return res

        word_len = len(words[0])

        sentense_len = word_len * len(words)

        w_count = Counter(words)
        for i in range(len(s) - sentense_len + 1):
            word_used = 0
            count = dict(w_count)

            for j in range(i, i + sentense_len, word_len):
                word = s[j:j + word_len]
                if word in count and count[word] > 0:
                    count[word] -= 1
                    word_used += 1
                else:
                    break

            if word_used == len(words):
                res.append(i)

        return res

