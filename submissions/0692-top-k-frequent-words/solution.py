from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = []
        n = len(words)
        counts = Counter(words)

        buckets = [[] for _ in range(n + 1)]

        for key, value in counts.items():
            buckets[value].append(key)
        
        for i in range(n, 0, -1):
            buckets[i].sort()

            for word in buckets[i]:
                ans.append(word)
                if len(ans) == k:
                    return ans
