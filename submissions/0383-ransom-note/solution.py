from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countsNote = Counter(ransomNote)
        countsMagazine = Counter(magazine)
       
        for ch, count in countsNote.items():
            if ch in countsMagazine:
                if count > countsMagazine[ch]:
                    return False
            else:
                 return False
    
        return True
        
        
