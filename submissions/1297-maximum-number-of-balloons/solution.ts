function maxNumberOfBalloons(text: string): number {
   let total:number = Infinity;
   let word:string = "balloon"; 
    let count = new Map();
   for(let i = 0; i < text.length; i++){
       count.set(text[i], (count.get(text[i]) || 0) + 1);
       
   } 
    
 for (let char of word) {
        if (!count.has(char)) {
            return 0;
        }

        total = Math.min(total, Math.floor(count.get(char) / (char === 'l' || char === 'o' ? 2 : 1)));
    }

    return total;
    
};
