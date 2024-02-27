class Solution(object):
    def reverseString(self, s):
        right = len(s) - 1
        left = 0
        while left < right:
            temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left += 1;
            right -= 1;
            
        return s;
