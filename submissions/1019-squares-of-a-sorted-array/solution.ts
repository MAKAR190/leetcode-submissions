function sortedSquares(nums: number[]): number[] {
   let ans: number[] = []; 
   let left:number = 0;
   let right:number = nums.length - 1;
for(let i = nums.length - 1; i>=0; i--){
    let square;
    if(Math.abs(nums[left]) < Math.abs(nums[right])){
        square = nums[right]
        right--;
    }else{
        square = nums[left];
        left++
    }
    ans.unshift(square * square)
}
  
    return ans;
};
