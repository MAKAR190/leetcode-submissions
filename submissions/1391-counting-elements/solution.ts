function countElements(arr: number[]): number {
  const map = new Map(); 
  let ans:number = 0;
    
  for (let i = 0; i < arr.length; i++) {
    const num = arr[i];
    map.set(num, (map.get(num) || 0) + 1);
  }
    
  for(let i = 0; i < arr.length; i++){
      if(map.has(arr[i] + 1)) {
         ans += 1
      }
  }
  return ans;  
};
