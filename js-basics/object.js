var Food = {
    cuisine: 'abc'
    }
    
    var food1 = Object.create(Food);
    delete food1.cuisine
    console.log(food1.cuisine, Food, food1); // abc { cuisine: 'abc' } {}

    //  copy object problem-
     let obj = {
        a: 1,
        b: 2,
        c: {
            age: 30
        }
    };
    // var objclone = Object.assign({},obj);
    var objclone = {...obj};

    console.log('objclone: ', objclone); // { a: 1, b: 2, c: { age: 30 } }
    obj.c.age = 45;
    console.log('After Change - obj: ', obj);           // 45 - This also changes  { a: 1, b: 2, c: { age: 45 } }
    console.log('After Change - objclone: ', objclone); // 45  { a: 1, b: 2, c: { age: 45 } }
     

    // solution ?

    // value update ?
    var a={},
        b={key:'b'},
        c={key:'c'};
    a[b]=123;
    a[c]=456;
    console.log(a[b], a[c]); // 456 456
    

    var checkProp = { hasownProperty: 1, foo: 2 };

console.log(checkProp.hasOwnProperty('foo'), 'hasOwnProperty');   // true



//  node js-basics/object.js   