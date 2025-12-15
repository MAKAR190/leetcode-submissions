class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        chars = []

        def join_me(chars_arr):
            ans = ""
            for i in range(len(chars_arr)):
                ans += chars_arr[i]
            return ans

        def reverse_me(chars_arr):
            left = 0
            right = len(chars_arr) - 1

            while left < right:
                temp = chars_arr[left]
                chars_arr[left] = chars_arr[right]
                chars_arr[right] = temp

                left += 1
                right -= 1

            return chars_arr

        while x > 0:
            digit = x % 10
            chars.append(chr(ord('0') + digit))
            x //= 10
        
        return join_me(chars) == join_me(reverse_me(chars))



