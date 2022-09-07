

function sortD(data){
for (let i = 0; i < data.length; i++){
for (let j = 0; j < data.length - 1; j++){
  if (data[j] > data[j + 1]) {
    tmp = data[j];
    data[j] = data[j + 1];
    data[j + 1] = tmp;
  }
}
}
  return data;
}

const val = [2, 3, 1, 4];
const rt = sortD(val);
console.log(rt, 'rt')

// node sorting/Bubble-sort.js