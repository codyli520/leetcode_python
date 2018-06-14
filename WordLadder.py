class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        
        if beginWord in wordList:
            wordList.remove(beginWord)
        
        queue = collections.deque([(beginWord, 1)])
        while queue:
            cur, level = queue.popleft()
            for i in range(len(cur)):
                # 对于当前单词的每一个字母，替换成新的字母，并检查是否是endword 或者在 wordList里
                for c in [chr(i) for i in range(ord('a'), ord('z')+1)]:
                    trans = cur[:i] + c + cur[i+1:]
                    # 发现结束单词
                    if trans == endWord:
                        return level + 1
                    # 未发现结束单词，但是在wordList,放在下一层
                    elif trans in wordList:
                        queue.append((trans, level + 1))
                        wordList.remove(trans)
                        
        return 0