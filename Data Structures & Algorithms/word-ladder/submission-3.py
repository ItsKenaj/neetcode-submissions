from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (beginWord == endWord or endWord not in wordList):
            return 0
        
        words = set(wordList)
        res = 0
        queue = deque([beginWord])
        while queue:
            res += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return res

                for i in range(len(cur)):
                    for c in range(97, 123):
                        next_word = cur[:i] + chr(c) + cur[i+1:]
                        if next_word in words:
                            words.remove(next_word)
                            queue.append(next_word)

        
        return 0
