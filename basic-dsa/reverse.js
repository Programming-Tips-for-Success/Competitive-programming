// Write a recursive function called reverse which accepts a string and returns a new string in reverse.

function reverse(str){
	if(str.length <= 1) return str;
	return reverse(str.slice(1)) + str[0];
}

function print(x){
console.log(x);

}

// reverse('awesome') // 'emosewa'
// reverse('rithmschool') // 'loohcsmhtir'

//  node basic-dsa/reverse.js
