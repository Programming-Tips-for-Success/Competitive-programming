objArray = [{ name: 'kuhuk' }, { name: 'kuhukvh' }]
array = ['kuhuk', 'kuhukvh']

for (let i of objArray) {
  console.log(i, 'AOO')
}

for (let i of array) {
  console.log(i, 'arr')
}



objArray.forEach((i, e) => {
  console.log(i, e, 'for_each')
})
for (let i in objArray) {
  console.log(i, 'AOO2')
}
for (let i in array) {
  console.log(i, 'arr2')
}

console.time('loop')  
for (let i = 0; i < 100; i++) {    
  // Do stuff here  
}  
console.timeEnd('loop')

// tricky question-
let arr = [1,2 ,4, 6 ];
arr.forEach((el)=>{
if(el == 2) {
return el;
}
console.log(el)
})

          // node js-basics/for-loop.js