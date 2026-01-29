class Trie:
    END_CHARACTER = "*"
    
    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        root = self
        
        for c in word:
            if c not in root.children:
                root.children[c] = Trie()
                
            root = root.children[c]
            
        root.children[self.END_CHARACTER] = True

    def search(self, word: str) -> bool:
        root = self
        
        for c in word:
            if c not in root.children:
                return False
                
            root = root.children[c]
            
        return self.END_CHARACTER in root.children

    def startsWith(self, prefix: str) -> bool:
        root = self
        
        for c in prefix:
            if c not in root.children:
                return False
                
            root = root.children[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
