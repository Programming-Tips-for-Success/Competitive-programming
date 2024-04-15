// HELPER METHOD RECURSION

function outer(input){
    
    var outerScopedVariable = []

    function helper(helperInput){
        // modify the outerScopedVariable
        helper(helperInput-1)
    }
    
    helper(input)

    return outerScopedVariable;

}

function collectOddValues(arr){
    
    let result = []

    function helper(helperInput){
        if(helperInput.length === 0) {
            return;
        }
        
        if(helperInput[0] % 2 !== 0){
            result.push(helperInput[0])
        }
        
        helper(helperInput.slice(1))
    }
    
    helper(arr)

    return result;

}

// PURE RECURSION

function collectOddValuesWith(arr){
    let newArr = [];
    
    if(arr.length === 0) {
        return newArr;
    }
        
    if(arr[0] % 2 !== 0){
        newArr.push(arr[0]);
    }
        
    newArr = newArr.concat(collectOddValues(arr.slice(1)));
    return newArr;
}

function print(x){
console.log(x);

}

print(collectOddValuesWith([1, 2, 3,4]))
// node basic-dsa/outerScopedVariable.js