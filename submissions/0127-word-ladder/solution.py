from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def differs_by_one(str1, str2):
            differs = 0

            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    differs += 1
            
            return differs == 1
           
        wordSet = set(wordList)
        queue = deque([beginWord])
        seen = set()
        ans = 1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == endWord:
                    return ans
            
                for word in wordSet:
                    if word not in seen and differs_by_one(word, node):
                        seen.add(word)
                        queue.append(word)
                    
            ans += 1

        return 0
