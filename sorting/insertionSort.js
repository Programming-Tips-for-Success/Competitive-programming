
function sortD(data){
for (let i = 0; i <= data.length; i++) {
    let j = i;
    while (j > 0 && data[i] < data[j - 1])
      j--;
    let tmp = data[i];
    for (let k = i; k > j; k--){
      data[k] = data[k - 1];
    data[j] = tmp;
    }
  }
  return data;

}

const val = [2, 3, 1, 4];
const rt = sortD(val);
console.log(rt, 'rt')

// node sorting/insertionSort.js