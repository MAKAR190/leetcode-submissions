function reachableNodes(n: number, edges: number[][], restricted: number[]): number {
  const graph = new Map();
  const visited = new Array(n).fill(false);
  let ans = 0;

  for (let i = 0; i < n; i++) {
    graph.set(i, []);
  }

  for (const [x, y] of edges) {
    graph.get(x).push(y);
    graph.get(y).push(x);
  }
   
  for(const node of restricted){
      visited[node] = true;
  }  

  const dfs = (node) => {
    ans+=1
    visited[node] = true
     
    for(const edge of graph.get(node)){
        if(!visited[edge]){
            dfs(edge);
        }
    }
  };

  dfs(0);

  return ans;
};
