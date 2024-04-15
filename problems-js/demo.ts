  console.log('fd')
const myPhoneFunction = (opts) => {
    // ...
    // if (opts.phoneNumbr){
        // doStuff();
    // }

    console.log(opts)

}

myPhoneFunction({name: 'hi', phoneNumbr:44});

interface Test{
  phoneNumbr?: number;
  name?: string;
}

// node problems-js/demo.ts