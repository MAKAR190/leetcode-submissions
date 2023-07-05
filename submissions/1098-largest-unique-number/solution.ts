function largestUniqueNumber(nums: number[]): number {
  const map = new Map();
  let max:number = 0;  
  let passed:boolean = true;  
  for(let i = 0; i < nums.length; i++){
      map.set(nums[i], (map.get(nums[i]) || 0) + 1);
  }  
    
   for(const [key,value] of map){
       if(value > 1){
           passed = false;
       } else {
           passed = true;
           max = Math.max(max, key)
       }
   } 
    if(passed) {
      return max;
    }
    
return -1;
};
