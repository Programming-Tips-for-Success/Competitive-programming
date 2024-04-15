// Given a sorted array of integers, write a function called search, that accepts a value and returns the index where the value passed to the function is located. If the value is not found, return -1

// Linear Search


// function search(arr, val){
//     for(let i = 0; i < arr.length; i++){
//         if(arr[i] === val){
//             return i;
//         }
//     }
//     return -1;
// }
// Time Complexity O(N)

// try the linear search with indexof

// divide and conquer approach

function search(array, val) {
 
    let min = 0;
    let max = array.length - 1;
 
    while (min <= max) {
        let middle = Math.floor((min + max) / 2);
        let currentElement = array[middle];
 
        if (array[middle] < val) {
            min = middle + 1;
        }
        else if (array[middle] > val) {
            max = middle - 1;
        }
        else {
            return middle;
        }
    }
 
    return -1;
}
// Time Complexity - Log(N) - Binary Search!
// Binary search is a much faster form of search
// Rather than eliminating one element at a time, you can eliminate half of the remaining elements at a time
// Binary search only works on sorted arrays!

function print(x){
console.log(x);

}
print(search([1,2,3,4,5,6],4)) // 3
print(search([1,2,3,4,5,6],6)) // 5
print(search([1,2,3,4,5,6],11)) // -1

// node basic-dsa/search