
class Chameleon {
  static colorChange(newColor) {
    this.newColor = newColor;
    return this.newColor;
  }

  constructor({ newColor = "green" } = {}) {
    this.newColor = newColor;
  }
}

class Student {
    constructor(firstName, lastName){
        this.firstName = firstName;
        this.lastName = lastName;
    }
    
    fullName(){
        return `Your full name is ${this.firstName} ${this.lastName}`;
    }
    
    static enrollStudents(...students){
      print(students)
        // maybe send an email here
    }
}

class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  static distance(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;

    return Math.hypot(dx, dy);
  }
}

function print(x){
console.log(x);

}

const p1 = new Point(5, 5);
const p2 = new Point(10, 10);

print(Point.distance(p1, p2)); // 7.0710678118654755

let firstStudent = new Student("Colt", "Steele");
let secondStudent = new Student("Blue", "Steele");

Student.enrollStudents([firstStudent, secondStudent])

// const freddie = new Chameleon({ newColor: "purple" });
// console.log(freddie.colorChange('orange')); // error
console.log(Chameleon.colorChange("orange")); // orange

// node basic-dsa/static_class
