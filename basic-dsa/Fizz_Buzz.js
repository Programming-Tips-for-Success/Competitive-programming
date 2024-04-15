// FizzBuzz is a task where the programmer is asked to print numbers from 1 to n, but here’s the catch, multiple of three should print “Fizz” and similarly print “Buzz” for multiples of 5 and lastly print “FizzBuzz” for multiples of three and five.
function fizzBuzz(n){
      const answer = []

for (var i = 1; i < n; i++) {
    if (i % 15 == 0) {
      answer.push('FizzBuzz') ;
      console.log("FizzBuzz")
      }
    else if (i % 3 == 0) {console.log("Fizz")}
    else if (i % 5 == 0) {console.log("Buzz")}
    else {console.log(i)};
}
}

// node basic-dsa/Fizz_Buzz.js
