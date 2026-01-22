from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        words = set(wordList)
        steps = 1
            
        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)
            
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return steps
                    
                for i in range(len(curr)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == curr[i]:
                            continue
                            
                        new_curr = curr[:i] + c + curr[i+1:]
                        if new_curr in words:
                            queue.append(new_curr)
                            words.remove(new_curr)    
                    
            steps += 1
            
        return 0
        
