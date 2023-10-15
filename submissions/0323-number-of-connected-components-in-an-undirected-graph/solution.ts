function countComponents(n: number, edges: number[][]): number {
   
  let graph = new Map();  
  let seen = new Array(n).fill(false);
    
  for(let i = 0; i < n; i++){
      graph.set(i, []);
  }
  
  for(const [x, y] of edges){
      graph.get(x).push(y);
      graph.get(y).push(x);
  }  
    
  let dfs = node => {
      for(const neighbour of graph.get(node)){
          if(!seen[neighbour]){
              seen[neighbour] = true;
              dfs(neighbour);
          }
      }
  }
  
  let ans = 0;
    
  for(let i = 0; i < n; i++){
      if(!seen[i]){
         ans+=1
         seen[i]=true
         dfs(i); 
      }
  }  
  
  return ans;  
};
