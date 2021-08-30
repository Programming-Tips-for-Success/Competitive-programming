
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
    sortedContacts.sort()
    let finalContact = !sortedContacts.length ? "NO CONTACT" :
        sortedContacts[0];
    return finalContact;
}

console.log(solution( ["pim", "pom"], ["999999999", "777888999"], "88999")) // pom


console.log(['a','c', 'b', 'A', 1].sort())
console.log(['ab','ca', 'ba','ac', 'A', 1].sort())


// node js-solutions/contact-search.js