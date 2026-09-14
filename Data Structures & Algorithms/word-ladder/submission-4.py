class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (beginWord == endWord or endWord not in wordList):
            return 0

        words = set(wordList)
        queue = collections.deque([beginWord])
        res = 0

        while queue:
            res += 1
            for _ in range(len(queue)): # we do this because every time we get to the start of the while that means we have added the candidates that are all one letter different that the previous iteration. Otherwise we would increment result for every candidate in the queue across the boundary of single letter change -- inflated number
                cur = queue.popleft()
                if cur == endWord:
                    return res
                for i in range(len(cur)):
                    for c in range(97, 123):
                        if cur[i] == chr(c):
                            continue
                        word = cur[:i] + chr(c) + cur[i + 1:]
                    
                        if word in words:
                            words.remove(word)
                            queue.append(word)
                
        return 0

