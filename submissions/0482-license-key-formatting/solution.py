class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        letters = s.replace("-", "").upper()
        n = len(letters)
        first = n % k or k
        
        ans = [letters[:first]]
        for i in range(first, n, k):
            ans.append(letters[i:i+k])
            
        return "-".join(ans)
