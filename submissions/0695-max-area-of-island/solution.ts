function maxAreaOfIsland(grid: number[][]): number {
  let m = grid.length;
  let n = grid[0].length;
  let seen = [];
  let max = 0;  
    
  for(let i = 0; i < m; i++){
      seen.push(new Array(n).fill(false));
  }  
    
  let valid = (row, col) => {
      return row >= 0 && col >= 0 && row < m && col < n && grid[row][col] == 1;
  }
   
  let directions = [[0,1],[1,0],[0,-1],[-1,0]];
    
  let dfs = (row, col) => {
      let temp = 1; 
      for(const [dx, dy] of directions){
          let nextRow = row + dy;
          let nextCol = col + dx;
          if(valid(nextRow, nextCol) && !seen[nextRow][nextCol]){
              seen[nextRow][nextCol] = true;
              temp += dfs(nextRow, nextCol);
          }   
    } 
          
   return temp; 
  }  
      
  
  for(let row = 0; row < m; row++){
      for(let col = 0; col < n; col++){
          if(!seen[row][col] && grid[row][col] == 1){
              seen[row][col] = true;
              max = Math.max(max, dfs(row, col));
          }
      }
  }
  
  return max;  
  
};
