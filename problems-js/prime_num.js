function isPrime(n) { 
 for (let x = 2; x * x <= n; x++) { 
 if (n % x == 0) { 
 return false; 
 } 
 } 
 return true;
}

console.log(isPrime(4));

// node problems-js/prime_num.js
