class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0;
        int right = s.size() - 1;
        
        while(left < right){
            s.insert(s.begin() + left, s[right]);
            s.erase(s.end());
            
            left++;
        }
    }
};
