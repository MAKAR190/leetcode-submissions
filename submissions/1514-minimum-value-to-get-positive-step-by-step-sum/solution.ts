function minStartValue(nums: number[]): number {
   let startValue:number = 1;
    while(true){
        let isValid:boolean = true;
        let total = startValue;
        for(const num of nums){
            total += num
            if(total < 1){
                isValid = false;
                break;
            }
        }
         if (isValid) {
            return startValue;
        } else {
            startValue += 1;
        }  
    }
   
        
 return startValue;
};
