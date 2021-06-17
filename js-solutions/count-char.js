// count characters
// duplicate characters

// problem statement
// find top most repeated character in a string basically you need to find 


// input hello world
// output l (because it appears 3 times)
// Algo 

function findTopRepeated(sentence) {

    const counterMap = {}
    for (const char of sentence) {
    if (counterMap[char]) {
    
    counterMap[ char ]++
    
    } else {
    counterMap[char] = 1
    
    }
    }
    console.log(counterMap)
    
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