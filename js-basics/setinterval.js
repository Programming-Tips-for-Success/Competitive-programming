var timesRun = 0;
var interval = setInterval(function(){
    timesRun += 1;
    if(timesRun === 4){
        clearInterval(interval);
    }
  console.log('timer')
}, 100); 


// node js-basics/setinterval.js