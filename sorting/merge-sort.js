function mergeSort(data) {
    if (data.Length == 1)
        return data;
    let middle = data.Length / 2;
    // let left = mergeSort(subArray(data, 0, middle - 1));
    // let right = mergeSort(subArray(data, middle, data.Length - 1));
      let left = (data.slice(0, middle - 1));
    let right = (data.slice(middle, data.Length - 1));
    let result = new Array[data.Length];
    let dPtr = 0;
    let lPtr = 0;
    let rPtr = 0;
    while (dPtr < data.Length) {
        if (lPtr == left.Length) {
            result[dPtr] = right[rPtr];
            rPtr++;
        } else if (rPtr == right.Length) {
            result[dPtr] = left[lPtr];
            lPtr++;
        } else if (left[lPtr] < right[rPtr]) {
            result[dPtr] = left[lPtr];
            lPtr++;
        } else {
            result[dPtr] = right[rPtr];
            rPtr++;
        }
        dPtr++;
    }
    return result;
}

const val = [2, 3, 1, 4];
const rt = mergeSort(val);
console.log(rt, 'rt')

// node sorting/merge-sort.js
