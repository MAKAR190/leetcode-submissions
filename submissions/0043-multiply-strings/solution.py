class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 1. Convert to a list of digits using unicode manipulation (from "123", "456" -> [1, 2, 3], [4, 5, 6])
    
        # 2. Do multiplication digit by digit, without ever forming the full number (and handle carry)
        # 3. Multiply and join to a string
        
        num1 = [ord(digit) - ord('0') for digit in num1]
        num2 = [ord(digit) - ord('0') for digit in num2]
        
        n, m = len(num1), len(num2)
        
        result = [0] * (n + m)
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                result[i + j + 1] += num1[i] * num2[j]
        
        carry = 0
        for i in range(len(result) - 1, -1, -1):
            total = result[i] + carry
            result[i] = total % 10
            carry = total // 10
        
        starting_point = 0
        while result[starting_point] == 0 and starting_point + 1 != len(result):
            starting_point += 1
        
       
        return "".join(str(digit) for digit in result[starting_point:])
            
