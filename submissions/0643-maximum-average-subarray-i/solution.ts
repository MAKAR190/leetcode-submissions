function findMaxAverage(nums: number[], k: number): number {
    let ans = 0;
    let curr = 0;
    
    for (let i = 0; i < k; i++){
        curr += nums[i]
    }
      ans = curr;

    for (let i = k; i < nums.length; i++){
        curr += nums[i] - nums[i - k]
        ans = Math.max(ans, curr);
    }

    return ans / k;
};
