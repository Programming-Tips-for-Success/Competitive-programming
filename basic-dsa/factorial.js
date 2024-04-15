// recursion problem


function factorial(x){
   if (x < 0 ) return 0;
   if (x <= 1 ) return 1;
   return x * factorial(x-1);
}
function print(x){
console.log(x);

}

print(factorial(5))

// node basic-dsa/factorial.js
