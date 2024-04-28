
const memoizedAdd = () => {
    // cache can remember its values since the returned function has a closure over it.
  
  let cache = {};
  
  return (n) => {
  
    if (n in cache) {
  
      console.log('Fetching from cache');
  
      return cache[n];
  
    }
  
    else {
  
      console.log('Calculating result');
  
      let result = n + 10;
  
      cache[n] = result;
  
      return result;
  
    }
  
  }
  
  }
  
  // returned function from memoizedAdd
  
  const newAdd = memoizedAdd();
  
  console.log(newAdd(9)); // calculated
  
  console.log(newAdd(9)); // cached
  
//   ========================= another example ========================= cache approach
function factorial(n) {
    if (n > 0) {
    
      if (!(n in factorial))  // Check if we already have the result cached.
    
        factorial[n] = n * factorial(n-1);
    
      return factorial[n];
    
    }
    
    return NaN;
    
    }
    
    factorial[1] = 1; // Cache the base case.
    
    console.log(factorial(5))
    // ==================
    const memoize = (fn) => {
      let cache = {};
      
      return (...args) => {
      
        let n = args[0];
      
        if (n in cache) {
      
          console.log('Fetching from cache', n);
      
          return cache[n];
      
        }
      
        else {
      
          console.log('Calculating result', n);
      
          let result = fn(n);
      
          cache[n] = result;
      
          return result;
      
        }
      
      }
      
      }
      
      const factorial = memoize(
      
      (x) => {
      
        if (x === 0) {
      
        return 1;
      
        }
      
        else {
      
          return x * factorial(x - 1);
      
        }
      
      }
      
      );
      
      console.log(factorial(5)); // calculated
      
      console.log(factorial(6)); // calculated for 6 and cached for 5
      // example:
      var wrapCache = function(f, fKey){
        fKey = fKey || function(id){ return id; };
      
        var cache = {};
      
      
        return function(key){
      
            var _key = fKey(key); 
      
            if (!cache[_key]){
      
                cache[_key] = f(key);
      
            };
      
      
            return cache[_key];
      
      };
      
      };
      
      
      // functions that expensive
      
      var getComputedRGB = function(n){
      
        console.log("getComputedRGB called", n) ;
      
        return n * n * n; 
      
      };
      
      
      // wrapping expensive
      
      var getComputedRGBCache = wrapCache(getComputedRGB, JSON.stringify);
      
      
      console.log("normal call");
      
      console.log(getComputedRGB(10));
      
      console.log(getComputedRGB(10));
      
      console.log(getComputedRGB(10));
      
      console.log(getComputedRGB(10));
      
      // compute 4 times
      
      
      
      console.log("cached call") ;
      
      console.log(getComputedRGBCache(10));
      
      console.log(getComputedRGBCache(10));
      
      console.log(getComputedRGBCache(10));
      
      console.log(getComputedRGBCache(10));
      
    //   compute just 1 times
    //  output
    //   => normal call  
      
    //   getComputedRGB called 10
      
    //   1000
      
    //   getComputedRGB called 10
      
    //   1000
      
    //   getComputedRGB called 10
      
    //   1000
      
    //   getComputedRGB called 10
      
    //   1000
      
       
      
    //   => cached call
      
    //   getComputedRGB called 10
      
    //   1000
      
    //   1000
      
    //   1000
      
    //   1000