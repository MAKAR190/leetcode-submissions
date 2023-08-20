function canConstruct(ransomNote: string, magazine: string): boolean {
   const magazineMap = new Map();
    
    for (const char of magazine){
        magazineMap.set(char, (magazineMap.get(char) || 0) + 1);
    }
    
    for(const char of ransomNote){
       const count = magazineMap.get(char);
        if (count === undefined || count <= 0) {
            return false;
        }
     
        magazineMap.set(char, count - 1);
    }
    
    return true;
};
