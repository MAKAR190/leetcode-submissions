class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        
        for character in sentence:
            if character in s: 
                continue

            s.add(character)
            
        return len(s) == 26
