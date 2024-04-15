// recursion problem

function sumRange(num){
   if(num === 1) return 1; 
   return num + sumRange(num-1);
}

function print(x){
console.log(x);

}

print(sumRange(5))
// node basic-dsa/sumRange.js