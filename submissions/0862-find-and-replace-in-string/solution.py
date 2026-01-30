# indices: [0, 2]

# sources: ["a", "cd"]

# targets = ["eee", "ffff"]

# s = abcd

# How wo de create an output: "eeebcd"?
# O(n+k)

# abcd
# eeebffff

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:       
            replacements = sorted(zip(indices, sources, targets))
            res = []
            i = 0
            r = 0
            
            while i < len(s):
                if r < len(replacements) and i == replacements[r][0]:
                    _, source, target = replacements[r]
                    
                    if s[i:i+len(source)] == source:
                        res.append(target)
                        i += len(source)
                        
                    r += 1
                else:
                    res.append(s[i])
                    i += 1
            
            return "".join(res)
