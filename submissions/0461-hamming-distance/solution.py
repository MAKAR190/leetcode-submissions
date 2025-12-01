class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        diff = x ^ y
        
        while diff:
            count += diff & 1
            diff >>= 1
            
            
        return count
