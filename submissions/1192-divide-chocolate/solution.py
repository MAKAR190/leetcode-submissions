# Target: maximum sweetness based on k cuts
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int: 
        def check(target):
            curr_sweetness = 0
            curr_number_of_people = 0
            
            for s in sweetness:
                curr_sweetness += s
                
                if curr_sweetness >= target:
                    curr_sweetness = 0
                    curr_number_of_people += 1
            
            return curr_number_of_people >= k + 1
        
        left = min(sweetness)
        right = sum(sweetness) // (k + 1)
        
        while left < right:
            mid = (left + right + 1) // 2
            
            if check(mid):
                left = mid
            else:
                right = mid - 1
                
        return left
