from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord == beginWord or endWord not in wordList):
            return 0
        
        words = set(wordList)
        count = 0
        queue = deque([beginWord])
        while queue:
            count += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return count
                for i in range(len(cur)):
                    for c in range(97, 123):
                        word = cur[:i] + chr(c) + cur[i+1:]
                        if word in words:
                            queue.append(word)
                            words.remove(word)
        return 0
