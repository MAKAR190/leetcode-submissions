/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    let left:number = 0;
 for(let right = s.length - 1; right>=left; right--){
     let temp:string = s[left]
     s[left] = s[right]
     s[right] = temp
     left++
 }   
};
