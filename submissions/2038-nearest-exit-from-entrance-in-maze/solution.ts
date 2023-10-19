function nearestExit(maze: string[][], entrance: number[]): number {
   const valid = (row, col) =>{
       return row >= 0 && col >= 0 && row < m && col < n && maze[row][col] == "."; 
   } 
   
   let steps = -1;
   let queue = [entrance];
   let seen = [];
   let m = maze.length;
   let n = maze[0].length;
   const directions = [[0,1], [1,0], [0,-1], [-1,0]];
    
   for(let i = 0; i < m; i++){
       seen.push(new Array(n).fill(false));
   } 
    
   while(queue.length){
     let currentLength = queue.length;
     let newQueue = [];
     steps++;
       
     for(let i = 0; i < currentLength; i++){
         let [row, col] = queue[i];
      
          if (row != entrance[0] || col != entrance[1]) {  
             if (row === 0 || row === m - 1 || col === 0 || col === n - 1) {
                 return steps;  
             }
         }
         
         for(const [dx, dy] of directions){
             let nextRow = row + dy;
             let nextCol = col + dx;
             
             if(valid(nextRow, nextCol) && !seen[nextRow][nextCol]){
                 seen[nextRow][nextCol] = true;
                 newQueue.push([nextRow, nextCol]);
             }
         }
     }  
     queue = newQueue; 
   } 
   
   return -1; 
};
