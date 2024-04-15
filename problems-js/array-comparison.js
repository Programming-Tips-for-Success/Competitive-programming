// problem statement - compare arrays
// two people getting married both have invitee list find out they both want to invite exact same people

// input 
// 2 array

// output 
// check list same or not return boolean



function verifyAllEqual(list1, list2) {
    // fail fast if both Lists are not the same Length
    if (list1.length !== list2.length) return false;

    let map = {};

    // loop through list 1, fill the hashmap, count characters
    for (let num of list1) {
        if (map[num] == null) {
            map[num] = 1;
        } else {
            map[num]++;
        }
    }

    // loop through list 2, decrease character count on hashmap
    for (let num of list2) {

        if (map[num] == null) return false;

        map[num]--;

    }

    // if any count is greater than 6, both Lists are not identical
    for (let val in map) {
        if (map[val] !== 0)
            return false;

    }

    return true;
}

console.log(verifyAllEqual([1, 2, 3], [3, 2, 1]));


// node problems-js/array-comparison.js
