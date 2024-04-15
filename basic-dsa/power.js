// recursion problem

// Write a function which accepts a base an an exponent.  It should return the result of raising the base to that exponent.

function power(base, exponent){
    if(exponent === 0) return 1;
    return base * power(base,exponent-1);
}

function print(x){
console.log(x);

}

power(2,4) //16
power(3,2) //9
power(3,3) //27

//  node basic-dsa/power.js
