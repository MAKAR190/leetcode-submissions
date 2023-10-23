function minMutation(startGene: string, endGene: string, bank: string[]): number {
   const getNeighbors = gene => {
       let ans = [];
       for (let i = 0; i < gene.length; i++) {
       for(const char of ['A', 'C', 'G', 'T']){
         let neighbor = gene.split(''); 
         neighbor[i] = char;
         ans.push(neighbor.join('')); 
         }
        }     
       return ans;
   }
   
   let queue = [startGene];
   let seen = new Set();
   let steps = 0;
   
   while(queue.length){
       let newQueue = [];
       let currentLength = queue.length;
       
       for(let i = 0; i < currentLength; i++){
            let gene = queue[i];
           if(gene == endGene){
               return steps;
           }
           for(const neighbor of getNeighbors(gene)){
               if(!seen.has(neighbor) && bank.includes(neighbor)){
                   seen.add(neighbor);
                   newQueue.push(neighbor);
               }
           }
       }
       queue = newQueue;
       steps++;
   }  
   return -1;
};
