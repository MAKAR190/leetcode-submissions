class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # [10,13,12,14,15] = [0, 1, 2, 3, 4] - > [10,12,13,14,15] = [0, 2, 1, 3, 4]
        
        n = len(arr)
        indices = list(range(n))
        even_next = [None] * n
        odd_next = [None] * n
        
        sorted_odd_indices = sorted(indices, key=lambda x: (arr[x], x))
        sorted_even_indices = sorted(indices, key=lambda x: (-arr[x], x))
        
        stack = []
        
        # odd_next precomputation
        for i in sorted_odd_indices:
            while len(stack) > 0 and stack[-1] < i:
                odd_next[stack[-1]] = i
                stack.pop()
            stack.append(i)
        
        # clean stack
        while len(stack) > 0:
            stack.pop()
        
        # even_next precomputation
        for i in sorted_even_indices:
            while len(stack) > 0 and stack[-1] < i:
                even_next[stack[-1]] = i
                stack.pop()
            stack.append(i)
        
        def dp(i, odd):
            if i == n - 1:
                return True
            
            if (i, odd) in memo:
                return memo[(i, odd)]
            
            memo[(i, odd)] = False
            
            if odd:
                if odd_next[i] != None:
                    memo[(i, odd)] = dp(odd_next[i], False)
            
            if not odd:
                if even_next[i] != None:
                    memo[(i, odd)] = dp(even_next[i], True)
            
            return memo[(i, odd)]
            
        memo = {}
        return sum(dp(i, True) for i in range(n))
        
        
