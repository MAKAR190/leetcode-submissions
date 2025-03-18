class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        vector<int> result(nums.size()); 
        int index = nums.size() - 1;    

        while (left <= right) {
            int lel = nums[left] * nums[left];
            int rel = nums[right] * nums[right];

            if (lel > rel) {
                result[index] = lel;
                left++;
            } else {
                result[index] = rel;
                right--;
            }
            
            index--; 
        }

        return result;
    }
};

