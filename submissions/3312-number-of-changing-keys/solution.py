class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        n = len(s)

        for i in range(1, n):
            if s[i - 1].lower() != s[i].lower():
                changes += 1

        return changes 
