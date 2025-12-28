class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = left = 0
        n = len(height)
        right = n - 1
        
        while left < right:
            h_r, h_l = height[right], height[left]
            container_height, container_width = min(h_r, h_l), right - left
            
            ans = max(ans, container_height * container_width)
            
            if h_r >= h_l:
                left += 1
            else:
                right -= 1
        
        return ans
        
        
