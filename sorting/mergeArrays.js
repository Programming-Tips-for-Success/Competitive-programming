// Merges two already sorted arrays

// Create an empty array, take a look at the smallest values in each input array
// While there are still values we haven't looked at...
// If the value in the first array is smaller than the value in the second array, push the value in the first array into our results and move on to the next value in the first array
// If the value in the first array is larger than the value in the second array, push the value in the second array into our results and move on to the next value in the second array
// Once we exhaust one array, push in all remaining values from the other array

function merge(arr1, arr2){
    let results = [];
    let i = 0;
    let j = 0;
    while(i < arr1.length && j < arr2.length){
        if(arr2[j] > arr1[i]){
            results.push(arr1[i]);
            i++;
        } else {
            results.push(arr2[j])
            j++;
        }
    }
    while(i < arr1.length) {
        results.push(arr1[i])
        i++;
    }
    while(j < arr2.length) {
        results.push(arr2[j])
        j++;
    }
    return results;
}

function print(x) {
  console.log(x);
}

// print(merge([100,200], [1,2,3,5,6]))

var arr1 = [1,3,4,5];
var arr2 = [2,4,6,8];
print(merge(arr1,arr2) )

var arr3 = [-2,-1,0,4,5,6];
var arr4 = [-3,-2,-1,2,3,5,7,8];
 
print(merge(arr3,arr4)); // [-3,-2,-2,-1,-1,0,2,3,4,5,5,6,7,8]
 
var arr5 = [3,4,5]
var arr6 = [1,2]
 
print(merge(arr5,arr6)) // [1,2,3,4,5]
 
var names = ["Bob", "Ethel", "Christine"]
var otherNames = ["M", "Colt", "Allison", "SuperLongNameOMG"]
 
function stringLengthComparator(str1, str2) {
  return str1.length - str2.length;
}
 
 // todo
// print(merge(names, otherNames, stringLengthComparator)); // ["M", "Bob", "Colt", "Ethel", "Allison", "Christine", "SuperLongNameOMG"]

// node sorting/mergeArrays.js

                   