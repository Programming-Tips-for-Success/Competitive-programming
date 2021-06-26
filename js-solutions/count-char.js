// problem statement
// find top most repeated character in a string 

// input 
// hello world

// output 
// l (because it appears 3 times)

// Algo 
// count characters
// duplicate characters
function findTopRepeated(sentence) {

    const counterMap = {}
    for (const char of sentence) {
    if (counterMap[char]) {
    
    counterMap[ char ]++
    
    } else {
    counterMap[char] = 1
    
    }
    }
 
    let top = '';
    for (const char in counterMap) {
    if (!counterMap[top] || counterMap[char] > counterMap[top]) {
    top = char
    
    }
    }
    return top;
    
    }
    let character  = findTopRepeated('hello world');
    console.log(character)