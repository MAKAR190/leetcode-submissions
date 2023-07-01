function getAverages(nums: number[], k: number): number[] {
  if (k === 0){
      return nums;
  }
  
  let avgs = new Array(nums.length).fill(-1);  
   
   if(2*k +1 > nums.length){
       return avgs;
   } 
   
   let windowSum = 0;
   for (let i = 0; i < 2*k+1; i++){
       windowSum += nums[i]
   }
   
   avgs[k] = Math.floor(windowSum / (2*k + 1));
    
   for (let i = 2*k + 1; i < nums.length; i++){
       windowSum = windowSum - nums[i - 2*k - 1] + nums[i];
       avgs[i - k] = Math.floor(windowSum / (2*k + 1));
   } 
    
   return avgs; 
};
