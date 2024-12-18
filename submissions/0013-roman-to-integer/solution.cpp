#include <map>
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> romToIntMap = {
            {'I', 1},
            {'V', 5},
            {'X', 10}, 
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int total = 0;

        for (int i = 0; i < s.size(); i++){
            int current = romToIntMap[s[i]];
            int next = (i + 1 < s.size()) ? romToIntMap[s[i+1]] : 0;

            if (current < next) {
                total -= current;
            } else {
                total += current;
            }
        }

        return total;
    }
};
