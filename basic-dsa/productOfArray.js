// recursion problem

// Write a function called productOfArray which takes in an array of numbers and returns the product of them all.

function productOfArray(arr) {
    if(arr.length === 0) {
        return 1;
    }
    return arr[0] * productOfArray(arr.slice(1));
}

function print(x){
console.log(x);

}

productOfArray([1,2,3])    // 6
productOfArray([1,2,3,10]) // 60

//  node basic-dsa/productOfArray.js
