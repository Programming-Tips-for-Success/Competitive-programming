for (let i = 1; i < n; i *= 2) {
    console.log(i);
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
        console.log(i, j);
    }
}
// Time Complexity: 
// space Complexity: 

function fibonacci(n) {
    const arr = [0, 1];
    for (let i = 2; i <= n; ++i) {
        arr.push(arr[i - 2] + arr[ i - 1]);
    }
    return arr[n - 1];
}

// Time Complexity: 
// space Complexity: 

const arr = [];
for (let i = 0; i < n; ++i) {
    for (let j = 0; j < n; ++j) {
        arr.push(i + j);
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


let a = 0, b = 0;
for (let i = 0; i < n; ++i) {
    for (let j = 0; j < n; ++j) {
        a = a + j;
    }
}
// time Complexity: 
// Space Complexity: 

for (let k = 0; k < n; ++k) {
    b = b + k;
}

// Time Complexity: O(n²)
// Space Complexity: O(1)

let a = 0;
for (let i = 0; i < n; ++i) {
    for (let j = n; j > i; --j) {
        a = a + i + j;
    }
}
// time Complexity: O(n²)
// Space Complexity: O(1)
