function longestOnes(nums: number[], k: number): number {
  let left:number = 0;
  let curr:number = 0;
  let ans:number = 0;
  for(let i = 0; i < nums.length; i++) {
      
      if(nums[i] == 0 ) {
          curr += 1
      }
      
     while (curr > k) {
      if (nums[left] === 0) {
        curr -= 1;
      }
      left += 1;
    }

    ans = Math.max(ans, i - left + 1);
      
  }
   return ans;
};
