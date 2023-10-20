function snakesAndLadders(board: number[][]): number {
  let graph = new Map();
  let seen = new Set();
  let n = board.length;
  let square = 1;
  let queue = [[1, 0]]; 
  
  seen.add(1);  
    
  for(let i = n - 1; i >= 0; i--){
      if((n - i) % 2 == 1){
         for (let j = 0; j < n; j++) {
                graph.set(square, [i, j]);
                square++;
            }
      } else {
            for (let j = n - 1; j >= 0; j--) {
                graph.set(square, [i, j]);
                square++;
            }
      }
  }  
    
      const getNeighbors = (square) => {
        const neighbors = [];
        for (let dice = 1; dice <= 6; dice++) {
            const nextSquare = square + dice;
            if (nextSquare <= n * n) {
                const [r, c] = graph.get(nextSquare);
                if (board[r][c] === -1) {
                    neighbors.push(nextSquare);
                } else {
                    neighbors.push(board[r][c]);
                }
            }
        }
        return neighbors;
    };  
    
    while(queue.length){
        const [square, moves] = queue.shift();
        for(const neighbor of getNeighbors(square)){
            if(neighbor === n * n){
                return moves + 1;
            }
            if(!seen.has(neighbor)){
                queue.push([neighbor, moves + 1]);
                seen.add(neighbor);
            }
        }
    }
    
    return -1;
};
