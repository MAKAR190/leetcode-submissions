class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = [""]

        for part in path.split("/"):
            
              if part == "" or part == ".":
                continue
        
              elif part == "..":
                if len(directories) == 1:
                    continue
                else:    
                    directories.pop()
              
              else:
                directories.append(part) 
        
        if len(directories) == 1:
            directories.append("")
        
        return "/".join(directories)
