people = [{name:'kuhuk'}, {name:'kuhukvh'}]
people2 = ['kuhuk', 'kuhukvh']

for(let i of people){ 
console.log(i, 'of')
  }

for(let i in people){
    console.log(i, 'in')
      }
      
      people.forEach((i, e)=>{
    console.log(i, e, 'for_each')
      })

      for(let i in people2){
        console.log(i, 'arr')
          }