// Complete the following plus and minus functions such that ...

// Test Case 1

// plus(2).plus(3).value() returns 5

// i.e. 2 + 3 = 5

// Test Case 2

// plus(4).minus(2).value() returns 2

// i.e. 4 - 2 = 2

// Test Case 3

// plus(5).minus(3).plus(6).minus(1).value() returns 7

// i.e. 5 - 3 + 6 - 1 = 7

const plusminus = function () {
  let final = 0;
  plusminus.prototype.plus = function (value) {
    final += value;
    return this;
  };
  plusminus.prototype.minus = function (value) {
    final -= value;
    return this;
  };
  plusminus.prototype.value = function (value) {
    return final;
  };
};

function plus(value) {
  return new plusminus().plus(value);
}

function minus(value) {
  return new plusminus().minus(value);
}

function value() {
  return new plusminus().minus(value);
}

console.log(plus(2).plus(3).value());
// node problems-js/plusminus.js
