class Solution {
public:
    vector<int> sortedSquares(vector<int>& vec) {
        for (int& num : vec) {
            num = num * num; 
        }

        // Perform bubble sort
        int n = vec.size();
        bool swapped;

        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            for (int j = 0; j < n - i - 1; j++) {
                if (vec[j] > vec[j + 1]) {
                    std::swap(vec[j], vec[j + 1]);
                    swapped = true;
                }
            }

            if (!swapped)
                break;
        }
        
        return vec; 
    }
};

