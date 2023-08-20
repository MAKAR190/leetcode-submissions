function numJewelsInStones(jewels: string, stones: string): number { 
  let count:number = 0;
  const jewelsMap = new Map();
    
    for (const jewel of jewels){
        jewelsMap.set(jewel, (jewelsMap.get(jewel) || 0) + 1);
    }
    
    for(const stone of stones){
        if(jewelsMap.has(stone)){
            count += 1
        }
    }
    
    return count;
};
