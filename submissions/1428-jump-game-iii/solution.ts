function canReach(arr: number[], start: number): boolean {
    
   if (start < 0 || start >= arr.length || arr[start] === 0) {
    return true; 
  }
   let queue = [start];
   let seen = new Set();
    seen.add(start);
    
   while(queue.length){
     let newQueue = [];
     let currentLength = queue.length;
     
     for(let i = 0; i < currentLength; i++){
         let currentIndex = queue[i];
         for(const nextIndex of [currentIndex + arr[currentIndex], currentIndex - arr[currentIndex]]){
         if(nextIndex >= 0 && nextIndex < arr.length){
             if(arr[nextIndex] === 0){
                 return true;
             }
             
             if (!seen.has(nextIndex)) {
            newQueue.push(nextIndex);
            seen.add(nextIndex);
          }
         }
     }  
   }
              queue = newQueue;

}  
    
    return false;
};
