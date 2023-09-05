class MovingAverage {
    private size: number;
    private queue: number[];

    constructor(size: number) {
         this.size = size;
         this.queue = [];
    }

    next(val: number): number {
       let result = 0;
       if(this.queue.length >= this.size){
         this.queue.shift();
       }
        this.queue.push(val);
        result = this.queue.reduce((acc, el)=> acc += el, 0) / this.queue.length;
        return result;
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */
