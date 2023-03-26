const shape = {
  radius: 10,
  diameter() {
    return this.radius * 2;
  },
  perimeter: () => 2 * Math.PI * this.radius,
  // perimeter() {return  2 * Math.PI * this.radius},
};

// console.log(shape.diameter()); // 20
// console.log(shape.perimeter()); // NaN

class Chameleon {
  static colorChange(newColor) {
    this.newColor = newColor;
    return this.newColor;
  }

  constructor({ newColor = "green" } = {}) {
    this.newColor = newColor;
  }
}

const freddie = new Chameleon({ newColor: "purple" });
// console.log(freddie.colorChange('orange')); // error
// console.log(Chameleon.colorChange("orange")); // orange

// for (let i = 0; i < 3; i++) { 
//   setTimeout(() => console.log(i), 1);
// }

// for(let k1=0; k1<5; k1++) {} console.log(k1); 

//  function func() { console.log("User1") } function func() { console.log("User2") } function func() { console.log("User3") } function func() { console.log("User4") } func(); 
//  const fnc=(function(a) { delete a; return a; })(7); 
//  console.log(fnc) 
//  for (var i = 0; i < 3; i++) { setTimeout(() => console.log(i), 1);
// }

// var a=5 , b=1

// var obj = { a : 10 }

// with(obj)

// {

// console.log(b)

// }

  

function print() {
  console.log(this, 'function'); // print() {}
 }
 
 let print2 = () => { 
  console.log(this, 'arrow'); // undefined
 }
 
 print();
 print2();

// node problems-js/tricky.js
