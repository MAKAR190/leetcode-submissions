# Edge cases
# 1.Sometimes you don't need to use a change

# Approach
# We don't need to replace 9s with 6s, only 6s with 9s to get the largest element and when they are all nines we don't need to change anything

# 

class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        
        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break
        
        return int(''.join(map(str, digits)))
