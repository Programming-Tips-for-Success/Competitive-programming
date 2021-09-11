people = [{name:'kuhuk'}, {name:'kuhukvh'}]
people2 = ['kuhuk', 'kuhukvh']

for(let i of people){ 
console.log(i, 'AOO')
  }
  
for(let i of people2){ 
  console.log(i, 'arr')
    }


      
      people.forEach((i, e)=>{
    console.log(i, e, 'for_each')
      })
      for(let i in people){
        console.log(i, 'AOO2')
          }
      for(let i in people2){
        console.log(i, 'arr2')
          }

          // node js/for-loop.js