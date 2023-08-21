function lengthOfLongestSubstring(s: string): number {
    let dic = new Map();
    let maxLength = 0;
    let start = 0;

    for (let i = 0; i < s.length; i++) {
        if (dic.has(s[i]) && dic.get(s[i]) >= start) {
            start = dic.get(s[i]) + 1;
        }
        dic.set(s[i], i);
        maxLength = Math.max(maxLength, i - start + 1);
    }

    return maxLength;
    
};
