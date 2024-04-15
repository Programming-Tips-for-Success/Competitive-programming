
// problem
// Get search results from the save contacts for the number you entered.

function solution(namesList, numberList, searchedNumber) {
    var contacts = [];
    for (i = 0; i < numberList.length; i++) {

        if (numberList[i].includes(searchedNumber)) {
            contacts.push(namesList[i]);
        }

    }
    let sortedContacts = contacts;
    console.log(sortedContacts, 'jhb')
    sortedContacts.sort()
    let finalContact = !sortedContacts.length ? "NO CONTACT" :
        sortedContacts[0];
    return finalContact;
}

function print(x){
console.log(x);

}

function numberCompare(num1, num2) {
  return num1 - num2;
}

function compareByLen(str1, str2) {
  return str1.length - str2.length;
}



print(solution( ["pim", "pom"], ["999999999", "777888999"], "88999")) // pom


print(['a','c', 'b', 'A', 1].sort())
print(['ab','ca', 'ba','ac', 'A', 1].sort())
print([ 6, 4, 15, 10 ].sort())
print([ 6, 4, 15, 10 ].sort(numberCompare)); // [ 4, 6, 10, 15 ]
print([ "Steele", "Colt", "Data Structures", "Algorithms" ].sort(compareByLen)); // [ "Colt", "Steele", "Algorithms", "Data Structures" ]

// node basic-dsa/contact-search.js