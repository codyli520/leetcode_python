class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]

            for j in range(min(len(word_1), len(word_2))):
                if order_index[word_1[j]] < order_index[word_2[j]]:
                    break
                elif order_index[word_1[j]] == order_index[word_2[j]]:
                    continue
                else:
                    if order_index[word_1[j]] > order_index[word_2[j]]:
                        return False
            else:
                if len(word_1) > len(word_2):
                    return False

        return True

