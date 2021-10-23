 
console.log(.1+.2); // 0.30000000000000004

function areTheNumbersAlmostEqual(num1, num2) {
    return Math.abs( num1 - num2 ) < Number.EPSILON;
}
console.log(areTheNumbersAlmostEqual(0.1 + 0.2, 0.3))


// node js-basics/Floating-point.js