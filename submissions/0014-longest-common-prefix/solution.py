# "fl o w e r", "fl o w", "fl i g h t"]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = {}
        ans = ""

        if "" in strs or not strs:
            return ""

        for str in strs:
            node = trie

            for ch in str:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]  

            node["#"] = True

        node = trie

        while True:
            if '#' in node:
                break
            children = [key for key in node.keys() if key != "#"]
            if len(children) == 1:
                ans += children[0]
                node = node[children[0]]
            else:
                break    

        return ans
