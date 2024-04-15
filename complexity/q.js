// https://rithmschool.github.io/function-timer-demo/
// https://cs.slides.com/colt_steele/big-o-notation
// https://cs.slides.com/colt_steele/built-in-data-structures-25#/3/0/2
// https://cs.slides.com/colt_steele/problem-solving-patterns

let n = 5;
let m = 5;
for (let i = 1; i < n; i *= 2) {
    // console.log(i);
}
// Here the loop will run (log n)-1 times
// 1st iteration, i = 1
// 2nd iteration, i = 2
// 3rd iteration, i = 4
// 4th iteration, i = 8
// ….
// kth iteration, i = 2 ^ (k-1)
// So, 2 ^ (k-1) < n
// now taking log on both sides
// log (2 ^ (k-1)) < log n
// k-1 = log n
// Time Complexity: O(log n)
// space Complexity: 

const arr = [];
for (let i = 0; i < n; ++i) {
    arr.push(i);
}

// Here the array will take n space
// Space Complexity: O(n)
// Time Complexity: 

for (let i = 0; i < n; ++i) {
    for (let j = 0; j < n; ++j) {
        // console.log(i, j);
    }
}
// Time Complexity: 
// space Complexity: 



const arr1 = [];
for (let i = 0; i < n; ++i) {
    for (let j = 0; j < n; ++j) {
        arr1.push(i + j);
    }
}
// Here the array will take n² space
// Space Complexity: O(n²)
// Time Complexity: 

let a = 0, b = 0;
for (let i = 0; i < n; ++i) {
    a = a + i;
}
for (let j = 0; j < m; ++j) {
    b = b + j;
}
// time Complexity: O(n +m)
// Space Complexity: O(1)


let a1 = 0, b1 = 0;
for (let i = 0; i < n; ++i) {
    for (let j = 0; j < n; ++j) {
        a1 = a1 + j;
    }
}
// time Complexity: 
// Space Complexity: 

for (let k = 0; k < n; ++k) {
    b = b + k;
}

// Time Complexity: O(n²)
// Space Complexity: O(1)

let a2 = 0;
for (let i = 0; i < n; ++i) {
    for (let j = n; j > i; --j) {
        a2 = a2 + i + j;
    }
}
// time Complexity: O(n²)
// Space Complexity: O(1)
