// Many sorting algorithms involve some type of swapping functionality (e.g. swapping to numbers to put them in order)



// ES5
function swap(arr, idx1, idx2) {
  var temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

// ES2015
const swap = (arr, idx1, idx2) => {
  [arr[idx1],arr[idx2]] = [arr[idx2],arr[idx1]];
}

function print(x){
console.log(x);

}

// node basic-dsa/swapping