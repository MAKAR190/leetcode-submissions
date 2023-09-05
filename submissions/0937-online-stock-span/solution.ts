class StockSpanner {
    private stack: number[];

    constructor() {
     this.stack = [];
    }

    next(price: number): number {
      let days = 1;
      let popped = [];
      while(this.stack.length > 0 && price >= this.stack[this.stack.length - 1]){
         let j = this.stack.pop();
         popped.push(j);
         days += 1;
      }  
      
      for (let i = 0; i < popped.length; i++){
         this.stack.push(popped[i]); 
      }           
     this.stack.push(price);       
   
     return days;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */
