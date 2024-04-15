// problem statement1- find top most repeated character in a string

// Algo
// count characters
// duplicate characters

// input - hello world

// output
// l (because it appears 3 times)

// problem statement2- Write a function which takes in a string and returns counts of each character in the string.

function findTopRepeated(sentence) {
  const counterMap = {};
  for (const char of sentence) {
    if (counterMap[char]) {
      counterMap[char]++;
    } else {
      counterMap[char] = 1;
    }
  }
  console.log(counterMap)
  let top = '';
  for (const char in counterMap) {
    if (!counterMap[top] || counterMap[char] > counterMap[top]) {
      top = char;
    }
  }
  return top;
}

function print(x){
console.log(x);

}

let character  = findTopRepeated('hello world');
console.log(character, 'char')



// node basic-dsa/count-char.js
