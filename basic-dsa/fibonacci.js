
// fib(4) // 3
// fib(10) // 55
// fib(28) // 317811
// fib(35) // 9227465

function fib(n){
    if (n <= 2) return 1;
    return fib(n-1) + fib(n-2);
}

function fibonacci(n) {
    const arr = [0, 1];
    for (let i = 2; i <= n; ++i) {
        arr.push(arr[i - 2] + arr[ i - 1]);
    }
    return arr[n - 1];
}

function print(x){
console.log(x);

}

console.log("fib", fibonacci(5));

// Time Complexity: 
// space Complexity: 

// node basic-dsa/fibonacci.js
